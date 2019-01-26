# pysurvivor
Simple survivor / retention analysis in python

Take a spreadsheet or a dataframe that has a bunch of join and churn dates and do a periodic survival analysis.

Turn this:
```
joined	churned
12/28/17 23:15	1/28/18 23:15
4/13/18 7:57	5/13/18 7:57
3/22/18 14:01	8/22/18 16:01
3/10/18 7:55	4/10/18 6:55
10/11/17 1:18	11/11/17 1:18
12/14/17 17:03	1/14/18 17:03
1/8/18 8:28	2/8/18 8:28
12/25/17 0:36	8/25/18 2:35
6/18/17 19:46	7/25/17 19:46
```
Into this:

```                                 
                     CUSTOMERS STILL REMAINING
JOINED	2016-06	2016-07	2016-08	2016-09	2016-10	2016-11	2016-12	2017-01
2016-05	5	5	5	5	5	5	5	5
2016-06		9	9	9	9	1	1	1
2016-07			2	2	2	1	1	1
2016-08				2	1	1	1	1
2016-09					3	3	3	2
2016-10						4	4	4
2016-11							9	2
2016-12								3
```

And even this (with seaborn)
```
import matplotlib.pyplot as plt
plt.figure(figsize=(16,12))
mask = asdf.survivors_pct.isnull()
sns.heatmap(asdf.survivors_pct, mask=mask, cmap="Blues")
plt.title('Heatmap of Percentage of Customers Retained By Month', size=16)
plt.xlabel('Churn Month')
plt.ylabel('Joined Month')
```
![Image created with seaborn](https://github.com/hyonschu/pysurvivor/blob/master/retentionheatmap.png)



## How to use:
```
from pysurvivor import pysurvivor
analysis = pysurvivor(
         dataframe=df,         # pandas dataframe 
         start_col='joined',   # name of dataframe column with join/subscription start date
         churn_col='churned',  # name of df column with churn date      
         freq='m'              # strftime options ('Y' for %Y, 'm' for %Y-%m, 'W' for %Y-%W)
         # in english, that's 
         # Y for Year, 
         # m for Year-month,
         # W for Year-week
   )
```
Creates a python object called `analysis`. 

This object contains the following:

`analysis.survivors` 
generates a pandas.DataFrame that shows how many accounts remain active that up to that month

`analysis.survivors_pct` 
generates a pandas.DataFrame that shows how many accounts remain active that up to that month as a percentage

`analysis.churn` 
generates a pandas.DataFrame that shows how many accounts churned that month

`analysis.churn_pct` 
generates a pandas.DataFrame that shows how many accounts churned that month as a percentages

`analysis.data` 
generates the transformed data

`analysis.totals` 
returns the total new accounts by month

`analysis.freq` 
returns the frequency of churn analysis used
