# VisualNestedDict

VisualNestedDict is a simple Python tool to visualize keys and data types in a nested dictionary.

Data pulled from an API are often stored in nested dictionaries, and sometimes it is hard to keep track of the keys and their layers. This tool will print a tree of all keys and their data types so you can find the desired information quickly.



## Example

```python
from VisualNestedDict import VisualNestedDict

course = {'id':'MATH 101', 'name':'Differential Calculus', 'section':100, 'term':'Spring 2021', 'credict':3, 'instructor':'John Doe', 'schedule': [{'day':'Monday', 'time':[840,930], 'room':'Remote'}, {'day':'Wednesday', 'time':[510, 600], 'room':'Remote'}], 'student': [{'name': 'Adam Lee', 'major': 'mathematics', 'grade': {'homework': [10, 9, 10, 10, 8], 'midterm':9, 'final':9}}, {'first_name':'Dana McKay', 'major': 'business', 'grade': {'homework':[8, 9, 10, 7, 8], 'midterm':8, 'final': 10}}]}
                                  
VND = VisualNestedDict(name='course')
VND.load(course)
VND.text()
```
Output:
```
course <dict>
├── id <str>
├── name <str>
├── section <int>
├── term <str>
├── credict <int>
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

## TODO

1. add an option to display values
2. use different colors for keys/dtypes
3. build an interactive GUI
