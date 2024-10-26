# Zestaw 3

## Zadanie 1

[Podany kod](./1.py) nie jest poprawny składniowo, ponieważ na [linii 7](./1.py#L7) *statement* `if` znajduje się bezpośrednio na początku bloku.
Brakuje tu przejścia do nowej linii:

```diff
- for i in "axby": if ord(i) < 100: print (i)
+ for i in "axby":
+     if ord(i) < 100: print (i)
```

Alternatywnie, gdyby (podobnie do [linii 9](./1.py#L9)) użyty został `if` w postaci *expression*, to kod byłby poprawny składniowo:

```diff
- for i in "axby": if ord(i) < 100: print (i)
+ for i in "axby": print(i) if ord(i) < 100 else None
```

Średniki i nawiasy użyte w początkowej sekcji kodu nie są niepoprawne, ale (z wyjątkiem pierwszego, który jest wymagany, chodź mógłby być zastępiony przez przejście do nowej linii) nie są one potrzebne:

```diff
- x = 2; y = 3;
+ x = 2
+ y = 3

- if (x > y):
-     result = x;
+ if x > y:
+     result = x
  else:
-     result = y;
+     result = y
```

## Zadanie 2

Na [pierwszej linii](2.py#L1) podanego kodu druga instrukcja przypisuje do zmiennej `L` wynik wywołania `L.sort()`.
Nie jest to koniecznie niepoprawne, ale przez to, że metoda `list.sort` sortuje listę w miejscu i nie zwraca jej, po wykonaniu tego kodu zmienna L będzie zawierała wartość `None`.
Posortowanie listy w zmiennej `L` można osiągnąc wywołaniem `L.sort()` bez przypisania wyniku do zmiennej `L` lub przypisaniem wartości `sorted(L)` do zmiennej `L`.

Na [drugiej linii](2.py#L2) przypisane są do dwóch zmiennych trzy wartości.
Jeśli taka linia kodu zostanie wywołana, interpreter rzuci błąd `ValueError`.

[Trzecia linia](2.py#L3) kodu próbuje przypisać nową wartość do elementu krotki, co nie jest dozwolone w języku python.
Żeby taki kod działał można zmienić `X` na listę lub nadpisać całą wartość `X` nową krotką.

Na [kolejnej linii](2.py#L4) kodu indeksowana jest trójelementowa lista z indeksem 3, co spowoduje wyrzucenie `IndexError`.
Do dodania nowego elementu na daną pozycję listy można użyć metody `insert`.

Na [piątej linii](2.py#L5) kodu jest próba wywołania metody `append` na zmiennej typu `str`, który takiej metody nie posiada.
Metoda o nazwie `append` istnieje n.p. na typie `list`.
Aby dodać znak "w miejscu" na koniec zmiennej typu `str` można użyć operatora `+=`.

[Ostatnia linia](2.py#L6) kodu zawiera wywołanie (poprzez `map`) funkcji dwuargumentowej `pow` z jednym argumentem, co skutkuje błędem `TypeError`.
Jeśli ta linia kodu powinna stworzyć listę zawierającą liczby podniesione do n.p. drugiej potęgi, to możnaby użyć wyrażenia lambda do podania drugiego argumentu do funkcji pow: `L = list(map(lambda n: pow(n, 2), range(8)))`.

## Zadania 3 - 6, 8 - 10

Rozwiązania tych zadań znajdują się w pliku [`main.py`](./main.py).

Testy do rozwiązań są w pliku [`tests.py`](./tests.py).
Można je wykonać z flagą `-v` aby dostać dodatkowe informacje o ich przebiegu.
