def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    i = 1
    flowerbed.insert(0, 0)
    flowerbed.append(0)

    while i < len(flowerbed) - 1:
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1
        i += 1
    return True if n <= 0 else False


answer = canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2)
print("answer is", answer)
