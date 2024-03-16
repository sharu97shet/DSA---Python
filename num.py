print("anv")

from collections import Counter

def recursive_dict_keys(dictionary):
    for key, value in dictionary.items():
        print(key)
        if isinstance(value, dict):
            recursive_dict_keys(value)

# Example usage:
nested_dict = {
    'key1': 'value1',
    'key2': {
        'key3': 'value3',
        'key4': {
            'key5': 'value5',
            'key6': 'value6'
        }
    },
    'key7': 'value7'
}

recursive_dict_keys(nested_dict)

ar=[1,2,3,5]
tu=[2,4,6]
ar.append(tu)

print(ar[4][0])


dictems={'name':"abc",
         'email':"@gmail",
          "author": {
        "lastname": "Doe",
        "firstname": "Jane"
    }}

parent_key=''
sep='#'

print(dictems.items())

for k, v in dictems.items():

 new_key = f"{parent_key}{sep}{k}" if parent_key else k

 print(new_key)


 import re

data_string = '{"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}'

# Extracting age values using regular expression
ages = [int(match.group(1)) for match in re.finditer(r'age=(\d+)', data_string)]

# Counting age values greater than 50
count_greater_than_50 = sum(age > 50 for age in ages)

print("Number of age values greater than 50:", count_greater_than_50)


 

# n = int(input("Enter the number of participants: "))

# # Get the scores as a space-separated string and convert it to a list of integers
# scores = list(map(int, input("Enter the scores separated by space: ").split()))

# print(scores)


# lst=[]

# for i in range((3)):
#    name=input()
#    score=float(input())
#    lst.append([name,score])


#    print(lst)   
#    lst=[]

# for i in range(int(input('enter no of students'))):
#    name=(input(''))
#    score=float(input(''))
#    lst.append([name,score])
   

#print(lst) 

# scores=[x[1]  for x in lst]
# print(scores)

# sortedscore=sorted(set(scores))
# print(sortedscore)
# print(lst) 

# names=[s[0] for s in lst if( sortedscore[1]==s[1])]
# print(names)

  # hire pro linked in  , skaad it solutions , LG  , akash  , map 



# import os

# file_name="example.txt"

# with open(file_name ,"w")  as file:
#     file.write("new file created and deleted")

# f=open(file_name,"r")
# print(f.read())

# os.remove(file_name)

# with open(file_name, 'r') as file:
#     file.write("Hello, this is a sample file.")

# delete an file in python

# cube of map elements


num=[0,1,1,2,3]

cubes=list(map(lambda a:a*a*a, num))

print(cubes)


def fun():
   x=100
   print(x)

#x+=1
fun()


def  pair_sum(arr, target):
   pair=[]
   for i in range(0, len(arr)):
      for j in range(i+1, len(arr)):
         if arr[i]+arr[j]==target:
            pair.append((arr[i],arr[j]))
   return pair 

mark=[2, 3 , 5 , 6 ,8 ,3,8 ,4 ,12]
print(pair_sum(mark, 10)) 


#how to find  missing no from list

nums=[2,4,5,6,7,9]
miss=[]

for i in range(1,len(nums)):
   if i not in nums:
      miss.append(i)

print(miss)

      
   






         