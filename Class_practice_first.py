class Patient:
  def __init__(self, name, age, patient_id):
    self.name = name
    self.age = age
    self.patient_id = patient_id

  def __str__(self):
    return f"환자 {self.patient_id}: {self.name}({self.age}세)"

patient = Patient("김환자", 45, "P001")
print(patient)
