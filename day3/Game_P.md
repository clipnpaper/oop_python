# 문제 4. 잘못된 설계 고치기

한 학생이 다음과 같이 코드를 작성했습니다.

```
class Weapon:
    def __init__(self, power):
            self.power = power

class Character(Weapon):   # 캐릭터가 무기를 상속?
   def __init__(self, name, power):
           super().__init__(power)
                self.name = name
```

1. 이 설계가 어색한 이유를 IS-A / HAS-A 관점에서 한 문장으로 설명하세요.

 → 캐릭터가 무기를 상속하게 되면서, 캐릭터가 여러 개의 무기 중 하나로 설계가 됩니다(IS-A).

2. 게임 도중 무기를 바꾸고 싶을 때, 위 설계의 문제점은 무엇인가요? 

 → 상속받은 무기를 교체하게 되면 캐릭터 클래스도 교체된다.

3. 구성을 사용하도록 코드를 고쳐 보세요.

```
class Weapon:
    def __init__(self, power):
            self.power = power

class Character(GameObject):   # 캐릭터가 무기를 상속?
   def __init__(self, name, power):
           super().__init__(power)
                self.name = name
                self.weapon = Weapon("무기")
```