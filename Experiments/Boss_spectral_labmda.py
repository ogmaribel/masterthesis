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
    
    e=1
    for w in range(0, e):
        '''   
        wlen = randint(125,135)
        voclen = randint(2,7)
        ncoefs = randint(2,7)
        '''
        wlen = 126
        voclen = 7
        ncoefs = 7
        
        data=[wlen, voclen, ncoefs]
        with open("ranscore_l0.csv", "a") as f:         
            writer = csv.writer(f)
            writer.writerow(data)
            writer.writerow(" ")
        
        
        x=10
        lol=[]
    
        for u in range(0, x):
            
            p = Pacientes()
            e = Exercises()
        
            p.from_db(pilot='NOGALES')
            e.from_db(pilot='NOGALES')
        
            e.delete_exercises([1425638547])
            e.delete_exercises([1425638507])
            e.delete_exercises([1425638379])
            e.delete_exercises([1425638343])
            e.delete_exercises([1425637677])
            e.delete_exercises([1425637642])
            e.delete_exercises([1425637526])
            e.delete_exercises([1425637492])
            e.delete_exercises([1425637369])
            e.delete_exercises([1425637335])
            e.delete_exercises([1425577862])
            e.delete_exercises([1425577789])
            e.delete_exercises([1425575356])
            e.delete_exercises([1425575304])
            e.delete_exercises([1425573938])
            e.delete_exercises([1425573906])
            e.delete_exercises([1425573789])
            e.delete_exercises([1425573757])
            e.delete_exercises([1425573640])
            e.delete_exercises([1425573606])
            e.delete_exercises([1425573062])
            e.delete_exercises([1425572965])
            e.delete_exercises([1425572937])
            e.delete_exercises([1425572838])
            e.delete_exercises([1425572808])
            e.delete_exercises([1425572405])
            e.delete_exercises([1425572379])
            e.delete_exercises([1425572256])
            e.delete_exercises([1425572167])
            e.delete_exercises([1425572139])
            e.delete_exercises([1425571770])
            e.delete_exercises([1425571619])
            e.delete_exercises([1425571572])
            e.delete_exercises([1425571388])
            e.delete_exercises([1425571342])
            e.delete_exercises([1425556214])
            e.delete_exercises([1425556120])
            e.delete_exercises([1425556093])
            e.delete_exercises([1425556002])
            e.delete_exercises([1425555975])
            e.delete_exercises([1425555680])
            e.delete_exercises([1425555625])
            e.delete_exercises([1425555472])
            e.delete_exercises([1425555422])
            e.delete_exercises([1425555295])
            e.delete_exercises([1425555253])
            e.delete_exercises([1425552422])
            e.delete_exercises([1425552395])
            e.delete_exercises([1425552313])
            e.delete_exercises([1425552290])
            e.delete_exercises([1425552206])
            e.delete_exercises([1425552180])
            e.delete_exercises([1425551673])
            e.delete_exercises([1425551640])
            e.delete_exercises([1425551539])
            e.delete_exercises([1425551509])
            e.delete_exercises([1425551398])
            e.delete_exercises([1425551366])
            e.delete_exercises([1425550599])
            e.delete_exercises([1425550565])
            e.delete_exercises([1425550466])
            e.delete_exercises([1425550435])
            e.delete_exercises([1425550336])
            e.delete_exercises([1425550302])
            e.delete_exercises([1425489865])
            e.delete_exercises([1425489839])
            e.delete_exercises([1425489722])
            e.delete_exercises([1425488298])
            e.delete_exercises([1425488261])
            e.delete_exercises([1425488088])
            e.delete_exercises([1425487960])
            e.delete_exercises([1425487921])
            e.delete_exercises([1425487395])
            e.delete_exercises([1425487360])
            e.delete_exercises([1425487231])
            e.delete_exercises([1425487192])
            e.delete_exercises([1425487055])
            e.delete_exercises([1425487015])
            e.delete_exercises([1425486298])
            e.delete_exercises([1425486172])
            e.delete_exercises([1425486082])
            e.delete_exercises([1425486057])
            e.delete_exercises([1425485751])
            e.delete_exercises([1425485718])
            e.delete_exercises([1425485606])
            e.delete_exercises([1425485574])
            e.delete_exercises([1425485470])
            e.delete_exercises([1425485439])
            e.delete_exercises([1425485088])
            e.delete_exercises([1425485036])
            e.delete_exercises([1425484925])
            e.delete_exercises([1425484893])
            e.delete_exercises([1425484760])
            e.delete_exercises([1425484713])
            e.delete_exercises([1425469774])
            e.delete_exercises([1425469739])
            e.delete_exercises([1425469633])
            e.delete_exercises([1425469604])
            e.delete_exercises([1425468771])
            e.delete_exercises([1425468736])
            e.delete_exercises([1425468617])
            e.delete_exercises([1425468583])
            e.delete_exercises([1425468456])
            e.delete_exercises([1425468412])
            e.delete_exercises([1425466823])
            e.delete_exercises([1425466786])
            e.delete_exercises([1425466659])
            e.delete_exercises([1425466626])
            e.delete_exercises([1425466501])
            e.delete_exercises([1425466469])
            e.delete_exercises([1425465011])
            e.delete_exercises([1425464983])
            e.delete_exercises([1425464875])
            e.delete_exercises([1425464846])
            e.delete_exercises([1425464735])
            e.delete_exercises([1425464710])
            e.delete_exercises([1425463876])
            e.delete_exercises([1425463840])
            e.delete_exercises([1425463727])
            e.delete_exercises([1425463695])
            e.delete_exercises([1425463590])
            e.delete_exercises([1425463551])
            e.delete_exercises([1425462983])
            e.delete_exercises([1425462954])
            e.delete_exercises([1425462848])
            e.delete_exercises([1425462818])
            e.delete_exercises([1425462708])
            e.delete_exercises([1425462677])
            e.delete_exercises([1425403967])
            e.delete_exercises([1425403917])
            e.delete_exercises([1425403721])
            e.delete_exercises([1425403665])
            e.delete_exercises([1425403456])
            e.delete_exercises([1425403399])
            e.delete_exercises([1425402904])
            e.delete_exercises([1425402868])
            e.delete_exercises([1425402751])
            e.delete_exercises([1425402716])
            e.delete_exercises([1425402601])
            e.delete_exercises([1425402566])
            e.delete_exercises([1425401783])
            e.delete_exercises([1425401757])
            e.delete_exercises([1425401655])
            e.delete_exercises([1425401630])
            e.delete_exercises([1425401535])
            e.delete_exercises([1425401508])
            e.delete_exercises([1425400336])
            e.delete_exercises([1425400313])
            e.delete_exercises([1425400187])
            e.delete_exercises([1425400164])
            e.delete_exercises([1425400072])
            e.delete_exercises([1425400046])
            e.delete_exercises([1425399709])
            e.delete_exercises([1425399623])
            e.delete_exercises([1425399598])
            e.delete_exercises([1425399514])
            e.delete_exercises([1425399489])
            e.delete_exercises([1425382666])
            e.delete_exercises([1425382621])
            e.delete_exercises([1425382475])
            e.delete_exercises([1425382439])
            e.delete_exercises([1425382286])
            e.delete_exercises([1425382251])
            e.delete_exercises([1425380544])
            e.delete_exercises([1425380508])
            e.delete_exercises([1425380353])
            e.delete_exercises([1425380315])
            e.delete_exercises([1425380116])
            e.delete_exercises([1425380081])
            e.delete_exercises([1425379596])
            e.delete_exercises([1425379568])
            e.delete_exercises([1425379463])
            e.delete_exercises([1425379436])
            e.delete_exercises([1425379334])
            e.delete_exercises([1425379305])
            e.delete_exercises([1425378746])
            e.delete_exercises([1425378713])
            e.delete_exercises([1425378591])
            e.delete_exercises([1425378555])
            e.delete_exercises([1425378431])
            e.delete_exercises([1425378397])
            e.delete_exercises([1425378008])
            e.delete_exercises([1425377965])
            e.delete_exercises([1425377826])
            e.delete_exercises([1425377784])
            e.delete_exercises([1425377636])
            e.delete_exercises([1425377598])
            e.delete_exercises([1425376999])
            e.delete_exercises([1425376956])
            e.delete_exercises([1425376849])
            e.delete_exercises([1425376805])
            e.delete_exercises([1425376682])
            e.delete_exercises([1425376650])
            e.delete_exercises([1425375989])
            e.delete_exercises([1425375955])
            e.delete_exercises([1425375821])
            e.delete_exercises([1425375787])
            e.delete_exercises([1425375638])
            e.delete_exercises([1425375604])
            e.delete_exercises([1425375135])
            e.delete_exercises([1425375111])
            e.delete_exercises([1425375024])
            e.delete_exercises([1425374996])
            e.delete_exercises([1425374877])
            e.delete_exercises([1425318036])
            e.delete_exercises([1425317995])
            e.delete_exercises([1425316795])
            e.delete_exercises([1425316755])
            e.delete_exercises([1425316640])
            e.delete_exercises([1425316553])
            e.delete_exercises([1425316524])
            e.delete_exercises([1425316255])
            e.delete_exercises([1425316223])
            e.delete_exercises([1425316096])
            e.delete_exercises([1425316066])
            e.delete_exercises([1425315932])
            e.delete_exercises([1425315885])
            e.delete_exercises([1425314183])
            e.delete_exercises([1425314147])
            e.delete_exercises([1425313987])
            e.delete_exercises([1425313947])
            e.delete_exercises([1425313782])
            e.delete_exercises([1425313744])
            e.delete_exercises([1425313339])
            e.delete_exercises([1425313307])
            e.delete_exercises([1425313182])
            e.delete_exercises([1425313145])
            e.delete_exercises([1425313031])
            e.delete_exercises([1425312998])
            e.delete_exercises([1425311963])
            e.delete_exercises([1425311928])
            e.delete_exercises([1425311807])
            e.delete_exercises([1425311774])
            e.delete_exercises([1425311648])
            e.delete_exercises([1425311612])
            e.delete_exercises([1425295841])
            e.delete_exercises([1425295807])
            e.delete_exercises([1425295677])
            e.delete_exercises([1425295639])
            e.delete_exercises([1425295500])
            e.delete_exercises([1425295463])
            e.delete_exercises([1425294795])
            e.delete_exercises([1425294764])
            e.delete_exercises([1425294072])
            e.delete_exercises([1425294041])
            e.delete_exercises([1425293934])
            e.delete_exercises([1425293906])
            e.delete_exercises([1425293784])
            e.delete_exercises([1425293756])
            e.delete_exercises([1425292872])
            e.delete_exercises([1425292823])
            e.delete_exercises([1425292617])
            e.delete_exercises([1425292567])
            e.delete_exercises([1425292358])
            e.delete_exercises([1425292307])
            e.delete_exercises([1425291688])
            e.delete_exercises([1425291548])
            e.delete_exercises([1425291448])
            e.delete_exercises([1425291415])
            e.delete_exercises([1425289297])
            e.delete_exercises([1425289270])
            e.delete_exercises([1425289167])
            e.delete_exercises([1425289141])
            e.delete_exercises([1425289038])
            e.delete_exercises([1425289012])
            e.delete_exercises([1425038069])
            e.delete_exercises([1425037901])
            e.delete_exercises([1425037869])
            e.delete_exercises([1425037761])
            e.delete_exercises([1425037731])
            e.delete_exercises([1425034634])
            e.delete_exercises([1425034597])
            e.delete_exercises([1425034425])
            e.delete_exercises([1425034396])
            e.delete_exercises([1425034283])
            e.delete_exercises([1425034256])
            e.delete_exercises([1424973356])
            e.delete_exercises([1424973293])
            e.delete_exercises([1424971902])
            e.delete_exercises([1424971864])
            e.delete_exercises([1424971721])
            e.delete_exercises([1424971680])
            e.delete_exercises([1424971539])
            e.delete_exercises([1424971499])
            e.delete_exercises([1424970891])
            e.delete_exercises([1424970788])
            e.delete_exercises([1424970755])
            e.delete_exercises([1424970589])
            e.delete_exercises([1424970561])
            e.delete_exercises([1424970530])
            e.delete_exercises([1424969549])
            e.delete_exercises([1424969514])
            e.delete_exercises([1424969366])
            e.delete_exercises([1424969332])
            e.delete_exercises([1424969188])
            e.delete_exercises([1424969149])
            e.delete_exercises([1424968545])
            e.delete_exercises([1424968494])
            e.delete_exercises([1424968327])
            e.delete_exercises([1424968277])
            e.delete_exercises([1424968105])
            e.delete_exercises([1424968035])
            e.delete_exercises([1424967358])
            e.delete_exercises([1424967327])
            e.delete_exercises([1424967210])
            e.delete_exercises([1424967168])
            e.delete_exercises([1424967037])
            e.delete_exercises([1424967002])
            e.delete_exercises([1424966587])
            e.delete_exercises([1424966454])
            e.delete_exercises([1424966354])
            e.delete_exercises([1424966324])
            e.delete_exercises([1424965896])
            e.delete_exercises([1424965791])
            e.delete_exercises([1424965752])
            e.delete_exercises([1424965647])
            e.delete_exercises([1424965616])
            e.delete_exercises([1424965136])
            e.delete_exercises([1424965038])
            e.delete_exercises([1424965013])
            e.delete_exercises([1424964902])
            e.delete_exercises([1424964878])
            e.delete_exercises([1424947916])
            e.delete_exercises([1424947673])
            
            #create random variables
            
            
            #wlen = 132
            #voclen = 2
            #ncoefs = 5
            
    
            
            nseries = 0
            lcl = []
        
          #  print('primer print',len(e.edict))
            for ex in e.iterator():
                t = Trajectory(ex.get_coordinates())
                if t.straightness()[0] < 0.95:
                    e.delete_exercises([ex.id])
           # print('segundo print ',len(e.edict))
        
            for ex in e.iterator():
                forces = ex.get_forces()
                if forces.shape[0] > wlen:
                    nseries += 1
                    if 'FSL' in ex.uid:
                        lcl.append('r')
                    else:
                        lcl.append('g')
                else:
                    e.delete_exercises([ex.id])
          #  print('tercer print ',len(e.edict))
        
            mdist = np.zeros((nseries, nseries))
            print('cuarto print ',nseries)
        
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
            imap = SpectralEmbedding(n_components=3, affinity='precomputed')
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
            
            print(len(np.unique(lab)))
            
            counter=collections.Counter(lab)
            print(counter)
            maxvalue=counter.most_common(1)
            value=str(maxvalue).split(",")
            value2=value[1].split(")")
            value3=int(value2[0])
            array=[value3,wlen,voclen,ncoefs ]
            print(value3)
            
            lol.append(lab)
            print(lol)
        
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
        
        with open("ranscore_l0.csv", "a") as f:         
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