def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    res = []
    largest = max(candies)
    for i in candies:
        if (i + extraCandies) >= largest:
            res.append(True)
        else:
            res.append(False)
    return res


answer = kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3)
print("answer is", answer)


def decentNumber(n: int):
    fives_count = (n // 3) * 3
    while fives_count >= 0:
        threes_count = n - fives_count
        if threes_count % 5 == 0:
            print('5' * fives_count + '3' * threes_count)
            return
        fives_count -= 3
    print(-1)

decentNumber(4)
