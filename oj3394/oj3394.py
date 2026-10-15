'''ส่งต่อ'''
def main():
    '''ส่งต่อ'''
    n, s = map(int, input().split())

    next_student = [0] + [int(input()) for _ in range(n)]

    visited = set()
    current = s

    while current and current not in visited:
        visited.add(current)
        current = next_student[current]

    print(len(visited))

main()
