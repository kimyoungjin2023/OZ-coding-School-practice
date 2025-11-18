# 기본 데이터
clinic_info = {
    "operating_hours": (9, 18),    # 클리닉 운영시간: 9시-18시
    "lunch_break": (12, 13),       # 점심시간: 12시-13시
}

# 예약 현황 리스트 (전역 변수)
appointments = []  # 딕셔너리 리스트: [{"time": 10, "patient": 김환자}, ...]

# 상태 키워드
AVAILABLE = "AVAILABLE"           # 예약 가능
LUNCH_TIME = "LUNCH_TIME"         # 점심시간
OUT_OF_HOURS = "OUT_OF_HOURS"     # 운영시간 외
ALREADY_BOOKED = "ALREADY_BOOKED" # 이미 예약됨


def check_appointment_availability(hour):
    """
    예약 가능 여부를 종합적으로 확인합니다.

    Args:
        hour (int): 예약 시간 (0-23)

    Returns:
        tuple: (가능여부(bool), 상태 키워드(str))
    """
    # 여기에 코드를 작성하세요
    start, end = clinic_info["operating_hours"]
    lunch_start, lunch_end = clinic_info["lunch_break"]
    
    if start >= hour or hour > end:
        return False, OUT_OF_HOURS


    if lunch_start <= hour < lunch_end:
        return False, LUNCH_TIME

      
    for appointment in appointments:
        if appointment["time"] == hour:
            return False, ALREADY_BOOKED

    return True, AVAILABLE
    pass

def add_appointment(patient_name, hour):
    """
    새로운 예약을 추가합니다.

    Args:
        patient_name (str): 환자 이름
        hour (int): 예약 시간 (0-23)

    Returns:
        str: 예약 결과 메시지
    """
    # 여기에 코드를 작성하세요
    is_available, status = check_appointment_availability(hour)

    if is_available:
        appointments.append({"time": hour, "patient": patient_name})
        return f"{patient_name} : {hour}시: 예약 완료"
    else:
        if status == LUNCH_TIME:
            reason = "점심시간 (예약 불가)"
        elif status == OUT_OF_HOURS:
            reason = "운영시간 외 (예약 불가)"
        elif status == ALREADY_BOOKED:
            reason = "이미 예약된 시간입니다"

        return f"{patient_name} : {hour}시: {reason}"

    pass

def show_appointments():
    """
    현재 예약 현황을 보기 좋게 출력합니다.

    Returns:
        None: 예약 현황을 출력만 함
    """
    # 여기에 코드를 작성하세요
    if not appointments:
        print("예약된 환자가 없습니다.")
        return

    for appointment in appointments:
        time = appointment["time"]
        patient = appointment["patient"]
        print(f"{time}시: {patient}")
    pass

test_requests = [
    ("김환자", 10),    # 정상 예약
    ("이환자", 10),    # 중복 시간
    ("박환자", 12),    # 점심시간
    ("정환자", 20),    # 운영시간 외
    ("최환자", 14)     # 정상 예약
]

print("=== 예약 처리 결과 ===")
for patient_name, hour in test_requests:
    result = add_appointment(patient_name, hour)
    print(result)

print("\n=== 현재 예약 현황 ===")
show_appointments()
