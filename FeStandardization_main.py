'''
Created on Feb 8, 2021

@author: haruka
'''
#Cfeデータを標準化する

import FeStandardization_lib as mdl

beforepath = './feData'#標準化前csvフォルダ
afterpath = './feData_stand'#標準化後csvフォルダ

fmdl = mdl.FeStandardization_lib(beforepath, afterpath)
fmdl.getstanderd()#標準化

