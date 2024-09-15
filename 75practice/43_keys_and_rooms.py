def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    visited_rooms = set()
    stack = [0]
    while stack:
        room = stack.pop()
        visited_rooms.add(room)
        for key in rooms[room]:
            if key not in visited_rooms:
                stack.append(key)
    return len(visited_rooms) == len(rooms)


answer = canVisitAllRooms(rooms=[[1], [2], [3], []])
print("answer is")
print(answer)
