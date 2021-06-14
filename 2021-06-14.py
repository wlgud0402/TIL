# 추상클래스는 인스턴스로 만들수 없음 => james = StudentBase() X => 불가능
# 추상클래스를 상속받을 때는 @abstractmethod를 가지고 있는 모든 메서드를 구현해햐함
from abc import *


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass  # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦

    @abstractmethod
    def go_to_school(self):
        pass
