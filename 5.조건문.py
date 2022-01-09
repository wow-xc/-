# 5. 조건문을 1개
if 5>3 and 2>1:
  print("참")
if 5>3 or 2<1:
  print("거짓")

# 조건문을 2개 -> Yes or No
level = 99
if level>=99:
  print("참")
else:
  print("거짓")   

# 조건문 여러개 -> if elif elif elif elif elif else
level = 99
if level>50:
  print("골드")
elif level>30:
  print("실버")
elif level>10:
  print("브론즈")
else:
  print("아이언")

age = 15
if age>70:
  print("노인")
elif age>19:
  print("성인") 
elif age>13:
  print("청소년")
else:
  print("어린이")     