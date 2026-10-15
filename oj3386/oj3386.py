'''Duplicate I'''
def main():
    '''Duplicate I'''
    m = int(input())
    n = int(input())

    group1 = {input() for _ in range(m)}
    group2 = {input() for _ in range(n)}

    duplicates = group1 & group2

    if duplicates:
        for student_id in sorted(map(int, duplicates), reverse=True):
            print(student_id)
    else:
        print("Nope")
main()
