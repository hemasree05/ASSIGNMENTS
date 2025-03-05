from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def non_abstract_method(self):
        """This is a non-abstract method"""
        print("This is a non-abstract method from AbstractClass.")

    @abstractmethod
    def abstract_method(self):
        """Abstract method that must be overridden"""
        pass


class ChildClass(AbstractClass):

    def abstract_method(self):
        print("Abstract method implemented in ChildClass.")


obj = ChildClass()
obj.abstract_method()
obj.non_abstract_method()   