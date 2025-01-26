# [T9](https://en.wikipedia.org/wiki/T9_(predictive_text))

## Problem

Na urządzeniach z małą ilością klawiszy (jak n.p. telefonach komórkowych bez ekranu dotykowego) nie można każdej literze przyznać osobnego klawiszu. Problem ten można rozwiązać w dwa sposoby: Wymagać kilkurazowego kliknięcia klawisza dla różnych liter (metoda [multi-tap](https://en.wikipedia.org/wiki/Multi-tap)) lub zgadywanie litery na podstawie słownika (metoda [T9](https://en.wikipedia.org/wiki/T9_(predictive_text)) i podobne). Program ten implementuje motodę T9 dla języka polskiego i angielskiego.

## Architektura

Projekt jest podzielony na dwie części:

- Biblioteka (w [`t9/`](./t9/))
- Przykładowy program (w [`t9.py`](./t9.py))

## Implementacja

### `decode()`

Funkcja `decode` zwraca *n* najlepiej pasujące słowa dla podanago wejścia w podanym języku (lub dla podanego słownika) dla metody wejścia [*T9*](https://en.wikipedia.org/wiki/T9_(predictive_text)).
Zwrócone słowa są najbardziej popularnymi słowami odpowiadającymi wejściu użytkownika ze słownika.

Implementacja (znajdująca się w pliku `t9/t9.py`) działa w następujący sposób, bazując na mapie słów:

- ```py
    def decode(
        input: Sequence[Character], lang_or_wordmap: Language | WordMap, n: int = 3
    ) -> tuple[str]:
    ```

    Definicja funkcji.

- ```py
    if isinstance(lang_or_wordmap, Language):
        words = _WORDMAPS[lang_or_wordmap].get()
    else:
        words = lang_or_wordmap

    if len(input) == 0 or n <= 0:
        return ("", "", "")
    ```

    Wybranie odpowiedniego słownika oraz zwrócenie pustych słów dla pustego wejścia.

- ```py
    for char in input:
        if words is None:
            break

        words = words.next[char]
    ```

    Przejście przez słownik: dla każdego znaku wejścia znaleziona jest odpowiednia podmapa (jeśli istnieje).

- ```py
    words = words.content if words is not None else []
    return tuple([*words, "", ""][:3])
    ```

    Zwrócenie wyniku: trzy pierwsze słowa (lub puste ciągi znaków jeśli nie ma wystarczająco słów) są zwrócone.

### Mapa słów

Dla słowników w funkcji `decode` została użyta klasa `WordMap`, która zawiera słowa posortowane według popularności i skategoryzowane według klawiszy T9.

Klasa `WordMap` implementuje dziewięciorzędne drzewo *trie* i jest zdefiniowana jak poniżej:

```py
class WordMap:
    next: dict[Character, None | WordMap]
    content: list[str]
```

`WordMap` ma w `next` jedną wartość dla każdego z klawiszy, zawierającą podmapę jeśli istnieją odpowiednie słowa w słowniku źródłowym. Dodatkowo jest również pole `content`, które zawiera listę słów znajdujących się w (pod)mapie.

Mapa jest skonstruowana jak drzewo, gdzie przechodząc do następnej podmapy można znaleźć słowa mające następną literę odpowiadającą tej podmapie. W ten sposób odwiedzając *N* map można znaleźć wszystkie słowa w słowniku zaczynające się na *N*-literowe słowo odpowiadające *N*-elementowemu wejściu użytkownika.

Cała mapa słów wraz z podmapami jest tworzona przez metodę statyczną `new` (`__init__` jedynie inicjalizuje jedną (pod)mapę):

- ```py
    @staticmethod
    def new(words: Iterable[str]) -> WordMap:
        res = WordMap()
    ```

    Definicja metody, zainicjalizowanie początkowo pustego wyniku.

- ```py
    for word in words:
        chars = list(map(Character.from_char, word))

        if any(map(lambda c: c is None, chars)):
            continue

        res.content.append(word)
        current = res

        for char in chars:
            next = current.next[char]

            if next is None:
                current.next[char] = WordMap()
                next = current.next[char]

            current = next
            current.content.append(word)
    ```

    Dla każdego słowa w liście słów (posortowanej od najbardziej do najmniej częstego/ważnego):
    1. Słowo jest skonwertowane na ciąg znaków T9 (`Character`). Jeśli w słowie są znaki, których nie można wypisać przy pomocy klawiatury T9 (`Character.from_char` zwróciło `None`), słowo jest ignorowane.
    2. Słowo jest dodane do listy słów w korzeniu.
    3. Słowo jest dadane do mapy słów znak po znaku, przechodząc przez drzewo i tworząc nowe poddrzewa jeśli to jest potrzebne.

- ```py
    return res
    ```

    Zwrócenie wyniku.

## Wykonanie i testowanie

Program można wykonać interaktywnie (`python t9.py [--language {EN, PL}] [-n N]`) lub nie (`python t9.py [--language {EN, PL}] [-n N] INPUT...`), n.p. `python t9.py --language EN -n 1 43556` (co powinno wypisać słowo *hello*).
W trybie interaktywnym, program można zakończyć przy użyciu <kbd>CTRL</kbd>+<kbd>C</kbd>.

Kod również można użyć jako bibliotekę: `import t9`.
Przykładem użycia jest program w [`t9.py`](./t9.py).

Bibliotekę można przetestować przy użyciu modułu `unittest`: `python -m unittest`.

## Listy słów

Listy słów (w `t9/words-*.txt`) pochodzą z <https://github.com/IlyaSemenov/wikipedia-word-frequency> i są oparte na danych z [Wikipedii](https://wikipedia.org). Listy są skrócone i zawierają tylko słowa użyte w co najmniej 100 artykułach, i są używane na warunkach licencji [MIT](https://github.com/IlyaSemenov/wikipedia-word-frequency/blob/3354c90d8cc1b4f53f4b57479d15da26d303fc69/LICENSE) i [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.pl)
