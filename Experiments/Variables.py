#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:07:34 2017

@author: maribelojeda
"""

class Variables():
    

    # The class "constructor" - It's actually an initializer 
    def __init__(self, twlen, tvoclen, tncoefs, tclusts):
        self.wlen = twlen
        self.voclen = tvoclen
        self.ncoefs = tncoefs
        self.clusts = tclusts

    def return_variables(self):
        variables = Variables(self.twlen, self.tvoclen, self.tncoefs, self.tclusts)
        return variables
    
    def set_clusts(self,tclusts):
        self.clusts = tclusts
    

    