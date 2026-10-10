results = []

for num in range(2000, 3201):
    if num % 7 == 0 and num % 3 != 0:
        results.append(str(num))

print(",".join(results))