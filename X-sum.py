for __ in range(int(input())):
    n, m = map(int, input().split())

    nums = []

    for _ in range(n):
        nums.append(list(map(int, input().split())))

    row, col = len(nums), len(nums[0])
    x_sum = 0
    for r in range(row):
        for c in range(col):
            main_diagonal, sub_diagonal = 0, 0

            i, j = r, c
            # for main diagona
            while i >= 0 and j >= 0 and i < row and j < col:
                main_diagonal += nums[i][j]
                j -= 1
                i -= 1
            i, j = r, c
            while i < row and j < col:
                main_diagonal += nums[i][j]
                i += 1
                j += 1

            # for sub diagonal
            i, j = r, c
            while i >= 0 and i < row and j < col:
                sub_diagonal += nums[i][j]
                i -= 1
                j += 1
            i, j = r, c
            while j >= 0 and i < row and j < col:
                sub_diagonal += nums[i][j]
                i += 1
                j -= 1

            total = sub_diagonal + main_diagonal - 3 * nums[r][c]
            x_sum = max(x_sum, total)

    print(x_sum)
