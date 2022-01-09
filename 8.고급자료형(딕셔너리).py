# 8. 고급자료형2(딕셔너리)
# 공통점 : 데이터 여러개 저장 가능
# 차이점 : KEY가 리스트는 순서번호, 딕셔너리 자유롭게
# 센서데이터
sizes = [250,260,255,260,270]
name="이원희"


# Key - Value 구조
# 게임, 웹, 모바일
# 게임 : 유저데이터, 웹:회원데이터, 모바일:유저데이터
sizes2 = {"강한백발사이즈":250, name:260}
강한백 = {"나이":30, "학력":"대학교졸업", "사는곳":"서울"}
print(sizes[0])
print(sizes2["강한백발사이즈"])

user = "wow"
user2 = "bback"
user3 = "hi"

level = {user:42, user2:56, user3:25}
item = {user:"모자", user2:"검", user3:"쓰레기"}

print(level[user])
print(item[user2])