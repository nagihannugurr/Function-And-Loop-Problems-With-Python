def collatz_array(n):
    #dizi1 = []
    number = n
    count = 1 #çünkü 2 den başlıyor 2 de 1 adım vardır

    while number != 1:
        if number % 2 == 0:
            number = number // 2
            count += 1
        else:
            number = 3 * number + 1
            count += 1
    return [count , n]   #giren sayının adım sayısı ve kendisi döner


full_list = []

for i in range(2,1000000):
    full_list.append(collatz_array(i))

sortedList = sorted(full_list, reverse=True)
print(sortedList[:1])