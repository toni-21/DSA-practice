def compress(chars: list[str]) -> bool:
    n = len(chars)
    if (n < 2):
        return n
    
    #start position of contiguous char group we are currently on
    anchor = 0
    #count of times we write to the array
    write = 0

    #1.iterate until we find a different char
    #2. record the count of the repeated char 
    for pos, char in enumerate(chars):
        if pos + 1 == n or chars[pos + 1] != char:
            chars[write] = char
            write += 1

            #char is repeated if pos is ahead of anchor
            if pos > anchor:
                repeated_times = pos - anchor + 1
            #write each digit separately and increase write count as well
                for i in str(repeated_times):
                    chars[write] = i
                    write += 1
            #wupdate anchor position to the next start of contiguous strings
            anchor = pos + 1

    return write

answer = compress(chars=['a','a','b','b','c','c','c'])
print("answer is:")
print(answer)