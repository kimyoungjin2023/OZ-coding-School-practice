from datetime import datetime

current_year = datetime.now().year

# 1. 환자 기본정보 저장
patient_name = "박건강"
birth_year = 1990
height = 170
weight = 65
gender = "남성"

# 2. BMI 계산
height_m = height / 100

BMI = weight / (height_m ** 2)

# 3. 현재 나이 계산
age = current_year - birth_year + 1

# 4. 성인 여부 판별
is_adult = age >= 20

# 5. 결과 출력
print("=== 환자 정보 ===")
print(f"이름 : {patient_name} ({gender}, {age}세)")
print(f"키 : {height}cm , 몸무게 : {weight}kg")
print(f"BMI : {BMI:.1f}")
print(f"출생연도 : {birth_year}")
print(f"성인 여부 : {is_adult}")
