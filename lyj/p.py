scores = [85,92,55,78,40,96,73]
grade = 0

#총 학생 수 출력
total_students = len(scores)
print(f"총 학생 수: {total_students}명 ")

#통계
Max_score = max(scores)
Min_score = min(scores)
average = sum(scores)/len(scores)
print(f"최고점: {Max_score}점")
print(f"최저점: {Min_score}점")
print(f"평균: {average:.1f}점")

#점수별 등급 출력

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"점수: {score} -> {grade}학점")

#4. 정렬 후  상위 3개
scores.sort(reverse=True)
top = scores[:3]
print(f"상위 3개 : {top}")