# Access Specifiers :-


class Emperor:
    army_strength = 20000
    _children = 4
    __Wife = 1
    # print(.__Wife)

class Commander(Emperor):
    pass

class War_minister:
    pass


Henry = Emperor()
Nicholus = War_minister()
Apocalypse = Commander()

# print(Emperor.__Wife)
# print(Commander.__Wife)
# print(War_minister.__Wife)

print(Apocalypse._Emperor__Wife)
# print(Nicholus.__Wife)
# print(Apocalypse.__Wife)
