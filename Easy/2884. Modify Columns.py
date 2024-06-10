import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    print(employees)
    employees["salary"] = employees["salary"]*2
    print(employees)

employees = pd.read_csv("2884. Modify Columns.csv")
employees = pd.DataFrame(employees)
modifySalaryColumn(employees)


'''
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(salary=2 * employees['salary'])
'''