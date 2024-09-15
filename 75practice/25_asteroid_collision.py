def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            if -a > stack[-1]:
                stack.pop()
                continue
            elif -a == stack[-1]:
                stack.pop()
            break
        else:
            stack.append(a)
    return stack
 
answer = asteroidCollision(asteroids=[5,10,-5])
print("answer is:")
print(answer)