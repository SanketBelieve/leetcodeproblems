import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sortedoff = employee['salary'].sort_values(ascending=False).drop_duplicates(keep='first')
    
    if N <= len(sortedoff):
        nth_highest_salary=sortedoff.iloc[N-1]
        return pd.DataFrame({'getNthHighestSalary': [nth_highest_salary]})
    else:   
   
        return pd.DataFrame({'getNthHighestSalary': [None]})