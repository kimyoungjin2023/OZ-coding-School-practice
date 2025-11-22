def create_prescription(patient_name, medicine, dosage="적정량", frequency="1일 3회", duration="7일"):
    # 코드 작성
        prescription = f"""
처방전
================
환자명: {patient_name}
약물명: {medicine}
용량: {dosage}
복용법: {frequency}
처방 기간: {duration}
================
    """
        return prescription.strip()


result1 = create_prescription("김환자", "아스피린")
print(result1)

print("\n" + "="*30 + "\n")

result2 = create_prescription("이환자", "타이레놀", dosage="500mg", duration="5일")
print(result2)
