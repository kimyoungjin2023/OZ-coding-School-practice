import matplotlib.pyplot as plt
import numpy as np

# 입력 데이터: -10부터 10까지의 위험도 점수
risk_scores = np.linspace(-10, 10, 100)

# 시그모이드 함수 정의
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 위험도 점수를 확률로 변환
probabilities = sigmoid(risk_scores)

# TODO: 환자들의 위험도 점수
patient_scores = np.array([-7, 0.5, 4.8])

# TODO: 각 점수를 확률로 변환

result = sigmoid(patient_scores)

print(f"위험조 점수 -7.0 : {result[0]*100:.2f}%")
print(f"위험조 점수 0.5 : {result[1]*100:.2f}%")
print(f"위험조 점수 4.8 : {result[2]*100:.2f}%")

# TODO: 결과 출력 (예: 위험도 점수 0.0  ->  질병 확률: 0.00%)
plt.plot(patient_scores, result, color='orange', linewidth=3)
plt.axhline(y=0.5, color='grey', linestyle='--', label='확률 0.5 (결정 경계)') # 0.5 기준선 추가
plt.title('시그모이드 함수: 위험도 점수를 확률로 변환')
plt.xlabel('AI가 계산한 위험도 점수')
plt.ylabel('질병이 있을 확률 (0.0 ~ 1.0)')
plt.legend()
plt.show()
