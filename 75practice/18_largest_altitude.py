def largestAltitude(gain: list[int]) -> int:
    maxAlt = 0
    curr = 0
    for g in gain:
        curr += g
        maxAlt = max(curr, maxAlt)
    return maxAlt
    
answer = largestAltitude(gain=[-5,1,5,0,-7])
print("answer is:")
print(answer)