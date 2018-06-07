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
    
    
    wlen = 135
    voclen = 7
    ncoefs = 2
    
    dimension=3
    clustn=10
    ctype=159
    
    nseries = 42
    lcl = []



    mdist = np.zeros((nseries, nseries))
    forces=np.zeros((nseries, 6))
     
            
    for f in [0,1,2,3,4,5]:
        for g in range(1,43):
            num=g
            nums='cvi'+str(num)
            filen='/Users/maribelojeda/Desktop/MIT/I-WALKER/i-walker-Atia/terceranalisis/Straightpath/'+nums+ '.mat.csv'
            reader = csv.reader(open(filen, "rb"), delimiter=",")
            x = list(reader)
            x.pop(0)
            result = np.array(x).astype("float") 
            avforce = np.mean(result[:, f])
            forces[g-1][f]= avforce
