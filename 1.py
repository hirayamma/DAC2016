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
#
dat_col = pd.read_csv('item_new.csv')
dat_order = pd.read_csv('ORDER.csv')
dat_order_det = pd.read_csv('ORDERDETAIL.csv')
dat_member = pd.read_csv('MEMBER.csv')
 
  
dat = pd.merge(dat_order, dat_order_det,on='order_ID')
dat = pd.merge(dat, dat_member,on='customer_ID')
dat = pd.merge(dat, dat_col, left_on=['item_ID', 'item_det_ID'], right_on=['jan_cd', 'sjan_cd'])
  
dat.to_csv('ORDERCOL.csv')
# dat_line = dat.groupby('brand_cd')
# dat_line_size = dat_line.size()
# dat_line_size = dat_line_size.sort_values(ascending=False)
# dat_line_size.to_csv('brand_cd_size.csv')
# 
# dat.datetime = dat.datetime.astype("datetime64")
# 
# dat.groupby([dat['datetime'].dt.year, dat['datetime'].dt.month]).size().plot(kind="bar")
# plt.show()
