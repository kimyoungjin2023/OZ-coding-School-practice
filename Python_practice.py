import random

lunch_menu = ["된장찌개", "김치볶음밥", "비빔면", "제육볶음", "돈까스"]
dinner_menu = ["삼겹살", "피자", "파스타", "곱창", "치킨"]

choice = input("점메추? or 저메추?")

if choice == "점메추":
  lunch_menu_choice = random.choice(lunch_menu)
  print(f"점메추 : {lunch_menu_choice}")
elif choice == "저메추":
  dinner_menu_choice = random.choice(dinner_menu)
  print(f"저메추 : {dinner_menu_choice}")
else:
  print("잘못입력되었습니다")
