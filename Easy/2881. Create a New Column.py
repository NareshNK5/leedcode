import pandas as pd
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    print(employees)
    employees["bonus"] = employees["salary"]*2
    print(employees)
    
employees = pd.read_csv("2881. Create a New Column.csv")
employees = pd.DataFrame(employees)
createBonusColumn(employees)

'''
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(bonus = lambda df: 2 * df['salary'])
'''