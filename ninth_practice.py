patient_names = ["김환자", "이환자", "박환자", "최환자"]  # 환자 명단
prescribed_drugs = ["해열제", "항생제", "진통제", "비타민"]  # 처방 약물
dosages = ["1일 3회", "1일 2회", "1일 1회", "1일 1회"]  # 복용법

for name, drug, dosage in zip(patient_names, prescribed_drugs, dosages):
  print(f"{name}: {drug} ({dosage})")
