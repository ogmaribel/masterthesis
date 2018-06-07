"""
.. module:: Boss_spectral

Boss_spectral
*************

:Description: Boss_spectral

    

:Authors: bejar
    

:Version: 

:Created on: 03/03/2017 9:39 

"""

__author__ = 'bejar'

import sys
sys.path.append('/Users/maribelojeda/WalkAnalysis-master')
from iWalker.Data import User, Exercise, Exercises, Pacientes, Trajectory
from iWalker.Util.Misc import show_list_signals
from iWalker.Util import Boss, boss_distance, euclidean_distance, bin_hamming_distance, hamming_distance,\
    cosine_similarity
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as colors
import collections
import csv
import Variables
from random import randint
import pandas as pd


# colors = "rgbymcykrgbymcyk"


if __name__ == '__main__':
                
    p = Pacientes()
    e = Exercises()

    p.from_db(pilot='NOGALES')
    e.from_db(pilot='NOGALES')

    # e.delete_exercises([1425290750])
    
    #create random variables
    
    
    wlen = 127

    nseries = 0
    lcl = []

  #  print('primer print',len(e.edict))
    for ex in e.iterator():
        t = Trajectory(ex.get_coordinates())
        if t.straightness()[0] < 0.95:
            e.delete_exercises([ex.id])
   # print('segundo print ',len(e.edict))
    for ex in e.iterator():
        t = Trajectory(ex.get_coordinates())
        if t.straightness()[0] < 0.95:
            e.delete_exercises([ex.id])
            
    for ex in e.iterator():
        forces = ex.get_forces()
        if forces.shape[0] > wlen:
            nseries += 1
        else:
            e.delete_exercises([ex.id])
            
    print('tercer print ',len(e.edict))

    mdist = np.zeros((nseries, nseries))
    
   # print('cuarto print ',nseries)
    for f in range(6):
        dseries = {}
        for ex in e.iterator():
            forces = ex.get_forces()
            if forces.shape[0] > wlen:
                dseries[str(ex.uid) + '#' + str(ex.id)] = forces[:, f]
    
    
    msearch=['1425572016',	'1425572045',	'1425555855',	'1425555880',	'1424964678',	'1424964712',	'1424965463',	'1424965495',	'1424966175',	'1424966214',	'1424966840',	'1424967801',	'1424967845',	'1424968950',	'1424968992',	'1424970366',	'1424970412',	'1424971305',	'1424971345',	'1424972915',	'1424972980',	'1425034102',	'1425034133',	'1425037581',	'1425037618',	'1425288797',	'1425288830',	'1425291229',	'1425291265',	'1425292071',	'1425292125',	'1425293574',	'1425293602',	'1425294623',	'1425294655',	'1425295284',	'1425295325',	'1425311441',	'1425311480',	'1425313553',	'1425313602',	'1425315713',	'1425316403',	'1425316429',	'1425317818',	'1425317861',	'1425374738',	'1425374768',	'1425375444',	'1425375480',	'1425376487',	'1425376527',	'1425377398',	'1425377447',	'1425378214',	'1425378253',	'1425379172',	'1425379200',	'1425379906',	'1425379949',	'1425382054',	'1425382113',	'1425399361',	'1425399396',	'1425399890',	'1425399932',	'1425401377',	'1425401404',	'1425402404',	'1425402441',	'1425403115',	'1425403181',	'1425462508',	'1425462549',	'1425463388',	'1425463425',	'1425464532',	'1425464577',	'1425466298',	'1425466341',	'1425468227',	'1425468273',	'1425484520',	'1425484570',	'1425485291',	'1425485329',	'1425485931',	'1425485966',	'1425486818',	'1425486861',	'1425487748',	'1425487792',	'1425489597',	'1425550161',	'1425550200',	'1425551207',	'1425551245',	'1425552062',	'1425552088',	'1425555092',	'1425555132',	'1425571115',	'1425571166',	'1425572684',	'1425572713',	'1425573452',	'1425573485',	'1425575125',	'1425575168',	'1425577392',	'1425577469']    
    #Recuperar las fuerzas
    getforces1 = {}
    getforces2 = {}
    getforces3 = {}
    getforces4 = {}
    getforces5 = {}
    getforces6 = {}
    
    print(msearch[0])
    
    for ex in e.iterator():
        getforces1[str(ex.id)]= ex.get_forces()[:,0]
        getforces2[str(ex.id)]= ex.get_forces()[:,1]
        getforces3[str(ex.id)]= ex.get_forces()[:,2]
        getforces4[str(ex.id)]= ex.get_forces()[:,3]
        getforces5[str(ex.id)]= ex.get_forces()[:,4]
        getforces6[str(ex.id)]= ex.get_forces()[:,5]
    
    for g in range(0,len(msearch)): 
        val1 = dict(getforces1)[msearch[g]]
        val2 = dict(getforces2)[msearch[g]]
        val3 = dict(getforces3)[msearch[g]]
        val4 = dict(getforces4)[msearch[g]]
        val5 = dict(getforces5)[msearch[g]]
        val6 = dict(getforces6)[msearch[g]]

'''
        with open("getforces1.csv", "a") as f:         
                 writer = csv.writer(f)
                 writer.writerow(val1)
        with open("getforces2.csv", "a") as f:         
                 writer = csv.writer(f)
                 writer.writerow(val2)
        with open("getforces3.csv", "a") as f:         
                 writer = csv.writer(f)
                 writer.writerow(val3)
        with open("getforces4.csv", "a") as f:         
                 writer = csv.writer(f)
                 writer.writerow(val4)
        with open("getforces5.csv", "a") as f:         
                 writer = csv.writer(f)
                 writer.writerow(val5)
        with open("getforces6.csv", "a") as f:         
                 writer = csv.writer(f)
                 writer.writerow(val6)
   
'''