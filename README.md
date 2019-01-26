# pysurvivor
Simple survivor / retention analysis in python

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
Creates a python object called analysis.

`analysis.survivors` generates a pandas.DataFrame that shows how many accounts remain active that up to that month

`analysis.survivors_pct` generates a pandas.DataFrame that shows how many accounts remain active that up to that month as a percentage

`analysis.churn` generates a pandas.DataFrame that shows how many accounts churned that month

`analysis.churn` generates a pandas.DataFrame that shows how many accounts churned that month as a percentages

