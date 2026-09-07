[README.md](https://github.com/user-attachments/files/31904988/README.md)
# Automate the Boring Stuff with Python: Practice Code

Practice scripts written while working through *Automate the Boring Stuff with Python, 3rd Edition* by Al Sweigart. Each file targets a specific concept from the book: functions, scope, exceptions, loops, and a few small games built to apply them.

No external dependencies. Every script uses only the Python standard library, so you can clone and run them directly.

## Requirements

- Python 3.8 or later
- No `pip install` needed

## How to run

Clone the repo and run any file directly:

```bash
git clone https://github.com/fahim6a/Automate-boring-stuff-with-python-3rd-edition-book-practice-code.git
cd Automate-boring-stuff-with-python-3rd-edition-book-practice-code
python3 <filename>.py
```

For example:

```bash
python3 rock_paper_scissors.py
```

## Files in this repo

| File | Topic | What it does |
|---|---|---|
| `hellofunc.py` | Functions, arguments vs. parameters, return values | Defines a function that returns a different string depending on which number it's given |
| `funcpart2.py` | The call stack | Chains five functions together to show call order vs. return order |
| `local_global_scope.py` | Local and global scope, the `global` keyword | Compares variables that live inside a function against ones shared across the whole program |
| `exception_handeling.py` | `try` / `except` | Handles `ZeroDivisionError` so a bad input doesn't crash the program |
| `collatz_sequence.py` | Loops, recursion-free math, `try` / `except ValueError` | Runs the Collatz conjecture on a user-supplied number until it reaches 1 |
| `guess_the_number.py` | `for` loops, `range()`, `random`, `break` | A number-guessing game with a limited number of attempts and "too high / too low" hints |
| `rock_paper_scissors.py` | Nested `while` loops, `sys.exit()`, `random` | A playable rock-paper-scissors game against the computer, with a running win/loss/tie tally |
| `spike.py` | Infinite loops, `KeyboardInterrupt`, `time.sleep()` | Prints a growing-and-shrinking bar animation until the user presses Ctrl+C |
| `zigzag.py` | Infinite loops, `KeyboardInterrupt` | Prints a zigzag pattern that shifts indentation back and forth |

## Notes

- `blank.py` and `tempCodeRunnerFile.py` are scratch/temp files left over from the editor's "Run Code" feature and aren't meant to be read as examples.
- Some scripts contain comments written while working through the book's exercises. They're left in intentionally as a study log, not cleaned up for presentation.

## About the book

*Automate the Boring Stuff with Python* teaches practical Python by building small, useful programs rather than focusing purely on syntax. This repo tracks progress through the early chapters: functions, flow control, and exception handling.

## License

MIT. See [LICENSE](./LICENSE).
