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


# colors = "rgbymcykrgbymcyk"


if __name__ == '__main__':
                    
    #create random variables
    
    
    wlen = 127
    voclen = 7
    ncoefs = 7
    
    dimension=4
    clustn=10
    ctype=159
    
    nseries = 0
    lcl = []

    mdist = np.zeros((nseries, nseries))

    for f in range(6):
        dseries = {}
        for ex in e.iterator():
            forces = ex.get_forces()
            if forces.shape[0] > wlen:
                dseries[str(ex.uid) + '#' + str(ex.id)] = forces[:, f]

        boss = Boss(dseries, 10, butfirst=True)
        boss.discretization_intervals(ncoefs, wlen, voclen)
        boss.discretize()
        lcodes = list(boss.codes.keys())
        sorted(lcodes)
        for i in range(len(lcodes)):
            for j in range(i+1, len(lcodes)):
                # mdist[i,j] += bin_hamming_distance(boss.codes[lcodes[i]], boss.codes[lcodes[j]])
                # mdist[i,j] += euclidean_distance(boss.codes[lcodes[i]], boss.codes[lcodes[j]])
                mdist[i,j] += cosine_similarity(boss.codes[lcodes[i]], boss.codes[lcodes[j]])
                mdist[j, i] = mdist[i,j]
                # mdist[i,j] += (boss_distance(boss.codes[v1], boss.codes[v2]) + boss_distance(boss.codes[v2], boss.codes[v1]))/2

    lexer = list(boss.codes.keys())

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

    dp = Dirichlet(n_components=clustn)

    dp.fit(fdata)

    lab = dp.predict(fdata)
   # print('quinto print ',np.unique(lab))

    #-fig = plt.figure(figsize=(10, 10))
    #-ax = fig.add_subplot(111, projection='3d')
    # ax = fig.add_subplot(111)
    
    print(len(np.unique(lab)))
    
    counter=collections.Counter(lab)
    print(counter)
    maxvalue=counter.most_common(1)
    value=str(maxvalue).split(",")
    value2=value[1].split(")")
    value3=int(value2[0])
    array=[value3,wlen,voclen,ncoefs ]
    print(value3)
    lab2= np.array(lab)
    lab3=np.reshape(lab2,(1,len(lab2)))       

#with open("coeff.csv", "a") as f: 
    
    data=[wlen, voclen, ncoefs]
    
    '''       
    #PARA IMPRIMIR ARRAYS EN ARCHIVOS INDIVIDUALES 
    with open("25user.csv", "w") as f:         
         writer = csv.writer(f)
         writer.writerows(dseries)        
    
    with open("25matrix.csv", "w") as f:         
         writer = csv.writer(f)
         writer.writerows(fdata)
         
    with open("25clust.csv", "w") as f:         
         writer = csv.writer(f)
         writer.writerow(lab)
         
        '''
        
    
    #Para transformar info a data frame
    lcn=[]
    lcs=[]
    
    for i in range(len(lcodes)):
        sp=lcodes[i].split('S')
        s2=sp[1].split('#')
        lcn.append(s2[0])
        lcs.append(s2[1])
        
    awlen=[]
    avoclen=[]
    ancoefs=[]
    adimension=[]
    aclustn=[]
    actype=[]
    for i in range(len(lcodes)):
        awlen.append(wlen)
        avoclen.append(voclen)
        ancoefs.append(ncoefs)
        adimension.append(dimension)
        aclustn.append(clustn)
        actype.append(ctype)
    
    lab2=lab.tolist()
 
    
    df = pd.DataFrame.from_dict([lcn, lcs, lab2, actype, awlen, avoclen, ancoefs, adimension, aclustn])
    df=df.T
    #with open('test.csv', 'a') as f:      
    #    df.to_csv(f, header=False)
    
    
    
    '''
    #Recuperar las fuerzas
    getforces1 = {}
    getforces2 = {}
    getforces3 = {}
    getforces4 = {}
    getforces5 = {}
    getforces6 = {}
    
    getforces1S = {}
    getforces2S = {}
    getforces3S = {}
    getforces4S = {}
    getforces5S = {}
    getforces6S = {}
    
    for ex in e.iterator():
        getforces1[str(ex.id)]= np.mean(ex.get_forces()[:,0])
        getforces2[str(ex.id)]= np.mean(ex.get_forces()[:,1])
        getforces3[str(ex.id)]= np.mean(ex.get_forces()[:,2])
        getforces4[str(ex.id)]= np.mean(ex.get_forces()[:,3])
        getforces5[str(ex.id)]= np.mean(ex.get_forces()[:,4])
        getforces6[str(ex.id)]= np.mean(ex.get_forces()[:,5])
        
        getforces1S[str(ex.id)]= np.sum(ex.get_forces()[:,0])
        getforces2S[str(ex.id)]= np.sum(ex.get_forces()[:,1])
        getforces3S[str(ex.id)]= np.sum(ex.get_forces()[:,2])
        getforces4S[str(ex.id)]= np.sum(ex.get_forces()[:,3])
        getforces5S[str(ex.id)]= np.sum(ex.get_forces()[:,4])
        getforces6S[str(ex.id)]= np.sum(ex.get_forces()[:,5])
        
    getforces1SD = {}
    getforces2SD = {}
    getforces3SD = {}
    getforces4SD = {}
    getforces5SD = {}
    getforces6SD = {}
    
    for ex in e.iterator():
        getforces1SD[str(ex.id)]= np.std(ex.get_forces()[:,0])
        getforces2SD[str(ex.id)]= np.std(ex.get_forces()[:,1])
        getforces3SD[str(ex.id)]= np.std(ex.get_forces()[:,2])
        getforces4SD[str(ex.id)]= np.std(ex.get_forces()[:,3])
        getforces5SD[str(ex.id)]= np.std(ex.get_forces()[:,4])
        getforces6SD[str(ex.id)]= np.std(ex.get_forces()[:,5])
    
   
    
    '''
    getforces1L = {}
    getforces2L = {}
    getforces3L = {}
    getforces4L = {}
    getforces5L = {}
    getforces6L = {}
    
    for ex in e.iterator():
        getforces1L[str(ex.id)]= np.shape(ex.get_forces()[:,0])
        getforces2L[str(ex.id)]= np.shape(ex.get_forces()[:,1])
        getforces3L[str(ex.id)]= np.shape(ex.get_forces()[:,2])
        getforces4L[str(ex.id)]= np.shape(ex.get_forces()[:,3])
        getforces5L[str(ex.id)]= np.shape(ex.get_forces()[:,4])
        getforces6L[str(ex.id)]= np.shape(ex.get_forces()[:,5])
    
    
    '''
    with open("forces.csv", "w") as f:         
         writer = csv.writer(f)
         for key, value in getforces1.iteritems():
             writer.writerow([key] + [value])
    '''         
 


  #  for i in range(len(np.unique(lab))):
   #     print

    #-plt.scatter(fdata[:, 0], fdata[:, 1], zs=fdata[:, 2], depthshade=False, s=100, c=lab, cmap=plt.get_cmap('jet') )
    #plt.scatter(fdata[:, 0], fdata[:, 1], zs=fdata[:, 2], depthshade=False, s=100, c=lab/len(np.unique(lab)), cmap=plt.get_cmap('jet') )
# plt.scatter(fdata[:, 0], fdata[:, 1], c=[colors[i] for i in lab])
    #-plt.colorbar()
    #-plt.show()

# classes = {}
# for i in np.unique(lab):
#     classes[i] = []
# for i, ex in  zip(lab, lexer):
#     eid = ex.split('#')[1]
#     classes[i].append((ex.split('#')[0], eid,  e.edict[int(eid)].lamb))
#
# for i in classes:
#     print(sorted(classes[i]))
