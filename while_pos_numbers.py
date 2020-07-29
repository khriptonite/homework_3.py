num = 0
sum = 0
val = 0
avg = 0

print("Introduceti cate un numar pozitiv: ")

while num >= 0:
    try:
        num = int(input("VALOARE: "))   
        if num >= 0:
            sum += num
            val += 1
            avg = sum / val
    except Exception:   
        num = -1     

print(" ● " * 20)    
print("Suma numerelor introduse este: ", sum)
print("Numarul total de valori este: ", val)
print("Valoarea medie este: ", int(avg))
print(" ● " * 20)   