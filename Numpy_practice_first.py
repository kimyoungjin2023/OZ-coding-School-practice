import numpy as np

my_vector = np.array([120, 42, 165])
my_friend_vector = np.array([[110, 40, 178], [130, 45, 168]])
team_matrix = np.vstack([my_vector, my_friend_vector])
#team_matrix_1 = np.concatenate([my_vector, my_friend_vector]) 차원이 같이야지 np.concatenate 사용가능 지금은 차원이 다르므로 사용 불가능
team_matrix

print(f"우리팀 행렬 : \n{team_matrix}")
print(f"\n두번째 사람의 모든 정보 : {team_matrix[1]}")
print(f"\n세 사람 모두의 키 정보 : {team_matrix[:,2]}")
