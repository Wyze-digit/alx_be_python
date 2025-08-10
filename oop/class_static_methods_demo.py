# Understand the use of @staticmethod for functions that perform a task in isolation, 
# without needing access to class or instance-specific data.git 

# class_static_methods_demo.py

class Calculator:
    # Class attribute (shared by all instances and accessible via the class itself)
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method:
        - Does not use 'self' or 'cls'.
        - Behaves like a normal function but belongs to the class's namespace.
        - Useful for operations that don't depend on class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method:
        - Receives the class as the first parameter ('cls').
        - Can access and modify class-level attributes.
        - Here, we print the class attribute before performing multiplication.
        """
        # Accessing the class attribute via cls
#        print(cls.calculation_type) 
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


