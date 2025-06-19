class Foo:
    def __init__(self, x=None):
        self._x = x

    @property # Decorator para definir uma propriedade.
    def x(self):
        return self._x or 0

    @x.setter # Decorator para definir o setter da propriedade.
    def x(self, value):
        self._x += value

    @x.deleter # Decorator para definir o deleter da propriedade.
    def x(self):
        self._x = 0

if __name__ == "__main__":
    foo = Foo(10)
    print(foo.x)
    del foo.x
    print(foo.x)
    foo.x = 10
    print(foo.x)
