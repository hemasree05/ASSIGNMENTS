from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def non_abstract_method(self):
        """This is a non-abstract method"""
        print("This is a non-abstract method from AbstractClass.")

    @abstractmethod
    def abstract_method(self):
        """Abstract method that must be overridden"""
        pass

class AnotherChildClass(AbstractClass):
    
    def abstract_method(self):
        print("Abstract method implemented in AnotherChildClass.")

    def call_non_abstract(self):
        self.non_abstract_method()
obj = AnotherChildClass()
obj.call_non_abstract()