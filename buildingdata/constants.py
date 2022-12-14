BATCH_SIZE = 10_000

HIGH_NULLS = [
     'bnb_optim_status',
     'adedpe202006_l_ch_gen_princ',
     'adedpe202006_l_ecs_gen_princ',
     'adedpe202006_l_id',
     'adedpe202006_l_numero_dpe',
     'adedpe202006_logtype_avancee_masque_max',
     'adedpe202006_logtype_baie_fs',
     'adedpe202006_logtype_baie_mat',
     'adedpe202006_logtype_baie_orientation',
     'adedpe202006_logtype_baie_remplissage',
     'adedpe202006_logtype_baie_type_vitrage',
     'adedpe202006_logtype_baie_u',
     'adedpe202006_logtype_ch_gen_lib',
     'adedpe202006_logtype_ch_gen_lib_appoint',
     'adedpe202006_logtype_ch_gen_lib_princ',
     'adedpe202006_logtype_ch_is_solaire',
     'adedpe202006_logtype_ch_type_ener_corr',
     'adedpe202006_logtype_ch_type_inst',
     'adedpe202006_logtype_classe_conso_ener',
     'adedpe202006_logtype_classe_estim_ges',
     'adedpe202006_logtype_coherence_data_methode_dpe',
     'adedpe202006_logtype_conso_ener',
     'adedpe202006_logtype_date_reception_dpe',
     'adedpe202006_logtype_ecs_gen_lib',
     'adedpe202006_logtype_ecs_gen_lib_appoint',
     'adedpe202006_logtype_ecs_gen_lib_princ',
     'adedpe202006_logtype_ecs_is_solaire',
     'adedpe202006_logtype_ecs_type_ener',
     'adedpe202006_logtype_ecs_type_inst',
     'adedpe202006_logtype_enr',
     'adedpe202006_logtype_estim_ges',
     'adedpe202006_logtype_id',
     'adedpe202006_logtype_inertie',
     'adedpe202006_logtype_is_3cl',
     'adedpe202006_logtype_min_classe_ener_ges',
     'adedpe202006_logtype_mur_ep_mat_ext',
     'adedpe202006_logtype_mur_mat_ext',
     'adedpe202006_logtype_mur_pos_isol_ext',
     'adedpe202006_logtype_mur_u_ext',
     'adedpe202006_logtype_nom_methode_dpe',
     'adedpe202006_logtype_numero_dpe',
     'adedpe202006_logtype_pb_mat',
     'adedpe202006_logtype_pb_pos_isol',
     'adedpe202006_logtype_pb_type_adjacence',
     'adedpe202006_logtype_pb_u',
     'adedpe202006_logtype_perc_surf_vitree_ext',
     'adedpe202006_logtype_periode_construction',
     'adedpe202006_logtype_ph_mat',
     'adedpe202006_logtype_ph_pos_isol',
     'adedpe202006_logtype_ph_type_adjacence',
     'adedpe202006_logtype_ph_u',
     'adedpe202006_logtype_presence_balcon',
     'adedpe202006_logtype_presence_climatisation',
     'adedpe202006_logtype_ratio_ges_conso',
     'adedpe202006_logtype_s_hab',
     'adedpe202006_logtype_traversant',
     'adedpe202006_logtype_type_batiment',
     'adedpe202006_logtype_type_ventilation',
     'adedpe202006_max_conso_ener',
     'adedpe202006_max_estim_ges',
     'adedpe202006_mean_class_conso_ener',
     'adedpe202006_mean_class_estim_ges',
     'adedpe202006_mean_conso_ener',
     'adedpe202006_mean_estim_ges',
     'adedpe202006_min_conso_ener',
     'adedpe202006_min_estim_ges',
     'adedpe202006_nb_classe_ene_a',
     'adedpe202006_nb_classe_ene_b',
     'adedpe202006_nb_classe_ene_c',
     'adedpe202006_nb_classe_ene_d',
     'adedpe202006_nb_classe_ene_e',
     'adedpe202006_nb_classe_ene_f',
     'adedpe202006_nb_classe_ene_g',
     'adedpe202006_nb_classe_ene_nc',
     'adedpe202006_nb_classe_ges_a',
     'adedpe202006_nb_classe_ges_b',
     'adedpe202006_nb_classe_ges_c',
     'adedpe202006_nb_classe_ges_d',
     'adedpe202006_nb_classe_ges_e',
     'adedpe202006_nb_classe_ges_f',
     'adedpe202006_nb_classe_ges_g',
     'adedpe202006_nb_classe_ges_nc',
     'adedpe202006_std_conso_ener',
     'adedpe202006_std_estim_ges',
     'ancqpv201410_id',
     'ancqpv201410_nom_qp',
     'arcthd2021t1_l_nom',
     'anarnc202012_nb_log',
     'anarnc202012_nb_lot_garpark',
     'anarnc202012_nb_lot_tertiaire',
     'anarnc202012_nb_lot_tot',
     'anarnc202012_l_nom_copro',
     'anarnc202012_l_id',
     'igntop202103_equ_l_nat_detail',
     'igntop202103_equ_l_nature',
     'igntop202103_equ_l_toponyme',
     'igntop202103_zoa_l_nat_detail',
     'igntop202103_zoa_l_nature',
     'igntop202103_zoa_l_toponyme',
     'insbpe2019_l_id',
     'insbpe2019_l_type_equipement',
     'mcumer202007_dist500min',
     'mcumer202007_id',
     'mcumer202007_tico',
     'mtedle2019_elec_conso_pro',
     'mtedle2019_elec_conso_res',
     'mtedle2019_elec_conso_res_par_pdl_res',
     'mtedle2019_elec_conso_tot',
     'mtedle2019_elec_l_id',
     'mtedle2019_elec_nb_pdl_pro',
     'mtedle2019_elec_nb_pdl_res',
     'mtedle2019_elec_nb_pdl_tot',
     'mtedle2019_gaz_conso_pro',
     'mtedle2019_gaz_conso_res',
     'mtedle2019_gaz_conso_res_par_pdl_res',
     'mtedle2019_gaz_conso_tot',
     'mtedle2019_gaz_l_id',
     'mtedle2019_gaz_nb_pdl_pro',
     'mtedle2019_gaz_nb_pdl_res',
     'mtedle2019_gaz_nb_pdl_tot'
]
