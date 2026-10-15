'''[LEARNING LOGS] หั่นขนมปัง'''
def main():
    '''[LEARNING LOGS] หั่นขนมปัง'''
    w, h, _, _ = map(int, input().split())
    x_cuts = [0] + list(map(int, input().split())) + [w]
    y_cuts = [0] + list(map(int, input().split())) + [h]

    widths = [x_cuts[i] - x_cuts[i - 1] for i in range(1, len(x_cuts))]
    heights = [y_cuts[i] - y_cuts[i - 1] for i in range(1, len(y_cuts))]

    widths.sort(reverse=True)
    heights.sort(reverse=True)

    w1 = widths[0]
    w2 = widths[1] if len(widths) > 1 else widths[0]

    h1 = heights[0]
    h2 = heights[1] if len(heights) > 1 else heights[0]

    areas = sorted([w1 * h1, w1 * h2, w2 * h1, w2 * h2], reverse=True)

    print(f"{areas[0]} {areas[1]}")
main()
