from unittest import TestCase


class TestGeneratorExpressions(TestCase):

    def test_simple_function_decorator(self):

        def hello_goodbye_decorator(func):
            def func_wrapper():
                print('hello')
                func()
                print('goodbye')

            return func_wrapper

        @hello_goodbye_decorator
        def example():
            '''Docstring'''
            print('world')

        example()
        print(example.__name__)
        print(example.__doc__)

    def test_functools_wraps(self):
        from functools import wraps

        def my_decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                print('Calling decorated function')
                return f(*args, **kwargs)
            return wrapper

        @my_decorator
        def example(*args, **kwargs):
            '''Docstring'''
            print('Called example function')
            print(args)
            print(kwargs)

        example('hello', who='world')

        print(example.__name__)
        print(example.__doc__)
