'''Shorten'''
def main():
    '''Shorten'''
    number = []
    while True:
        n = int(input())
        if n == -1:
            break
        number.append(n)

    if not number:
        return

    result = []
    start = number[0]
    end = number[0]

    for i in range(1, len(number)):
        if number[i] == end + 1:
            end = number[i]
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f'{start}-{end}')
            start = number[i]
            end = number[i]

    if start == end:
        result.append(str(start))
    else:
        result.append(f'{start}-{end}')

    print(', '.join(result))
main()
