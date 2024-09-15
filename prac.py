# x = ('hello world')
# sd = None;
# list = [23,434,34,34]
# st = {'sdkmv','sdvsdv','sd','sd'}
# map = {"sdc":"sdc", 23:"sdc", False:"sdc", True: "sc", 23:3}

# list.append(23)
# a =  100
# b  = 200

# for i in range(0,5,2):
#     print(i)

# print(sd)
# print(x[0])
# print(map)
# print(bool(None))
# print(bool(0))
# print(st)
# print(bool(str))
# print(list.count(23))

# def func(name):
#     print('name is ', name,'dfv')

# func(name ='sdc')

# class Person:
#     __isNew = False
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#     def __str__(self) -> str:
#         return f"{self.name} {self.age}"
        
#     def ise(self):
#         return self.__isNew
    
# p = Person('Tobi', 54)
# print(p)
    
# tre = [1,2,3]
# res = []
# res.extend([1,2])
# print(res)

def primeFactor(num : int) -> int:
    #returns the prime factors of num
    res = []
    div = 2
    while div < num:
        if num % div == 0:
            found = False
            for i in res:
                if div % i == 0:
                    found = True
                    break
            if not found:
                res.append(div)
        div += 1

    return res



answer = primeFactor(num=8992)
print(answer)