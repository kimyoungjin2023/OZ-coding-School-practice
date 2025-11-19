#클래스 (붕어빵 틀 설계)
class FishBread:
  factory = "벤타" #클래스 변수
  #이 클라스로 만들어진 기계가 만든 붕어빵의 총 갯수
  total_baked = 0

  #생성자 함수
  def __init__(self, dough = "밀가루 반죽", filling = "팥", roast = "웰던"):
    """
    Args:
      dough : 반죽종류 (밀가루 반죽 / 쌀 반죽 / 참쌀 반죽)
      filling : 속 내용 (팥 / 슈크림 / 피자 / 고구마)
      roast : 굽기 정도 (레어 / 미디움 / 웰던)
    """
    self.dough = dough # 인스턴스 변수
    self.filling = filling
    self.roast = roast
    self.total_made = 0 # 하나의 기계에서 구운 붕어빵 총 갯수
 # 붕어빵 굽는 매서드
  def bake(self, count=1):
    """
    Args:
      count : 붕어빵 구울 갯수
    """
    # 0. 몇개 주문 받았는지 출력
    print(f"{count}개 주문 완료!")

    # 1. 반죽 종류, 속 내용, 굽기 정도 출력
    print(f"{self.dough}에 {self.filling}을 넣고 {self.roast}굽기로 굽는중...")

    # 2. 구워준 총 붕어빵 갯수를 total_made에 추가
    self.total_made += count

    #2-1 클래스 변수애 구운 갯수 추가
    FishBread.total_baked += count

    # 3. 구워준 붕어빵 변환(list[dict])
    baked_fish_bread = []

    for i in range(1, count + 1): # 1번 순회 count = 1이기 때문에
      new_item = {
           "dough": self.dough,
          "filling": self.filling,
          "roast": self.roast
      }
      baked_fish_bread.append(new_item)
    #반환
    return baked_fish_bread

  #구어진 총 붕어빵 갯수 반환 함수
  def get_total_made(self):
    return self.total_made

#객체 (인스턴스)생성
팥붕어빵_기계 = FishBread()
슈크림붕어빵_기계 = FishBread(filling = "슈크림")

팥붕어빵_기계.total_made # bad
팥붕어빵_기계.get_total_made() # good

팥붕어빵_기계.bake(3)
슈크림붕어빵_기계.bake(2)

팥붕어빵_기계.bake(13)
슈크림붕어빵_기계.bake(11)

팥붕어빵_기계.get_total_made()

print(팥붕어빵_기계.factory)
print(슈크림붕어빵_기계.factory)

print(팥붕어빵_기계.total_baked)
print(슈크림붕어빵_기계.total_baked)
