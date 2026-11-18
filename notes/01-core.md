# Enumerate pair combinations: implementation

## What the example does

The Cartesian product combines every left item with every right item. Output size is the product of both lengths, so keep inputs small.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
[
  [
    "red",
    "blue"
  ],
  [
    "S",
    "M"
  ]
]
```

Expected result:

```json
[
  [
    "red",
    "S"
  ],
  [
    "red",
    "M"
  ],
  [
    "blue",
    "S"
  ],
  [
    "blue",
    "M"
  ]
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
