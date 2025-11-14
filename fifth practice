doctor = {"name": "박의사", "department": "내과", "experience": 5}

# 1. "license" 정보 추가 후 출력
doctor["license"] = "전문의"
print(f"면허 추가 후: {doctor}")

# 2. "experience" 수정 후 출력
doctor["experience"] = "6"
print(f"경력 수정 후: {doctor}")

# 3. "specialty" 안전하게 조회 (없으면 "미지정")
check = doctor.get("specialty", "미지정")
print(f"전문분야: {check}")


# 4. "license" 존재 여부 확인 후 출력
check_license = "license" in doctor
print(f"면허 정보 존재: {check_license}")

# 5. "department" 삭제하고 삭제된 값 출력
delete = doctor.pop("department")
print(f"삭제된 부서: {delete}")
print(f"최종 의료진 정보: {doctor}")
