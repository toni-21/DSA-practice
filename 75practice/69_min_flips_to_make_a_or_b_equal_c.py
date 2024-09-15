def minFlips(a: int, b: int, c: int) -> int:
    flips = 0
    while a or b or c:
        # get the last bit of each
        a_bit, b_bit, c_bit = a & 1, b & 1, c & 1

        if c_bit == 0:
            # this would ensure that the 1s are flipped to give a 0
            flips += a_bit + b_bit
        else:
            if a_bit == 0 and b_bit == 0:
                # if both are 0, only 1 needs to be flipped
                flips += 1

        # right shift a,b&c and equate to new values
        a, b, c = a >> 1, b >> 1, c >> 1

    return flips


answer = minFlips(a=2, b=6, c=5)
print("answer is")
print(answer)
