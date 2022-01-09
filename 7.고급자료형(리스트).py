# 자료형 (숫자형(int) 문자형(string), Boolean형)

# 고급자료형 (리스트)
user1 = "Roblox"
user2 = "wow"
user3 = "bbackdummy"

# 리스트의 접근은 순서대로 (순서번호)
users = ["roblox", "wow", "bbackdummy", "bbb", "ccc", "dddd"]
print(users[0])
print(users[1])
print(users[-1])
print(users[-2])


users = ["roblox", "WOW", "bbackdumy", "aaa", "dsds" "ooo"]
print(users[0], users[1], users[-3], users[-1])

# 리스트 안의 데이터를 여러개 가져올 때 (slicing문법)
print(users[2:6])
sizes = [250, 230, 260, 240, 250]
print(sizes[1:4])
print(sizes[1:])
print(sizes[:])
print(sizes[:-3])

print(users[2:6])
sizes = [280, 200, 230, 250, 265]
print(sizes[1:4])
print(sizes[1:])
print(sizes[:-1])
print(sizes[:])