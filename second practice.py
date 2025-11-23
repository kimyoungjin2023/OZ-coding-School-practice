age_from_chart = "65"    # 차트에서 가져온 나이 (문자열)
age_calculated = 65      # 계산으로 구한 나이 (숫자)

print(age_from_chart == age_calculated)        # 예상 결과: false
print(type(age_from_chart) == type(age_calculated))  # 예상 결과: false
print(int(age_from_chart) == age_calculated)   # 예상 결과: true
print(type(age_from_chart) == str)             # 예상 결과:true
