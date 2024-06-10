
'''
select a.name as Employee
from Employee as a , Employee as b
where a.managerID = b.id and a.salary > b.salary;

select e2.name as "Employee" 
from Employee e1 
join employee e2 
on e1.id = e2.managerID
where e2.salary > e1.salary
'''
import pandas as pd

df = pd.DataFrame({
    'name': ['Employee1', 'Employee2', 'Employee3', 'Employee4'],
    'managerID': [2, 3, 1, 2],
    'salary': [50000, 60000, 45000, 55000]
})

result = df.loc[df['managerID'] == df['id']][['name', 'salary']]
result = result[result['salary'] > df.loc[df['managerID'] == df['id']]['salary']]
result = result.rename(columns={'name': 'Employee'})

print(result)

