import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    
    # Sort the DataFrame by 'user_id' and reset the index
    users = users.sort_values(by='user_id').reset_index(drop=True)
    
    return users