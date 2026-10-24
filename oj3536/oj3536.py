'''isPrime_large'''
def main():
    '''isPrime_large'''
    n = int(input())

    if n <= 1:
        print("NO")
        return

    i = 2
    while i * i <= n:
        if not n % i:
            print("NO")
            return
        i += 1

    print("YES")
main()
