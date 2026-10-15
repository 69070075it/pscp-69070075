'''หุ่นยนต์เคาะเสียงกระเบื้อง'''
def main():
    '''หุ่นยนต์เคาะเสียงกระเบื้อง'''
    n, p = input().split()
    n, p = int(n), float(p)

    grid = [list(map(int, input().split())) for _ in range(n)]

    total_bad_tiles = 0
    total_bad_points = 0

    for row in grid:
        tiles = sum(1 for val in row if val > 0)
        points = sum(row)
        total_bad_tiles += tiles
        total_bad_points += points
        print(f"{' '.join(map(str, row))} {tiles} {points}")

    col_tiles = [sum(1 for i in range(n) if grid[i][j] > 0) for j in range(n)]
    col_points = [sum(grid[i][j] for i in range(n)) for j in range(n)]

    print(" ".join(map(str, col_tiles)))
    print(" ".join(map(str, col_points)))
    print(f"{total_bad_tiles} {total_bad_points} {total_bad_points * p:.2f}")

main()
