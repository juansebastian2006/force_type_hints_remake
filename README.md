# What is it ❔
If you are totally a beginner in python, wouldn't recommend you to understand this code yet.
In python we have something called type hints, they are hints for variables on parameters,
which we may indicate the exact type we are expecting to. 

Example

```py

def add_numbers(a: int, b: int) -> int:
  return n1 + n2
```

Here we are telling python to receive two arguments whose types are Integers. `-> int` means it's returning an integer value

Anyways, for more info, visit here: https://realpython.com/python-type-checking/ \n
Would really like if you read full explanation from there. You learn❗ 😄
 
## How does it work?

```py

@forced_types
def my_func(name: str):
    print(f"hello {name}!")
```

This is the syntax to use it.
