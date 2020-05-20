# shelvecache
A simple python function cache in a shelve. 

## Usage

``` python
from shelvecache import shelvecache

@shelvecache()
def foo(x):
    import time
    time.sleep(x)
    return x*2

foo(2)  # sleep 2 seconds and return 4
foo(2)  # return 4 withnot waiting
```

## TODO:
- [ ] Async support.
- [ ] Limit maxsize.
- [ ] Tests.
- [ ] Example.