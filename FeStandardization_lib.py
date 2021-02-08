'''
Created on Feb 8, 2021

@author: haruka
'''
import os
import csv
import scipy.stats#標準化用
import numpy as np

class FeStandardization_lib():
    '''
    classdocs
    '''
    def __init__(self, bpath, apath):
        '''
        Constructor
        '''
        self.bpath = bpath
        self.apath = apath

    def getstanderd(self):
        csv_file=os.listdir(self.bpath)#標準化前のcsvが入っているフォルダのcsvファイル
        for index, val in enumerate(csv_file):
            if '.DS_Store' == val:
                continue
            print(val)

            with open(self.bpath+'/'+val) as f:#csv読み込み
                reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
                csv_data = [row for row in reader]

            #SciPyには平均0、分散1に正規化（標準化）するscipy.stats.zscore()関数がある。最小値0、最大値1に正規化する関数はない。
            #引数axis=Noneとすると全体に対して標準化。
            st_data = scipy.stats.zscore(csv_data,axis=None)
            #print(st_data)
            print('平均値', np.average(st_data))
            print('分散', np.var(st_data))

            #csv出力
            with open(self.apath+'/std_'+val, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(st_data)





