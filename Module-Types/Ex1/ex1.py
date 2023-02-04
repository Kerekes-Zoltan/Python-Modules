import types

def function():
    return 1

print(isinstance(function, types.FunctionType))
print(isinstance(function, types.LambdaType))
print(isinstance(lambda x: x, types.FunctionType))
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance(max, types.FunctionType))
print(isinstance(max, types.LambdaType))
print(isinstance(abs, types.FunctionType))
print(isinstance(abs, types.LambdaType))