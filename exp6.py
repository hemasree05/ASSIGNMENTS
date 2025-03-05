class MyCustomException(Exception):
    def __init__(self, message="This is a custom exception!"):
        super().__init__(message)

try:
    raise MyCustomException("Something went wrong!")
except MyCustomException as e:
    print("Caught Exception:", e)
