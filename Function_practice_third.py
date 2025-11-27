def classify_blood_pressure(systolic_pressure):
    # 코드 작성
    if systolic_pressure < 120:
      return "정상"
    elif systolic_pressure < 140:
      return "고혈압 전단계"
    elif systolic_pressure < 160:
      return "1기 고혈압"
    else:
      return "2기 고혈압" 
    pass

print(classify_blood_pressure(110))  # 정상
print(classify_blood_pressure(130))  # 고혈압 전단계
print(classify_blood_pressure(150))  # 1기 고혈압
print(classify_blood_pressure(170))  # 2기 고혈압
