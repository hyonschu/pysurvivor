# pysurvivor
Simple survivor / retention analysis in python

TL;DR: You can take a spreadsheet or a dataframe that has a bunch of join and churn dates and do a periodic survival analysis

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

### What can I do with this?
