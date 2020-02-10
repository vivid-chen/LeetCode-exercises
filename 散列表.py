# book = dict()
book = {}

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.47
print(book)

print(book["avocado"])

# 查询投票是否重复
voted = {}
def check_voter(name):
    if voted.get(name):
        print("kick them vote!")
    else:
        voted[name] = True
        print("let them vote!")

check_voter("tom")

check_voter("tom")