def main():
    n, a, b = map(int, input().split())

    h = [int(k) for k in input().split()]

    first_hole_size = h.pop(0)

    h.sort(reverse=True)

    sum_holes = sum(h)

    answer = 0
    while answer < (n-1):
        calc_first_hole = (first_hole_size*a)/(sum_holes + first_hole_size)
        if calc_first_hole >= b:
            break
        sum_holes -= h[0]
        h.pop(0)
        answer += 1

    print(answer)

if __name__ == "__main__":
    main()