from abc import ABC, abstractmethod  # Import ABC and abstractmethod

# Define an abstract class
class AbstractClass(ABC):

    def non_abstract_method(self):
        """This is a non-abstract method"""
        print("This is a non-abstract method from AbstractClass.")

    @abstractmethod
    def abstract_method(self):
        """Abstract method that must be overridden"""
        pass

# Create a subclass to implement the abstract method
class ChildClass(AbstractClass):

    def abstract_method(self):
        print("Abstract method implemented in ChildClass.")

# Create an instance of the child class
obj = ChildClass()
obj.abstract_method()        # Calls the overridden abstract method
obj.non_abstract_method()    # Calls the non-abstract method