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
from sklearn.manifold import MDS, Isomap, TSNE, SpectralEmbedding
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.mixture import BayesianGaussianMixture as Dirichlet
import matplotlib.colors as colors
import collections
import csv
import Variables
from random import randint
from sklearn.metrics import adjusted_rand_score
import pandas as pd
from sklearn.metrics import silhouette_score

# colors = "rgbymcykrgbymcyk"


if __name__ == '__main__':
    filename = "labs_cos3_125140_test.csv"
    
    #print("creating array")

    inivar= np.array(([125,4,2,3],
[126,4,2,3],
[127,4,2,3],
[128,4,2,3],
[130,4,2,3],
[135,4,2,3]))
    
    for e in range(0, 6):
        wlen = inivar[e,0]
        voclen = inivar[e,1]
        ncoefs = inivar[e,2]
        
        dimension=inivar[e,3]
        clustn=10
        ctype=1
        
        data=[wlen, voclen, ncoefs, dimension]
        with open(filename, "a") as f:         
            writer = csv.writer(f)
            writer.writerow(data)
            writer.writerow(" ")
        
        nseries = 42
        lcl = []
    
    
    
        mdist = np.zeros((nseries, nseries))
    
         
                
        for f in [0,1,2,3,4,5]:
            dseries = {}
            for g in range(1,43):
                num=g
                nums='cvi'+str(num)
                filen='/Users/maribelojeda/Desktop/MIT/I-WALKER/i-walker-Atia/terceranalisis/Straightpath/'+nums+ '.mat.csv'
                reader = csv.reader(open(filen, "rb"), delimiter=",")
                x = list(reader)
                x.pop(0)
                result = np.array(x).astype("float") 
                dseries[nums] = result[:, f]
    
            boss = Boss(dseries, 10, butfirst=True)
            boss.discretization_intervals(ncoefs, wlen, voclen)
            boss.discretize()
            lcodes = sorted(list(boss.codes.keys()))
            #lcodes = list(boss.codes.keys())
            print("similarity measure")
    
            for i in range(len(lcodes)):
                for j in range(i+1, len(lcodes)):
                    #mdist[i,j] += bin_hamming_distance(boss.codes[lcodes[i]], boss.codes[lcodes[j]])
                    #mdist[i,j] += euclidean_distance(boss.codes[lcodes[i]], boss.codes[lcodes[j]])
                    mdist[i,j] += cosine_similarity(boss.codes[lcodes[i]], boss.codes[lcodes[j]])
                    mdist[j, i] = mdist[i,j]
                    #mdist[i,j] += (boss_distance(boss.codes[lcodes[i]], boss.codes[lcodes[j]]) + boss_distance(boss.codes[lcodes[j]], boss.codes[lcodes[i]]))/2
                    #mdist[j, i] = mdist[i,j]
    
        lexer = sorted(list(boss.codes.keys()))
        print("spectral")
        mdist /= np.max(mdist)
        fdata = mdist
        imap = SpectralEmbedding(n_components=dimension, affinity='precomputed')
        fdata = imap.fit_transform(fdata)
    
        # fig = plt.figure(figsize=(10, 10))
        # # ax = fig.add_subplot(111, projection='3d')
        # ax = fig.add_subplot(111)
        #
        # # plt.scatter(fdata[:, 0], fdata[:, 1], zs=fdata[:, 2], depthshade=False, s=100)
        # plt.scatter(fdata[:, 0], fdata[:, 1], c=lcl)
        #
        # plt.show()
        print("clustering")
        dp = Dirichlet(n_components=10)
    
        dp.fit(fdata)
    
        lab = dp.predict(fdata)
        print(np.unique(lab))
        
        
        
        #fig = plt.figure(figsize=(10, 10))
        #ax = fig.add_subplot(111, projection='3d')
        #ax = fig.add_subplot(111)
        #plt.scatter(fdata[:, 0], fdata[:, 1], zs=fdata[:, 2], depthshade=False, s=100, c=lab/len(np.unique(lab)), cmap=plt.get_cmap('jet') )
        #plt.scatter(fdata[:, 0], fdata[:, 1], zs=fdata[:, 2], depthshade=False, s=100, c=lab, cmap=plt.get_cmap('jet') )
        #plt.scatter(fdata[:, 0], fdata[:, 1], c=lab, cmap=plt.get_cmap('jet'))
        #plt.colorbar()
        #plt.show()
        
        si='Silhouette=', silhouette_score(fdata, dp.predict(fdata))
        print('Silhouette=', silhouette_score(fdata, dp.predict(fdata)))
        

        lab2 = np.zeros((42))
        for app in range(1, len(lab)):               
            lab2[app]=lab[app]
    

        with open(filename, "a") as f:         
            writer = csv.writer(f)
            writer.writerow(lab2)
            writer.writerow(" ") 
        
        with open(filename, "a") as f:         
                writer = csv.writer(f)
                writer.writerow(si)
                
            

    # classes = {}
    # for i in np.unique(lab):
    #     classes[i] = []
    # for i, ex in  zip(lab, lexer):
    #     eid = ex.split('#')[1]
    #     classes[i].append((ex.split('#')[0], eid,  e.edict[int(eid)].lamb))
    #
    # for i in classes:
    #     print(sorted(classes[i]))