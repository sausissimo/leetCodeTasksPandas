import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    print(employees.head(3))    

employees = pd.DataFrame([[1,15],[2,11],[3,11],[4,20]], columns = ["student_id", "age"])

selectFirstRows(employees)
