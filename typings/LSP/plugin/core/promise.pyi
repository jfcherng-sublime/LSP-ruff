from _typeshed import Incomplete
from typing import Callable, Generic, Protocol, TypeVar

T = TypeVar('T')
S = TypeVar('S')
TExecutor = TypeVar('TExecutor')
T_contra = TypeVar('T_contra', contravariant=True)
TResult = TypeVar('TResult')

class ResolveFunc(Protocol[T_contra]):
    def __call__(self, resolve_value: T_contra) -> None: ...

FullfillFunc: Incomplete
ExecutorFunc = Callable[[ResolveFunc[T]], None]
PackagedTask: Incomplete

class Promise(Generic[T]):
    @staticmethod
    def resolve(resolve_value: S) -> Promise[S]: ...
    resolver: Incomplete
    @staticmethod
    def packaged_task() -> PackagedTask[S]: ...
    @staticmethod
    def all(promises: list[Promise[S]]) -> Promise[list[S]]: ...
    resolved: bool
    mutex: Incomplete
    callbacks: Incomplete
    def __init__(self, executor_func: ExecutorFunc[T]) -> None: ...
    def then(self, onfullfilled: FullfillFunc[T, TResult]) -> Promise[TResult]: ...
