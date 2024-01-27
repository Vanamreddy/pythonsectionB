def prime_number(n, i=2):
    if n==i:
        return 'prime'
    elif n%i==0:
        return 'not prime'
    return prime_number(n,i+1)
print(prime_number(5))