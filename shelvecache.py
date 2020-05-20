import json
import shelve
from functools import wraps
from asyncio import iscoroutinefunction


def dump_args(args: tuple, kwargs: dict) -> str:
    """Util to make hashable function arguments."""
    return json.dumps(args) + json.dumps(kwargs, sort_keys=True)


def shelvecache(shelvename="cache"):
    """
    Decorator to wrap a function with a memoizing callable (like functools.lru_cache). 
    Save the function argument and result in a shelve.

    Parameters
    ----------
    shlevename: str
        Path of the shelve wuere the data will be saved.
    """

    def real_decorator(func_or_cor):
        if iscoroutinefunction(func_or_cor):
            # cor = func_or_cor
            raise NotImplementedError("decorator not implement for corroutine.")
        else:
            func = func_or_cor

            @wraps(func)
            def wrapper(*args, **kwargs):
                index = dump_args(args, kwargs)

                with shelve.open(shelvename) as db:
                    if index in db:
                        return db[index]

                    res = func(*args, **kwargs)
                    db[index] = res
                return res

        return wrapper

    return real_decorator
