#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 07:00:17 2019

@author: konstantinos.falangi
"""
import numpy as np
import pandas as pd

    
#initialise the fee structure
term12 = [50, 90, 90, 115, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
term24 = [70, 100, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600, 640, 680, 720, 760, 800]

#@app.route("/")
def feecalculator(term, amount=2750):
    """Calculate fee amount based on given rules """
    
    #test the term provided
    if term not in (12, 24):
        return('Term should be either 12 or 24 months')
        
    #test the amount provided
    if amount < 1000 or amount > 20000:
        return('Amount should be between £1,000 and £20,000')
    
    #create series of amounts
    amt = list(range(1000, 20001, 1000))
    
    #create a series with the fee and the respective amount
    if term == 12:
        s = pd.Series(term12, index = amt)
    else:
        s = pd.Series(term24, index = amt)
       
    #if amount provided not in the df then create new series
    if amount not in s.index:
        s.loc[amount] = np.nan
        
    #sort the updated series and apply interpolation if missing values
    s = s.sort_index()
    s = s.interpolate(method='index')
    fee = s[s.index == amount]
    
    #make sure that fee is rounded to be an exact multiple of 5
    if int(fee) % 5 == 0:
        return(int(fee))
    else:
        return(int(fee) - int(fee) % 5)
    
feecalculator(24, 1000)
#feecalculator(24, 2000)
#feecalculator(24, 3000)
#feecalculator(24, 20000)
#feecalculator(24, 19198)
#
#feecalculator(12, 1000)
#feecalculator(12, 3000)
#feecalculator(12, 20000)
#feecalculator(12, 19198)
