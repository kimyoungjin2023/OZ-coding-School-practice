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
#1
팥붕어빵_기계 = FishBread()
슈크림붕어빵_기계 = FishBread(filling = "슈크림")

#2
슈크림붕어빵 = FishBread("","슈크림","")
슈크림붕어빵.filling


# 1버은 기본값을 유지한채 필요한 것만 바뀜 2번은 기본값이 사라지고 빈 값("")으로 덮어짐 → 대부분의 상황에서는 오류나 버그 원인이 됨
# 2번 방식은 매개변수 위치를 전부 기억해야 함, 빈 문자열 전달은 오타와 다름없음, 실수 확률 매우 높음 (단점) 1번 방법이 더 좋은 방법이다.
