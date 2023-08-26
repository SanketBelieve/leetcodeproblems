import pandas as pd

def calculate_special_bonus(df: pd.DataFrame) -> pd.DataFrame:
    bns=(df['employee_id']%2) & (~df['name'].str.startswith('M'))
    df['bonus']=df['salary']*bns
    return df[['employee_id','bonus']].sort_values(by='employee_id')