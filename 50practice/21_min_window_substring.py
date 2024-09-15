from collections import defaultdict


def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    t_map = defaultdict(int)
    for ch in t:
        t_map[ch] += 1

    left, t_rem_count, window = 0, len(t), (0, float("inf"))

    for right, char in enumerate(s):
        if t_map[char] > 0:
            t_rem_count -= 1
        t_map[char] -= 1

        if t_rem_count == 0:
            while True:
                if t_map[s[left]] == 0:
                    break
                
                t_map[s[left]] += 1
                left += 1

            if right - left < window[1] - window[0]:
                window = (left,right)

    return "" if window[1] >= len(s) else s[window[0] : window[1] + 1]


answer = minWindow(s="ADOBECODEBANC", t="ABC")
print("answer is", answer)
