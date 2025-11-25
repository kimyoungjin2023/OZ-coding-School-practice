import matplotlib.pyplot as plt
import numpy as np

# 입력 데이터: 0시간부터 5시간까지
time = np.linspace(0, 5, 100)

# 지수 함수 정의
def bacteria_growth_model(t):
    # 2 * e^(t) -> 초기 2마리, 시간당 증식률
    return 2 * np.exp(t)

# 시간에 따른 박테리아 수 예측
bacteria_count = bacteria_growth_model(time)


# TODO: 증식 속도가 느린 새로운 지수 함수 정의
def bacteria_growth_growth_model(t):
    # 2 * e^(0.5 t) -> 초기 2마리, 시간당 증식률
    return 2 * np.exp(0.5 * t)


# TODO: 새로운 모델로 박테리아 수 예측
slow_bacteria_count = bacteria_growth_growth_model(time)

# 두 그래프 함께 그리기
plt.plot(time, bacteria_count, color='green', linewidth=3, label='일반 박테리아')
plt.plot(time, slow_bacteria_count, color='orange', linewidth=3, linestyle='--', label='저속 증식 박테리아')
plt.title('지수 모델 비교: 박테리아 증식 속도')
plt.xlabel('시간 (시간)')
plt.ylabel('박테리아 수')
plt.legend()
plt.show()
