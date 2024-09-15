def tribonacci(n: int) -> int:
    t0, t1, t2 = 0, 1, 1
    curr = 0
    i = 2

    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    while i < n:
        curr = t0 + t1 + t2
        t0, t1, t2 = t1, t2, curr
        i += 1
    return curr


answer = tribonacci(n=25)
print("answer is")
print(answer)
