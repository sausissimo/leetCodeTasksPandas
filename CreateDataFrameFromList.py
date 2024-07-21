import pandas as pd

def createDataFrame(studentData: list[list[int]]):
    print(pd.DataFrame(studentData, columns = ["student_id", "age"]))

studentData = [[1,15],[2,11],[3,11],[4,20]]

createDataFrame(studentData)
