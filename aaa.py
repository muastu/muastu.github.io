def taibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return   taibo(n-1) + taibo(n-2) + taibo(n-3)
print(taibo(10))

def dayOfYear(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])

    arr = [31,28,31,30,31,30,31,31,30,31,30,31]

    if year %  400 == 0:
        arr[1] = 29
    if year % 100 != 0 and year % 4 == 0:
        arr[1] = 29
    sum = 0
    for i in range(month-1):
        sum += arr[i]
    return sum + day

print(dayOfYear("2004-12-31"))