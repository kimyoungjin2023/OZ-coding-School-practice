patients = [
    {"name": "김환자", "age": 65, "systolic": 145},
    {"name": "이환자", "age": 45, "systolic": 125},
    {"name": "박환자", "age": 32, "systolic": 115},
    {"name": "최환자", "age": 28, "systolic": 135},
    {"name": "정환자", "age": 70, "systolic": 190}
]

# 여기에 코드를 작성하세요
# 정상: 수축기 < 120
# 고혈압 전단계: 120 ≤ 수축기 < 140
# 1기 고혈압: 140 ≤ 수축기 < 160
# 2기 고혈압: 수축기 ≥ 160


# 1. 개별 환자 혈압 분류 (if-elif-else 활용)
print("=== 개별 환자 혈압 분류 ===")
for patient in patients:
  name = patient["name"]
  age = patient["age"]
  systolic = patient["systolic"]

  if systolic < 120:
    result = "정상"
    result_1 = "정기검진"
  elif systolic < 140:
    result = "고혈압 전단게"
    result_1 = "생활습관 개선"
  elif systolic < 160:
    result = "1기 고혈압"
    result_1 = "약물 치료 필요"
  else:
    result = "2기 고혈압"
    result_1 = "즉시 치료 필요"
  
  print(f"{name}({age}): {systolic}mmHg - {result} ({result_1})")


# 2. 응급 처치 대상 즉시 감지 (break 활용)
print("\n=== 응급 처치 대상 ===")
first_aid_target = 0
for patient in patients:
  name = patient["name"]
  systolic = patient["systolic"]

  if systolic >= 180:
    print(f"🚨 응급: {name} ({systolic} mmHg) - 즉시 치료 필요")
    first_aid_target = 1
    break

if first_aid_target == 0:
  print("응급 처치가 필요한 환자가 없습니다.")


# 3. 혈압 등급별 통계 계산 (리스트 컴프리헨션 활용)
print("\n=== 혈압 등급별 통계 ===")

normal = len([patient for patient in patients if patient["systolic"] < 120])
prehypertension = len([patient for patient in patients if 120 <= patient["systolic"] < 140])
one_high_blood_pressure = len([patient for patient in patients if 140 <= patient["systolic"] < 160])
two_high_blood_pressure = len([patient for patient in patients if patient["systolic"] >= 160])

total_people = len(patients)

print(f"정상: {normal}명 ({normal/total_people * 100}%)")
print(f"고혈압 전 단계: {prehypertension}명 ({prehypertension/total_people * 100}%)")
print(f"1기 고혈압: {one_high_blood_pressure}명 ({one_high_blood_pressure/total_people * 100}%)")
print(f"2기 고혈압: {two_high_blood_pressure}명 ({two_high_blood_pressure/total_people * 100}%)")


# 4. 전체 현황 요약 (내장 함수 활용)
print("\n=== 전체 현황 요약 ===")

systolic = [patient["systolic"] for patient in patients]

systolic_average = sum(systolic) / total_people
high_blood_percent = (one_high_blood_pressure +two_high_blood_pressure) / total_people *100 
first_aid = len([patient for patient in patients if patient["systolic"] >= 180])

print(f"총 환자 수: {total_people}명")
print(f"평균 혈압: {systolic_average}mmHg")
print(f"고혈압 환자: {one_high_blood_pressure +two_high_blood_pressure}명 ({high_blood_percent}%)")
print(f"응급 처치 대상: {first_aid}명")
