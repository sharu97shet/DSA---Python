import csv

from http import HTTPStatus

#https://getbootstrap.com/docs/4.3/components/forms/

def get_leads(csv_path:str)->list[str]:
    websites:list[str]=[]
    with open(csv_path, 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            websites.append(f'id:{row[0]}') 
            websites.append(f'FirstName:{row[1]}') 

        return websites 

print(get_leads('myapp_lead.csv'))       

# generator 

def gen_func(filename):
    with open(filename, 'r') as file:
        reader=csv.reader(file)
        for data in reader:
            yield data

results=gen_func('myapp_lead.csv')
print(results)

print(next(results))

# dataclasses

from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x:float
    y:float
    z:float=0.02

point = Point(1.0, 2.0,3.0)
print(point)     







