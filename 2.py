'''
Created on 2017/02/16

@author: 6516371656
'''
import pandas as pd
import numpy as np
from pandas import DataFrame
import datetime
from pylab import *
import matplotlib
import matplotlib.pyplot as plt

dat = pd.read_csv('ORDERCOL.csv')
dat['sales'] = dat['order_price'] * dat['purchase_amount']
dat.order_date = pd.to_datetime(dat.order_date)
dat_col = dat[dat.collaboration == 1]
dat_non_col = dat[dat.collaboration == 0]

#collaboration
# dat_clb_amount = dat.groupby('collaboration')['purchase_amount'].sum()
# dat_clb_sales = dat.groupby('collaboration')['sales'].sum()

#sex amount
# dat_sex_size = dat_non_col.groupby('sex')['purchase_amount'].sum()
#sex sales
# dat_sex_sales = dat_non_col.groupby('sex')['sales'].sum()

#age
# dat_age = dat_col.groupby('age').sum()

#date
# dat_col_date_amount = dat_non_col.groupby([dat_non_col['order_date'].dt.year, dat_non_col['order_date'].dt.month])['purchase_amount'].sum()
# dat_col_date_sales = dat_col.groupby([dat_col['order_date'].dt.year, dat_col['order_date'].dt.month])['sales'].sum()

#scolor
# dat_scolor = dat.groupby(['collaboration','class_cd'])['sales'].sum()
# dat_scolor = dat_scolor.sort_values(ascending=False)
# dat_scolor.to_csv('dat_scolor.csv')

#where
dat_add = dat.groupby(['collaboration','add'])['sales'].sum()
dat_add = dat_add.sort_values(ascending=False)
dat_add.to_csv('dat_add.csv')