class MedicalStaff:
  def __init__(self, name, department):
    self.name = name
    self.department = department
    self.status = "근무중"

  def change_status(self, new_status):
    self.status = new_status
    return self.status

  def get_info(self):
    return f"{self.name}{self.department} - {self.status}"

class Nurse(MedicalStaff):
  def __init__(self, name, department):
    super().__init__(name, department)
    self.patients = []
  
  def assign_patient(self, patient_name):
    if self.status != "근무중":
      return f"{self.name}는 현재 휴무중이므로 환자 배정 불가"
    else:
      if patient_name not in self.patients:
        self.patients.append(patient_name)
        return f"{self.name}에게 {patient_name} 배정 완료"
      else:
        return f"{self.name}님이 {patient_name}담당중 입니다."
  
  def remove_patient(self, patient_name):
    if patient_name in self.patients:
      self.patients.remove(patient_name)
      return f"{patient_name}배정 취소"
    else:
      return f"{patient_name}님은 {self.name}님의 환자가 아닙니다"

class Doctor(MedicalStaff):
  def __init__(self, name, department, specialty):
    super().__init__(name, department)
    self.specialty = specialty

  def treat_patient(self, patient_name, diagnosis):
    if self.status != "근무중":
      return f"{self.name}는 현재 휴무중이므로 환자 배정 불가"
    return f"{self.name}가 {patient_name}을(를) {diagnosis}로 진료했습니다"

# 의료진 생성
nurse = Nurse("김간호사", "내과")
doctor = Doctor("이의사", "외과", "정형외과")

# 환자 배정
print("=== 환자 배정 결과 ===")
print(nurse.assign_patient("환자A"))
print(nurse.assign_patient("환자B"))

# 의사 상태 변경
doctor.change_status("휴무중")
print("이의사는 현재 휴무중이므로 환자 배정 불가")

# 현재 상황 출력
print("\n=== 의료진 현황 ===")
print(nurse.get_info())
print(doctor.get_info())

# 의사 근무 복귀 후 진료
doctor.change_status("근무중")
print("\n=== 진료 결과 ===")
print(doctor.treat_patient("환자D", "무릎 관절염"))
