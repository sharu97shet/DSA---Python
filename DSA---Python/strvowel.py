str1='the quick brown fox jumps over the lazy dog'

vow=['a', 'e', 'i', 'o', 'u']

outstr=''


for i in range(len(str1)):
     #print(str1[i])
     if str1[i] is not str1[i].capitalize() and str1:
          print(str1[i].capitalize())


# for i in range(0,len(str1)):
#     for j in range(i+1, len(str1)):
#          if str1[i] not  in vow and str1[j] not  in vow :
#               outstr+=str1[i].capitalize()
#              # outstr=outstr+str1[i].capitalize()
#          else:
#                outstr+=str1[i]
                   
        

 


# for i in range(0,len(str1)):
#       if str1[i] not  in vow and str1[i]  in vow :
#               outstr=outstr+str1[i].capitalize()

print(outstr)                
    

def transform_string(input_str):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    transformed_str = ''
    for i in range(len(input_str)):
        if input_str[i].isalpha():
            if i < len(input_str) - 1 and input_str[i + 1].lower() in vowels:
                transformed_str += input_str[i].lower()
            else:
                transformed_str += input_str[i].upper()
        else:
            transformed_str += input_str[i]

    return transformed_str

# Example usage:  fatal: could not create work tree dir 'DjangoReact-RestApi': Permission denied
str1 = 'the quick brown fox jumps over the lazy dog'
transformed_str = transform_string(str1)
print(transformed_str)

        
