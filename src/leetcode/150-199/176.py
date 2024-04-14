import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    v = employee.salary.unique()
    v.sort()
    return pd.DataFrame([v[-2] if v.size >= 2 else None], columns=['SecondHighestSalary'])