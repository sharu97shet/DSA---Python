def binary(arr, target):
    left, right=0, len(arr)-1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return -1


a=[10,20,30,40,50]
tar=40 

res=(binary(a,tar))
print(res)


user={
    'id':1,
    'name':'shaun',
    'email':'shaun@gmail.com',
    'skill':{
        'frontend':'ReactJs',
        'Backend':'Python'
    }
}
print(user.items())

def nesteddict(user, parent_key=''):
    for k,v in user.items():
         if type(v)==dict:
             nesteddict(v,k+'#')
         else:
             print(f"{parent_key+k}:{v}")
             
nesteddict(user)


objdata={
  "data": "key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47, key=0Sr4C, age=68, key=CGEqo, age=76, key=IxKVQ, age=79, key=eD221, age=29, key=XZbHV, age=32"
}

print(type(objdata))

pairs = objdata["data"].split(", ")
print(pairs)

details={}
counts=0

for item in pairs:
    key,age=item.split('=')
    print(key,age)
    if key.strip()=='age' and int(age)>=40:
        # print(key,age)
        counts+=1

print(counts)

person={
    'name':"anil",

}



    
# for i in objdata:
#     print(objdata[i])