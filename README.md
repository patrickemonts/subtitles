# Subtitles

This small piece of codes displays white text on a black background to provide subtitles for an artistic performance.

# Requirements

This tool is based on `tkinter`, there are no other python package dependencies which are not shipped with Python per default.
By default, `tkinter` is shipped with Python as well.
On Mac, however, you will have to install the `tkinter` package via `brew`:
```
brew install python-tk
```

# Usage
Call the python program `main.py` with 
```python
python main.py <name of subtitles>
```

The input file for the subtitles should contain each subtitle in a separate line.
Empty lines are ignored.

# Keys
- `Right arrow`, `Left Mouse Button`: Next subtitle
- `Left arrow`: Previous subtitle
- `q`: Quit the program

# Example

```
Sub 1
Sub 2

Sub 3
```

This will display three subtitles, the empty line is ignored.
