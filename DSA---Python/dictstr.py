fruits={
    'name':"apple",
    'color':"red",
    'rate':200
}
name="sharath"

#print(name[-1:2])


# p='pythonrogramming'

p='PythonProgaMmiNG'

# selc
# where<(select from )

# address column    ''

# select *  from emp where address in 'delhi'

# 100/2 half records

# frappe   

# select * from emp order by id limit 50 

# // git  5 files 3 add git reset   h1 to h6  


# ist loop p in countword no then else 1 
countword={}

for i in p.lower():
    if i in countword:
        countword[i]=countword[i]+1
    else:
        countword[i]=1   
 

print(countword)








rep=''

store=[]

for i in range(len(p)):
    print(i, "itr")

    if p[i] in p[1:]:
        rep=p[i]
        break
        
        

print(store)
    # for j in range(1,len(p)):
    #     if p[i] == p[j]:
    #         rep=p[j]
    #         break

print(rep)   

