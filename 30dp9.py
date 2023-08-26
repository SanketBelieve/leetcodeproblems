import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients = patients[patients["conditions"].str.contains(r"(^DIAB1)|( DIAB1)")]
    return patients