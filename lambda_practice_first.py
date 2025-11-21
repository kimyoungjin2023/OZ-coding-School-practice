# 방법 1: 일반 함수 방식
def check_fever(temperature):
  # if temperature >= 37.5:
  #   return "발열"
  # else:
  #   return "정상"
  return "발열" if temperature >= 37.5 else "정상"

# 방법 2: 람다함수 방식
check_fever_lambda = lambda temperature : "발열" if temperature >= 37.5 else "정상"

print(check_fever(36.5))           # "정상"
print(check_fever(37.8))           # "발열"

print("=" * 30)

print(check_fever_lambda(38.2))    # "발열"
print(check_fever_lambda(36.9))    # "정상"
