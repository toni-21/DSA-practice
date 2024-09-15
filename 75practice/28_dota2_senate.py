from collections import deque


def predicPartyVictory(senate: str) -> str:
    n = len(senate)
    rQ = deque()
    dQ = deque()

    for pos, char in enumerate(senate):
        if char == "R":
            rQ.append(pos)
        else:
            dQ.append(pos)

    while dQ and rQ:
        r = rQ.popleft()
        d = dQ.popleft()
        if r < d:
            rQ.append(r + n)
        else:
            dQ.append(d + n)

    return "Radiant" if rQ else "Dire"


answer = predicPartyVictory(senate="RDRDRDD")
print("answer is")
print(answer)
