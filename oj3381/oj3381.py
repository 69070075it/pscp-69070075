'''Point Sorting'''
def main():
    '''Point Sorting'''
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x + y, -y, x, y))

        points.sort()

        for point in points:
            print(f"{point[2]} {point[3]}")

main()
