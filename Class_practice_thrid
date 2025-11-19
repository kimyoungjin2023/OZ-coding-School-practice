# 부모 클래스 (기본 의료진)
class Doctor:
    def __init__(self, name, specialty):
        """의사 정보를 초기화합니다"""
        self.name = name
        self.specialty = specialty
        self.patient_list = []

    def diagnose_patient(self, patient_name, diagnosis):
        """환자를 진단하고 기록합니다"""
        patient_record = {"name": patient_name, "diagnosis": diagnosis}
        self.patient_list.append(patient_record)
        print(f"{self.name} 의사가 {patient_name} 환자를 {diagnosis}로 진단했습니다.")


class Specialist(Doctor):
  #생성자 함수
  def __init__(self, name, specialty, subspecialty):
    super().__init__(name,specialty)

    #고유 속성 세팅
    self.subspecialty = subspecialty

  def diagnose_patient(self, patient_name, diagnosis):

    #부모 클래스 메서드 실행
    super().diagnose_patient(patient_name, diagnosis)

    #자식 클래스 고유 매서드 실행
    print(f"{self.subspecialty} 전문의의 정밀 진단 완료")


specialist = Specialist("박전문의", "내과", "심장내과")
specialist.diagnose_patient("환자C", "부정맥")
