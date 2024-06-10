import pandas as pd
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # print(employees)
    print(employees.head(3))
employees = pd.read_csv("2879. Display the First Three Rows.csv")
employees = pd.DataFrame(employees)
selectFirstRows(employees)