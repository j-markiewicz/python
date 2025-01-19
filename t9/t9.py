from t9 import Language, Character, t9
import argparse


parser = argparse.ArgumentParser(description="Decode T9 inputs into words")

parser.add_argument(
    "-l",
    "--language",
    default=Language.PL,
    type=lambda s: Language[s],
    choices=(Language.PL, Language.EN),
    help="the language of the dictionary to use (default PL)",
)

parser.add_argument(
    "-n",
    default=3,
    type=int,
    help="the number of words to find (default 3)",
)

parser.add_argument(
    "input",
    nargs="*",
    help="the input as a string of digits (leave empty for interactive mode)",
)

args = parser.parse_args()


if len(args.input) == 0:
    # Pre-initialize dictionary
    t9([], args.language)

    while True:
        try:
            chars = input("> ")
            chars = list(map(lambda c: Character.from_input(c), chars))
            print(", ".join(t9(chars, args.language, args.n)))
        except ValueError:
            print("Invalid input - use digits 1-9 only")
        except KeyboardInterrupt:
            break
else:
    for chars in args.input:
        chars = list(map(lambda c: Character.from_input(c), chars))
        print(", ".join(t9(chars, args.language, args.n)))
