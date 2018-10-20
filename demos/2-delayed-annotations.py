# https://www.python.org/dev/peps/pep-0526/

# from __future__ import annotations
# from typing import get_type_hints

class Bar:
    pass


class Foo:
    def __init__(self, bar: Bar) -> None:
        self.bar = bar

    @classmethod
    def from_bar(cls, bar) -> 'Foo':  # "forward reference" to Foo
        return cls(bar)


foo = Foo.from_bar(Bar())
print(f'foo     => {foo}')
print(f'foo.bar => {foo.bar}')

print()

print(f'Foo.__init__.__annotations__ => {foo.__init__.__annotations__}')
print(f'Foo.from_bar.__annotations__ => {foo.from_bar.__annotations__}')

print()

# print(f'get_type_hints => {get_type_hints(foo.from_bar)}')
