# VisualNestedDict

VisualNestedDict is a simple Python tool to visualize keys and data types in a nested dictionary.

Data pulled from an API are often stored in nested dictionaries, and sometimes it is hard to keep track of the keys and their layers. This tool will print a tree of all keys and their data types so you can find the desired information quickly.



## Example

```
>>> from VisualNestedDict import VisualNestedDict
>>> T = VisualNestedDict()
>>> T.read_json('course.json', name='course')
>>> T.text()
course <dict>
├── id <str>
├── name <str>
├── section <int>
├── term <str>
├── instructor <str>
├── schedule <list[dict]>
│                  ├── day <str>
│                  ├── time <list[int]>
│                  └── room <str>
└── student <list[dict]>
                  ├── name <str>
                  ├── major <str>
                  └── grade <dict>
                      ├── homework <list[int]>
                      ├── midterm <int>
                      └── final <int>
```

## Features

1. Read a nested dictionary or a json file, then print a tree displaying their keys & data types.
2. For (nested) lists, it only reads the first element.

TODO:

3. Provide better support for nested lists
4. Add an option to display values
5. Use different colors for keys/dtypes
6. Build an interactive GUI
