#Initialize counter
num = 1

#Loop from 1 to 100
while num <= 100:
    #Check if num is NOT divisible by 3 or 5
    if num % 3 != 0 and num % 5 != 0:
        print(num, end=' ')
    #Increment counter
    num += 1
