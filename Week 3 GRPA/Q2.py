n = int(input())

for f in range(2, n + 1):
    if n % f == 0:
        is_prime=True
        for i in range(2,f):
            if f%i==0:
                is_prime=False
                break
    
        if is_prime:
            print(f)
