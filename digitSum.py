
def superDigit(n, k):

    def sumDigit(num):
        if num < 10:
            return num

        digit_sum = 0

        while num:
            digit_sum += num % 10
            num = num//10
        return sumDigit(digit_sum)


    # reating the given number k times is the same as mulitplying its digit sum with k

    digit_sum = 0
    n = int(n)
    while n:
        digit_sum += n % 10
        n //= 10

    digit_sum *= k
    return sumDigit(digit_sum)
