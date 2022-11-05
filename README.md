# Again X assignment

## Setup
First install the requirements by `pip install -r requirements.txt`

## Run
Simple run the main file: `python main.py`

## Notes:
- I removed lots of columns that I think are useless since they were mostly null values (more than 70% null)
- There was a column in building table that show the geometric properties of the building. I converted it based on the preprocessing described in [this paper](https://arxiv.org/pdf/1806.03857.pdf)
- The output of the code is two csv file next to `main.py`