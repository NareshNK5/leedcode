import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data)
    df = df.rename(columns={0:"student_id",1:"age"})
    print(df[["student_id","age"]])

'''
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data,columns= ["student_id","age"])
'''

student_data=[[1, 15],[2, 11],[3, 11],[4, 20]]
createDataframe(student_data)
