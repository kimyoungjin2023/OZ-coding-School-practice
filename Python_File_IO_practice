def save_patient(patient_id, name, diagnosis):
    """환자 정보를 파일에 저장합니다"""
    try:
      if not patient_id or not name:
          raise ValueError("환자 ID와 이름은 필수입니다")

      filename = f"{patient_id}.txt"
      with open(filename, 'w', encoding = "UTF-8") as file:
          file.write(f"환자명 : {name}\n")
          file.write(f"진단 : {diagnosis}\n")

      print(f"{name} 저장완료")
      return True

    except ValueError as error:
      print(f"오류 : {error}")
      return False
    except Exception as error:
      print(f"오류 : {error}")
      return False

def load_patient(patient_id):
    """환자 정보를 파일에서 읽습니다"""
    try:
      filename = f"{patient_id}.txt"
      with open(filename, 'r', encoding = "UTF-8") as file:
        record = file.read()

      print(f"{patient_id}조회 완료")
      return record

    except FileNotFoundError:
      print(f"{patient_id}님을 찾을 수가 없습니다.")
      return None
    except Exception as error:
      print(f"{error} 조회실패 ")
      return None

      # 테스트 데이터
test_patients = [
    ("P001", "김환자", "감기"),
    ("P002", "이환자", "두통"),
    ("", "박환자", "복통"),      # 오류 케이스: 빈 ID
    ("P003", "", "발열"),        # 오류 케이스: 빈 이름
    ("P004", "최환자", "고혈압")
]

test_lookups = ["P001", "P002", "P999"]  # P999는 없는 환자


# 1. 환자 등록 테스트
print("=== 환자 등록 테스트 ===")
for patient_id, name, diagnosis in test_patients:
    save_patient(patient_id, name, diagnosis)

# 2. 환자 조회 테스트
print("\n=== 환자 조회 테스트 ===")
for patient_id in test_lookups:
    record = load_patient(patient_id)
    if record:
        print(record)
