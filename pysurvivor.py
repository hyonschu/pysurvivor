# pysurvivor.py

import pandas as pd


class pysurvivor(object):
    '''
        awefjkhaesjk hfajkseh ajkhl jkh
    '''
    def __init__(self, dataframe, start_col, churn_col, freq='m'):
        self.lookup = {'W': '%Y-%W', 'm': '%Y-%m', 'Y': '%Y'}
        self.data = dataframe
        self.start_col = start_col
        self.churn_col = churn_col
        self.freq = freq
        self.data[start_col] = pd.to_datetime(self.data[start_col])
        self.data[churn_col] = pd.to_datetime(self.data[churn_col])
        self.data['join'] = self.data[start_col].apply(
            lambda x: x.strftime(self.lookup[freq]))
        self.data['churn'] = self.data[churn_col].apply(
            lambda x: x.strftime(self.lookup[freq]))
        self.totals = self.data.groupby('join').count()[self.data.columns[0]]
    #         how many people are left each month?
        self.survivors = (self.data.query('join!=churn').groupby(['join', 'churn']).count())[self.data.columns[0]]\
            .unstack().ffill(axis=1)
        self.survivors_pct = self.survivors.divide(self.totals)
    #         how many CUMULATIVE people CHURNED (have left) at each month?
        self.churn = (self.data.groupby(['join', 'churn']).count()[
                      self.data.columns[0]]).unstack()
        self.churn_pct = (self.data.groupby(['join', 'churn']).count()[
                          self.data.columns[0]]).divide(self.totals, axis=0).unstack()
