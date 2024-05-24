class MyClass:
    class_variable = "Hello, World!"

    def __init__(self, value):
        self.instance_variable = value

    def instance_method(self):
        return "This is an instance method."

    @classmethod
    def class_method(cls):
        return "This is a class method."

    @staticmethod
    def static_method():
        return "This is a static method."

print("Namespace of MyClass:")
print(dir(MyClass))

my_instance = MyClass("Some value")

print("\nNamespace of my_instance:")
print(dir(my_instance))
