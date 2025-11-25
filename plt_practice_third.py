import matplotlib.pyplot as plt
import numpy as np

training_sessions = np.linspace(1, 100, 100)

# 로그 함수 정의
def strength_gain_model(sessions):
    # 10 * log(sessions) -> 기본 근력 0에서 시작, 훈련에 따라 증가
    return 10 * np.log(sessions)

# 운동 횟수에 따른 근력 예측
strength_level = strength_gain_model(training_sessions)

# TODO: 재능 있는 선수의 로그 함수 정의
def talented_strength_gain_model(sessions):
    return 20 * np.log(sessions)

# TODO: 새로운 모델로 근력 예측
strength_gain_upgrade = talented_strength_gain_model(training_sessions)

# 두 그래프 함께 그리기
plt.plot(training_sessions, strength_level, color='purple', linewidth=3, label='일반 선수')
plt.plot(training_sessions, strength_gain_upgrade, color='skyblue', linewidth=3, linestyle='--', label='재능 있는 선수')
plt.title('로그 모델 비교: 선수별 근력 증가 곡선')
plt.xlabel('운동 횟수')
plt.ylabel('근력 레벨')
plt.legend()
plt.show()
