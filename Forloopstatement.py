#Perfect square numbers between 1 and 500
for num in range(1, 501):
    if int(num**0.5)**2 == num:
        print(num, end=' ')