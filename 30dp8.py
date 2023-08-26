import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users=users[users['mail'].str.match(r'^[a-zA-Z][\w\.-]*@leetcode\.com')]
    return users