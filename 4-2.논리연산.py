# or and not 논리연산

# and 그리고 : 무조건 전부 true면 결과는 true
age = 8
money = 120000

영화관람가능 = age > 19 and money == 12000

print(영화관람가능)

# or 또는 : 하나라도 true면 결과는 true
print(3>2 or 1>4)
print(3>1 or 4>2)


# not 반대(반전) : ~가 아닌

print(not True)
print(not 3>2)
print(3<=2)