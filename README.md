# Recursive sodoku solver in Python

## Usage

Clone or download this repo

```console
$ git clone https://github.com/vxxce/python-sodoku-solver.git
```

Test it with the demo board as input

```console
$ cd python-sodoku-solver/
$ python3 solve

             I N P U T                          S O L V E D

   +-----------------------------+    +-----------------------------+
   |  +-----------------------+  |    |  +-----------------------+  |
   |  | 8 . . | . . . | . . . |  |    |  | 8 1 2 | 7 5 3 | 6 4 9 |  |
   |  | . . 3 | 6 . . | . . . |  |    |  | 9 4 3 | 6 8 2 | 1 7 5 |  |
   |  | . 7 . | . 9 . | 2 . . |  |    |  | 6 7 5 | 4 9 1 | 2 8 3 |  |
   |  +-----------------------+  |    |  +-----------------------+  |
   |  | . 5 . | . . 7 | . . . |  |    |  | 1 5 4 | 2 3 7 | 8 9 6 |  |
   |  | . . . | . 4 5 | 7 . . |  |    |  | 3 6 9 | 8 4 5 | 7 2 1 |  |
   |  | . . . | 1 . . | . 3 . |  |    |  | 2 8 7 | 1 6 9 | 5 3 4 |  |
   |  +-----------------------+  |    |  +-----------------------+  |
   |  | . . 1 | . . . | . 6 8 |  |    |  | 5 2 1 | 9 7 4 | 3 6 8 |  |
   |  | . . 8 | 5 . . | . 1 . |  |    |  | 4 3 8 | 5 2 6 | 9 1 7 |  |
   |  | . 9 . | . . . | 4 . . |  |    |  | 7 9 6 | 3 1 8 | 4 5 2 |  |
   |  +-----------------------+  |    |  +-----------------------+  |
   +-----------------------------+    +-----------------------------+
```

Or, provide your own input

```console
$ vim solve/board.py
```

Provide sodoku board structured as a list with ```None``` for empty cells
```python
#!/usr/bin python3

board = [
  1,    None, None, None, 9,    None, None, None, None,
  None, None, None, None, None, None, None, None, None,
  None, 3,    None, None, None, None, None, None, None,
  None, None, None, None, None, None, None, None, None,
  None, None, None, None, None, None, None, None, None,
  None, None, None, None, None, None, None, None, None,
  None, None, None, None, None, None, None, None, None,
  None, None, None, None, None, 4,    None, None, None,
  None, None, None, None, None, None, None, None, None,
] 
```

And do it again?

```console
$ python3 solve
```
