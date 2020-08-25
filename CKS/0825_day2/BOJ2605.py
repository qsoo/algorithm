# T = int(input())  # 학생 수
# students = list(map(int, input().split()))  # 학생들 뽑은 수
#
# # 학생들 번호 리스트 생성
# num_students = [i for i in range(1, len(students)+1)]
#
# result = [] # 최종 배열
#
# # 뽑은 수 리스트에 접근해서 insert로 삽입시키기
# for idx, student in enumerate(students):
#     # 이동한만큼 나머지 뒤로 밀기
#     result.insert(len(result) - student, num_students[idx])
#
# for i in result:
#     print(i, end=' ')

s = "ABC"
s.insert(0, "a")
print(s)