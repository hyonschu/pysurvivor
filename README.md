# pysurvivor
Simple survivor / retention analysis in python

## How to use:
```
from pysurvivor import pysurvivor
analysis = pysurvivor(
         dataframe=df,         # pandas dataframe 
         start_col='joined',   # name of dataframe column with join/subscription start date
         churn_col='churned',  # name of df column with churn date      
         freq='M'              # strftime options ('Y' for %Y, 'm' for %Y-%m, 'W' for %Y-%W)
   )
```
