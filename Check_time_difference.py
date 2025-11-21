import time

start_time = time.time()

a = 170
b = 120

c = a - b

end_time = time.time()
print(f"정수형 시간 비교 {end_time - start_time}")

start2_time = time.time()

a_f = 170.000
b_f = 120.000

c_f = a_f - b_f

end2_time = time.time()

print(f"실수형 시간 비교 {end2_time - start2_time}")

