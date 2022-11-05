import shutil
import os

import geopandas as gpd
from tqdm import tqdm
import numpy as np

from .constants import HIGH_NULLS
from .constants import BATCH_SIZE


def geometry_encoding(x):
    if not x:
        return [[0]*5]
    geoms = []
    for i, geo in enumerate(x.geoms):
        try:
            poses = np.array(geo.boundary.coords)
        except NotImplementedError:
            continue
        pos_embed = np.zeros((poses.shape[0], 3))
        emb = i+1
        pos_embed[0] = [emb, 0, 0]
        pos_embed[-1] = [0, 0, emb]
        pos_embed[1:-1] = [0, emb, 0]
        geoms.append(np.hstack([poses, pos_embed]))
    if not len(geoms):
        return [[0]*5]
    return np.vstack(geoms)


class BatchReader:
    def __init__(self, file_name, layer, dtypes, batch_size=500):
        self.file_name = file_name
        self.layer = layer
        self.dtypes = dtypes
        self.current_batch = 0
        self.batch_size = batch_size

    def __iter__(self):
        self.current_batch = 0
        return self

    def __next__(self):
        batch = gpd.read_file(self.file_name, layer=self.layer,
                              rows=slice(self.current_batch * self.batch_size,
                                         (self.current_batch + 1) * self.batch_size),
                              dtypes=self.dtypes)
        self.current_batch += 1
        if not len(batch):
            raise StopIteration
        return batch


def convert_buildings_to_csv(path):
    fns = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('gpkg')]
    assert len(fns) == 1, f"Exactly one database expected found {len(fns)}: {fns}"
    file_name = fns[0]
    layer = 'batiment'
    files_path = f'{file_name}_csvs/buildings'
    shutil.rmtree(f'{files_path}', ignore_errors=True)
    os.makedirs(files_path)
    for i, b in tqdm(enumerate(BatchReader(file_name, layer=layer, dtypes=None, batch_size=BATCH_SIZE))):
        b['geom'] = b.geometry.apply(geometry_encoding)
        b.drop(['geometry'] + HIGH_NULLS, axis=1).to_csv(f'{files_path}/part{i:03d}.csv', index=False, header=not i)

    return files_path
