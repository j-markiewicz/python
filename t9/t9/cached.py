from __future__ import annotations
from typing import TypeVar, Generic, Callable


T = TypeVar("T")


class Cached(Generic[T]):
    """Cache a `T`, initializing it once on first access

    >>> long_computation = lambda: print("Initializing ...")
    >>> x = Cached(long_computation) # This is fast
    >>> a = x.get() # This calls `long_computation`
    Initializing ...
    >>> b = x.get() # This returns the cached value (without another call)
    >>> assert a is b
    """

    inner: T | None
    initializer: Callable[[], T] | None

    def __init__(self, initializer: Callable[[], T]) -> None:
        self.initializer = initializer

    def get(self) -> T:
        """Get the cached value or create it on first call"""

        if self.initializer is not None:
            self.inner = self.initializer()
            self.initializer = None

        return self.inner
