A = list(range(11))
avr = sum(A) / len(A)
if avr in A:
    print(int(avr))
else:
    print(f"В массиве нет числа {avr}")
