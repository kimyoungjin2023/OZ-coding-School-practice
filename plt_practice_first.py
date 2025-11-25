import matplotlib.pyplot as plt

# 입력 데이터: 1시간부터 10시간까지 100개의 점으로 부드럽게 표현
sleep_hours = np.linspace(1, 10, 100)

# 선형 함수 정의: y = -5x + 100
def stress_linear_model(x):
    return -5 * x + 100
print(sleep_hours)
# 모델로 스트레스 지수 예측
stress_level = stress_linear_model(sleep_hours)
stress_level


# TODO: 새로운 선형 함수 정의
def stress_new_linear_model(x):
  return -8 * x + 100


# TODO: 새로운 모델로 스트레스 지수 예측
new_stress_level = stress_new_linear_model(sleep_hours)

# 두 그래프 함께 그리기
plt.plot(sleep_hours, stress_level, color='blue', linewidth=3, label='기존 모델 (시간당 -5)')
plt.plot(sleep_hours, new_stress_level, color='red', linewidth=3, linestyle='--', label='고강도 운동 모델 (시간당 -8)')
plt.title('선형 모델 비교: 수면 시간과 스트레스 지수')
plt.xlabel('수면 시간 (시간)')
plt.ylabel('예측 스트레스 지수')
plt.legend() # label 옵션을 화면에 표시
plt.show()
