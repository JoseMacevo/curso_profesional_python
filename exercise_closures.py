from typing import TypeVar, Generic


T = TypeVar('T')


def make_division_by(n: int) -> Generic[T]:   # Funcion principal, o envolvente
    def numerator(x: int) -> float:  # Funcion anidada (nested_function)
        assert n != 0, "You can't divide by zero."
        return x/n  #  Funcion trabajando con un valor de un scope superior.
    return numerator #  Devolucion del resultado de la funcion anidada.


def main():
    divided_by_two = make_division_by(2)
    print(divided_by_two(10))


if __name__ == '__main__':
    main()
