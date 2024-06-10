import pandas as pd
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # print(df1)
    # print(df2)
    df = pd.concat([df1,df2],ignore_index=True)
    # print(df)
    print(pd.concat([df1,df2],ignore_index=True))
df1 = pd.read_csv("2888. Reshape Data Concatenate.csv")
df2 = pd.read_csv("2888. Reshape Data Concatenate 2.csv")
df1 = pd.DataFrame(df1)
df2 = pd.DataFrame(df2)
concatenateTables(df1,df2)