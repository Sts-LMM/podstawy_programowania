class SpecifiedClass:
    class_variable = "Class Level Variable"

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

instance = SpecifiedClass("Instance Level Value")

print("Namespace of the instance:")
print(dir(instance))

print("\nAttributes and methods of the instance:")
for attribute in dir(instance):
    print(attribute)
