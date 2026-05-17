# i = 1
# fact  = 1
# factNum = 3
# while(i <= factNum):
#     fact = fact * i ,     # fact *=i
#     i = i+1
# print("output :  ", fact)    

# i  = 12345

# 12345 /  10 =  

i  = 1234
# sum  = 0
rev = 0
while(i > 0):
    digit = i % 10
    # sum  = sum  + digit
    rev = rev * 10 + digit
    i = i // 10
print(rev )    
