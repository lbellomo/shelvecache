# shelvecache
A simple python function cache in a shelve. 
It works for functions and coroutines!

At the moment it is a toy project, for real applications use [joblib.Memory](https://joblib.readthedocs.io/en/latest/generated/joblib.Memory.html#joblib.Memory).

## Usage

``` python
import time

from shelvecache import shelvecache


@shelvecache()
def foo(x):
    time.sleep(x)
    return x*2

foo(2)  # sleep 2 seconds and return 4
foo(2)  # return 4 with not waiting

# also work for coroutines
import asyncio

@shelvecache()
async def bar(x):
    await asyncio.sleep(x)
    return x*2

await bar(3)  # sleep for 3 seconds and return 6
await bar(3)  # return 6 with not waiting

# by default it uses files called "cache" to store things
# in the previous case foo and bar are using the same cache

foo(3)        # return 6 with not waiting
await bar(2)  # return 4 with not waiting

# We can make them use different shelves 
# with the "shelvename" decorator parameter

@shelvecache(shelvename="foo")
def foo(x):
    time.sleep(x)
    return x*2


@shelvecache(shelvename="bar")
async def bar(x):
    await asyncio.sleep(x)
    return x*2

foo(2)        # sleep 2 seconds and return 4
await bar(2)  # this also sleeps for 2 seconds and returns 4
```

## TODO:
- [X] Async support.
- [ ] Limit maxsize.
- [ ] Tests.
- [ ] Example.
