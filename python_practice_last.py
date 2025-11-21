# 여기에 코드를 작성하세요
import numpy as np

# 1. 환자 목록 출력
print("=== 환자 목록 ===")
for p in patients:
  name = p["name"]
  age = p["age"]
  dept = p["department"]
  status = "입원중" if p["is_admitted"] else "외래"
  print(f"{name}({age}세) - {dept} - {status}")

# 2. 고위험 환자 필터링 (혈압 140↑ 또는 체온 38.0↑)
print("\n=== 고위험 환자(혈압 140↑ 또는 체온 38.0↑) ===")
high_risk_patients = [p for p in patients if p["vitals"]["systolic"] >= 140 or p["vitals"]["temperature"] >= 38.0]

if high_risk_patients:
  for p in high_risk_patients:
    print(f"{p["name"]}: 혈압 {p["vitals"]["systolic"]} mmHg, 체온 {p["vitals"]["temperature"]}℃")
else:
  print("고위험 환자 없음")
# 3. 신규 환자 등록 함수 작성 (기본 진료과는 "내과")
def add_patient(name, age, systolic, diastolic, temperature, department="내과", is_admitted=False): # 신규 환자는 입원중이 아니므로 Falsse 기본값 지정
  new_patient = {
      "name" : name,
      "age": age,
      "department": department,
      "vitals": {
          "systolic": systolic,
          "diastolic": diastolic,
          "temperature": temperature
        },
      "is_admitted": is_admitted
    }
  patients.append(new_patient)
new_patient_information_name=input("환자의 이름을 입력하시오")
new_patient_information_age=int(input("환자의 나이를 입력하시오"))
new_patient_information_department=input("환자의 과를 입력하시오")
new_patient_information_systolic=int(input("환자의 혈압을 입력하시오"))
new_patient_information_diastolic=int(input("환자의 심박수를 입력하시오"))
new_patient_information_temperature=float(input("환자의 온도 입력하시오"))
new_patient_information_is_admitted=bool(input("환자의 입원 유무 입력하시오"))
add_patient(new_patient_information_name, new_patient_information_age, new_patient_information_systolic, new_patient_information_diastolic, new_patient_information_temperature, new_patient_information_department, new_patient_information_is_admitted)
#add_patient("신환자", 50, 150, 95, 37.9, is_admitted=True)
print("\n=== 신규 환자 추가 후 ===")
print(f"총 환자 수: {len(patients)}명")


# 4. 통계 함수 작성 (전체 수, 입원 수, 평균 혈압, 발열 수)
def print_stats(patients_list):
  total = len(patients_list)
  admitted = len([p for p in patients_list if p["is_admitted"]])
  pressure = np.mean([p["vitals"]["systolic"]])
  # avg_systolic = sum(p["vitals"]["systolic"] for p in patients_list) / total
  fever = len([p for p in patients_list if p["vitals"]["temperature"] >= 37.5])

  print("\n=== 통계 ===")
  print(f"전체 환자 수: {total}명")
  print(f"입원 환자 수: {admitted}명")
  print(f"평균 수축기 혈압: {pressure:.1f} mmHg")
  print(f"발열 환자 수: {fever}명")
print_stats(patients)
# 5. 정렬: 혈압 기준 오름차순 / 나이 기준 내림차순
print("\n=== 혈압 오름차순 정렬 ===")
patients_by_bp = sorted(patients, key=lambda p: p["vitals"]["systolic"])
for p in patients_by_bp:
    print(f"{p['name']}: {p['vitals']['systolic']} mmHg")

print("\n=== 나이 내림차순 정렬 ===")
patients_by_age = sorted(patients, key=lambda p: p["age"], reverse=True)
for p in patients_by_age:
    print(f"{p['name']}: {p['age']}세")
