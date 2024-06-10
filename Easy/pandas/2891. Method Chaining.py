import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(animals)
    df = df.sort_values(by=["weight"],ascending=False)
    df = df[df["weight"]>100]
    print(pd.DataFrame(df["name"]))

'''
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    heavy_animals = animals.loc[animals['weight']>100,:]
    sorted_animals = heavy_animals.sort_values(by='weight', ascending=False)

    return  sorted_animals.loc[:,['name']]

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.loc[animals['weight'] > 100].sort_values(by=['weight'],ascending=False).drop(columns=['species','age','weight'])
'''
animals={
    "name":["Tatiana","Khaled","Alex","Jonathan","Stefan"],
    "species":["Snake","Giraffe","Leopard","Monkey","Bear"],
    "age":[98,50,6,45,100],
    "weight":[464,41,328,463,50]
 }
findHeavyAnimals(animals)
