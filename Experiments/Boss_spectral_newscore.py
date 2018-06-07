
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


# colors = "rgbymcykrgbymcyk"


if __name__ == '__main__':
    
    filename = "basecos_stability_test.csv"
    e=15
    for w in range(0, e):  
    
        wlen = 125+w
        #wlen = randint(125,140)
        voclen = 4
        ncoefs = 3
        dimension=3
        
        #voclen = randint(2,8)
        #ncoefs = randint(2,8)
        #dimension=randint(2,4)
        
        print(w)
        
        data=[wlen, voclen, ncoefs, dimension]
        with open(filename, "a") as f:         
            writer = csv.writer(f)
            writer.writerow(data)
            writer.writerow(" ")
        
        
        x=5
        lol=[]
    
        for u in range(0, x):

            nseries = 42
            lcl = []
            mdist = np.zeros((nseries, nseries))

        
          #  print('primer print',len(e.edict))
            for f in [0,1,2,3,4,5]:
                dseries = {}
                for g in range(1,43):
                    num=g
                    nums='cvi'+str(num)
                    filen='/Users/maribelojeda/Desktop/MIT/I-WALKER/i-walker-Atia/terceranalisis/Straightpath/'+nums+ '.mat.csv'
                    reader = csv.reader(open(filen, "rb"), delimiter=",")
                    x = list(reader)
                    x.pop(0)
                   # print('primer print',nums)
                    result = np.array(x).astype("float") 
                    dseries[nums] = result[:, f]
        
                boss = Boss(dseries, 10, butfirst=True)
                boss.discretization_intervals(ncoefs, wlen, voclen)
                boss.discretize()
                lcodes = sorted(list(boss.codes.keys()))
                #print(len(lcodes))
                #print(len(dseries))

                bcode =boss.codes[lcodes[1]]
                        
                for i in range(len(lcodes)):
                    for j in range(i+1, len(lcodes)):
                        #mdist[i,j] += bin_hamming_distance(boss.codes[lcodes[i]], boss.codes[lcodes[j]])
                        #mdist[i,j] += euclidean_distance(boss.codes[lcodes[i]], boss.codes[lcodes[j]])
                        mdist[i,j] += cosine_similarity(boss.codes[lcodes[i]], boss.codes[lcodes[j]])
                        #mdist[j, i] = mdist[i,j]
                        #mdist[i,j] += (boss_distance(boss.codes[lcodes[i]], boss.codes[lcodes[j]]) + boss_distance(boss.codes[lcodes[j]], boss.codes[lcodes[i]]))/2
                        mdist[j, i] = mdist[i,j]
                        
            lexer = sorted(list(boss.codes.keys()))
        
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
        
            dp = Dirichlet(n_components=10)
        
            dp.fit(fdata)
        
            lab = dp.predict(fdata)
            
            
           # print('quinto print ',np.unique(lab))
        
          #-  fig = plt.figure(figsize=(10, 10))
           #- ax = fig.add_subplot(111, projection='3d')
            # ax = fig.add_subplot(111)
            
            #print(len(np.unique(lab)))
            
            counter=collections.Counter(lab)
            print(counter)
            maxvalue=counter.most_common(1)
            value=str(maxvalue).split(",")
            value2=value[1].split(")")
            value3=int(value2[0])
            array=[value3,wlen,voclen,ncoefs ]
            #print(value3)
            
            
            lol.append(lab)
            #print(lol)
        
        aran=np.zeros((len(lol),len(lol)))
        for r in range(0, len(lol)):
            for s in range(r+1, len(lol)):
                ran=int((adjusted_rand_score(lol[r],lol[s])*100))
                aran[r][s]=ran
                aran[s][r]=ran
                
        aran[aran==0]=np.nan
        print(aran)
        
        amean=[]
        for r in range(0, len(lol)):
            amean.append(np.nanmean(aran[r,0:len(lol)]))
            
        ar=np.array(aran)
        am= np.array(amean)    
        fp= np.vstack((ar,am)).T
        
        with open(filename, "a") as f:         
            writer = csv.writer(f)
            writer.writerows(fp)
            
   
        
    ''' 
        
        #with open("coeff.csv", "a") as f: 

     with open("10user.csv", "wb") as f:         
         writer = csv.writer(f)
         writer.writerows(dseries)
             
     with open("10matrix.csv", "wb") as f:         
         writer = csv.writer(f)
         writer.writerows(fdata)
             
     with open("10clust.csv", "wb") as f:         
         writer = csv.writer(f)
         writer.writerow(lab)
    '''
    
        
    
      #  for i in range(len(np.unique(lab))):
       #     print
    
       #- plt.scatter(fdata[:, 0], fdata[:, 1], zs=fdata[:, 2], depthshade=False, s=100, c=lab, cmap=plt.get_cmap('jet') )
       # plt.scatter(fdata[:, 0], fdata[:, 1], zs=fdata[:, 2], depthshade=False, s=100, c=lab/len(np.unique(lab)), cmap=plt.get_cmap('jet') )
        # plt.scatter(fdata[:, 0], fdata[:, 1], c=[colors[i] for i in lab])
       #- plt.colorbar()
       #- plt.show()
    
        # classes = {}
        # for i in np.unique(lab):
        #     classes[i] = []
        # for i, ex in  zip(lab, lexer):
        #     eid = ex.split('#')[1]
        #     classes[i].append((ex.split('#')[0], eid,  e.edict[int(eid)].lamb))
        #
        # for i in classes:
        #     print(sorted(classes[i]))