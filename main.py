
from typing import (
    List,
    Any,
    Tuple,
    Callable,
    Coroutine,
    Union,
    Dict,
    get_type_hints,
    Optional
)
import inspect



def forced_types(func: Callable):

    type_hints = inspect.getfullargspec(func)

    for arg in type_hints.args:
        if arg not in type_hints.annotations:
            raise Exception(f'{arg} does not have type_hints')

    for kwarg in type_hints.kwonlyargs:
        if kwarg not in type_hints.annotations:
            raise Exception(f'{kwarg} does not have type_hints')

    def call_function(*args: Optional[Tuple[Any, ...]], **kwargs: Dict[Any, Any]) -> Coroutine:

        args_annotation: List[Tuple[str, Any]] = []
        # a tuple, first value is the variable name, and the second the type
        
        kwargs_annotation: List[Tuple[str, Any]] = []
        # same situation

        for arg_name in type_hints.args:
            args_annotation.append(
                (arg_name, type_hints.annotations.get(arg_name))
            )

        for kwarg_name in type_hints.kwonlyargs:
            kwargs_annotation.append(
                (kwarg_name, type_hints.annotations.get(kwarg_name))
            )

        zipped_args = list(zip(args, args_annotation))
        # we zip, the values with the tuples
        
        zipped_kwargs = list(zip(kwargs.values(), kwargs_annotation))
        

        new_args = []
        # we have the values already defined. However we have not checked if those values are in the correct type

        for value, (tuple_) in zipped_args:
            if isinstance(value, tuple_[1]):
                # remember our tuple look like this: (value, (name, type))
                new_args.append(tuple_[1](value))
            else:
                raise ValueError(f"{tuple_[0]} has to be of type {tuple_[1]}")

        new_kwargs = {}

        for value, (tuple_) in zipped_kwargs:
            if isinstance(value, tuple_[1]):
                new_kwargs[tuple_[0]] = tuple_[1](value)
            else:
                raise ValueError(f"{tuple_[0]} has to be of type {tuple_[1]}")

        return func(*new_args, **new_kwargs)

    return call_function
