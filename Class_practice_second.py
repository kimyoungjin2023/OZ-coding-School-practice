class Doctor:
  def __init__(self, name, specialty):
    self.name = name
    self.specialty = specialty
    self.patient_list = []


  def diagnose_patient(self, patient_name, diagnosis): 
    patient_record = {"name": patient_name, "diagnosis" : diagnosis}
    self.patient_list.append(patient_record)
    print(f"{self.name} 의사가 {patient_name} 환자를 {diagnosis}로 진단했습니다.")


doctor = Doctor("김의사", "내과")
doctor.diagnose_patient("환자A", "고혈압")
doctor.diagnose_patient("환자B", "당뇨병")

print(f"진료 환자들: {doctor.patient_list}")
print(f"진료 환자 수: {len(doctor.patient_list)}")
