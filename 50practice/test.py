def countPairs(k: int, numbers: list[int]) -> int:
    num_set = set(numbers)
    count = 0

    for n in num_set:
        if n + k in num_set:
            count += 1

    return count


answer = countPairs(k=1, numbers=[1, 1, 1, 2])
print("answer is", answer)
