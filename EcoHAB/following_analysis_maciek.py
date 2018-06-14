# -*- coding: utf-8 -*-   
from __future__ import division, print_function
import interactions
import sys
import plotfunctions
import numpy as np
import matplotlib.pyplot as plt

antenna_pos = {
    "/home/jszmek/EcoHAB_data_November/Maciek_01_30_2018":{'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8},
    "/home/jszmek/EcoHAB_data_November/Maciek_social_structure_16.01":{'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8},
    "/home/jszmek/EcoHAB_data_November/Maciek_social_structure_19.01.18_rep_II":{'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8},
    "/home/jszmek/EcoHAB_data_November/C57 30.04-11.05 LONG TIMP/":{'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8},
    "/home/jszmek/EcoHAB_data_November/C57 males long 11-22.05.18/":{'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8},
    "/home/jszmek/EcoHAB_data_November/C57_males_long_26.05-06.06.2018_after_TIMP/":
    {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8}
}

a_dirs  = [
    #"/home/jszmek/EcoHAB_data_November/Maciek_01_30_2018",
    #"/home/jszmek/EcoHAB_data_November/Maciek_social_structure_16.01",
    #"/home/jszmek/EcoHAB_data_November/Maciek_social_structure_19.01.18_rep_II",
    # "/home/jszmek/Results_EcoHAB_data_November/do_analizy_in_z_cohort_z_sociability_z_numerami_transponderow/Social structure males 02.03/",
    # '/home/jszmek/Results_EcoHAB_data_November/do_analizy_in_z_cohort_z_sociability_z_numerami_transponderow/social_dominance_swiss_webster_dominant_remove_12.02.18',
    # '/home/jszmek/Results_EcoHAB_data_November/do_analizy_in_z_cohort_z_sociability_z_numerami_transponderow/social_structure_16.01',
    # '/home/jszmek/Results_EcoHAB_data_November/do_analizy_in_z_cohort_z_sociability_z_numerami_transponderow/social_structure_19.01.18_rep_II',
    # '/home/jszmek/Results_EcoHAB_data_November/do_analizy_in_z_cohort_z_sociability_z_numerami_transponderow/social_structure_swiss_webster_ctrl_05.02.18',
    
     #'/home/jszmek/EcoHAB_data_November/C57 TIMP rep 2/',
     #'/home/jszmek/EcoHAB_data_November/C57 males TIMP/',
    "/home/jszmek/EcoHAB_data_November/mice K Wisniewska/",
    #"/home/jszmek/EcoHAB_data_November/C57 30.04-11.05 LONG TIMP/",
    #"/home/jszmek/EcoHAB_data_November/C57 males long 11-22.05.18/",
    #"/home/jszmek/EcoHAB_data_November/C57 13-24.04 long/",
    #"/home/jszmek/EcoHAB_data_November/C57 30.04-11.05 LONG TIMP/",
    #"/home/jszmek/EcoHAB_data_November/long_experiment_WT",
    #"/home/jszmek/EcoHAB_data_November/C57_males_long_26.05-06.06.2018_after_TIMP/",
]

masks = {"/home/jszmek/EcoHAB_data_November/Maciek_01_30_2018":[],
         "/home/jszmek/EcoHAB_data_November/Maciek_social_structure_16.01":[],
         "/home/jszmek/EcoHAB_data_November/Maciek_social_structure_19.01.18_rep_II":[],
         "/home/jszmek/EcoHAB_data_November/C57 13-24.04 long/":[],
         "/home/jszmek/EcoHAB_data_November/mice K Wisniewska/":[],
         "/home/jszmek/EcoHAB_data_November/C57 30.04-11.05 LONG TIMP/":[],
          '/home/jszmek/EcoHAB_data_November/C57 males TIMP/': [],
          "/home/jszmek/EcoHAB_data_November/C57 males long 11-22.05.18/":[],
          "/home/jszmek/EcoHAB_data_November/C57_males_long_26.05-06.06.2018_after_TIMP/":[],
}
phases = {"/home/jszmek/EcoHAB_data_November/Maciek_01_30_2018":["ALL"],
          "/home/jszmek/EcoHAB_data_November/Maciek_social_structure_16.01":['ALL'],
          "/home/jszmek/EcoHAB_data_November/Maciek_social_structure_19.01.18_rep_II":['ALL'],
          "/home/jszmek/EcoHAB_data_November/C57 13-24.04 long/":['ALL',],
          # ['SNIFF 11 dark',
          # 'END',
          # 'BEGINNING',
          # 'MIDDLE'],
          "/home/jszmek/EcoHAB_data_November/mice K Wisniewska/":['ALL'],
          "/home/jszmek/EcoHAB_data_November/C57 30.04-11.05 LONG TIMP/":['ALL'],
          "/home/jszmek/EcoHAB_data_November/C57 males long 11-22.05.18/":["ALL"],
           "/home/jszmek/EcoHAB_data_November/C57_males_long_26.05-06.06.2018_after_TIMP/":["ALL"], #["MIDDLE", "BEGINNING", "END"]
          '/home/jszmek/EcoHAB_data_November/C57 males TIMP/': ["ALL"],
          #'END',
          #'BEGINNING',
          #'MIDDLE'],
}

ts = 3   
window=12

IPP = {}
FAM = {}
sections = {}
directories = {}
endings = {}
mice = {}
for a_dir in a_dirs:
    IPP[a_dir] = []
    FAM[a_dir] = []
    sections[a_dir] = []
    directories[a_dir] = []
    endings[a_dir] = []
    mice[a_dir] = []
    
    if a_dir not in antenna_pos:
        antenna_pos[a_dir] = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8}
    if masks[a_dir] == []:
        
        for phase in phases[a_dir]:
            E = interactions.Experiment(a_dir,_ant_pos=antenna_pos[a_dir],which_phase=phase)#,remove_mice=['0065-0136657055'] )
            if phase == 'ALL':
                E.calculate_antenna_errors()
            fname = 'Interactions_' + E.fname_ending
            #E.tube_dominance_test(window=window)
            #E.plotTubeDominanceRasters(mice=E.mice)
            E.calculate_fvalue(window=window, threshold=ts, force=True)
            print(E.cf.sections())
            E.write_tables_to_file("following")
            E.write_tables_to_file("avoiding")
            E.write_tables_to_file("FAM")
            E.generate_heatmaps("following")
            E.generate_heatmaps("avoiding")
            E.plot_fam()
    else:
        for mask in masks[a_dir]:
            E = interactions.Experiment(a_dir,_ant_pos=antenna_pos[a_dir],mask=mask)
          
            fname = 'Interactions_' + E.fname_ending
            E.tube_dominance_test(window=window)
            E.plotTubeDominanceRasters(mice=E.mice)
            E.calculate_fvalue(window=window, threshold=ts, force=True)
            IPP[a_dir].append(E.InteractionsPerPair(0,2))
            FAM[a_dir].append(E.FollowingAvoidingMatrix())
            sections[a_dir].append(E.cf.sections())
            directories[a_dir].append(E.directory)
            endings[a_dir].append(E.fname_ending)
            mice[a_dir].append(E.mice)
            E.write_following_avoiding_to_file()
            E.calculate_antenna_errors()
                                

scalefactor = 0
print(mice)

for a_dir in a_dirs:
    maxi = 0

    for ipp in IPP[a_dir]:
        if np.max(ipp) > maxi:
            maxi = np.max(ipp)
    scalefactor += maxi
