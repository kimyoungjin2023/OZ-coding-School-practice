patients_db = [
    {"patient_id": "P001", "name": "김환자", "age": 65, "department": "내과", "disease": "고혈압"},
    {"patient_id": "P002", "name": "이환자", "age": 45, "department": "외과", "disease": "맹장염"},
    {"patient_id": "P003", "name": "박환자", "age": 32, "department": "소아과", "disease": "감기"}
]

# 1. 첫 번째 환자 정보 조회
print("=== 첫 번째 환자 정보 ===")
print(f"환자번호: {patients_db[0]["patient_id"]}")
print(f"이름: {patients_db[0]["name"]}")
print(f"나이: {patients_db[0]["age"]}")
print(f"진료과: {patients_db[0]["department"]}")
print(f"질병: {patients_db[0]["disease"]}")

# 2. 두 번째 환자 질병 수정
print("\n\n=== 환자 질병 수정 전 ===")
print(f"환자번호: {patients_db[1]["patient_id"]}")
print(f"이름: {patients_db[1]["name"]}")
print(f"질병: {patients_db[1]["disease"]}")
patients_db[1]["disease"] = "급성맹장염"

print("\n\n=== 환자 질병 수정 후 ===")
print(f"환자번호: {patients_db[1]["patient_id"]}")
print(f"이름: {patients_db[1]["name"]}")
print(f"질병: {patients_db[1]["disease"]}")


# 3. 새 환자 등록 및 데이터베이스에서 조회
new = {"patient_id" : "P004", "name" : "홍환자", "age" : "40", "department": "피부과", "disease": "아토피"}
patients_db.append(new)
print("\n\n=== 새 환자 등록 ===")
print(f"환자번호: {patients_db[3]["patient_id"]}")
print(f"이름: {patients_db[3]["name"]}")
print(f"나이: {patients_db[3]["age"]}")
print(f"진료과: {patients_db[3]["department"]}")
print(f"질병: {patients_db[3]["disease"]}")
print(f"현재 총 환자 수: {len(patients_db)}명")

# 4. 환자 퇴원 처리
print("\n\n=== 환자 퇴원 처리 ===")
discharged_from_hospital = patients_db.pop()
print(f"퇴원 환자번호: {discharged_from_hospital["patient_id"]}")
print(f"퇴원 환자명: {discharged_from_hospital["name"]}")
print(f"퇴원 후 총 환자 수: {len(patients_db)}명")

# 5. 나이 통계 계산
ages = {patients_db[0]["age"], patients_db[1]["age"], patients_db[2]["age"]}
print("\n\n=== 환자 나이 통계 ===")
print(f"최고령 환자 나이: {max(ages)}세")
print(f"최연소 환자 나이: {min(ages)}세")
print(f"평균 나이: {sum(ages)/len(ages):.1f}")


# 6. 최종 현황 출력
print("\n\n==================================================")
print("최종 병원 환자 데이터베이스 현황")
print("==================================================")
print(f"총 입원 환자: {len(patients_db)}명")
