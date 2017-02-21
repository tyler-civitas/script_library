# script_library
Minor scripts in bash (.sh) and python (.py)

---

### convert_tab_to_csv.py
**Used to avoid quote-related parsing errors**

_A command-line invoked, very verbose, tab-delimited-to-csv-delimited file converter that outputs all lines to STDOUT to make its changes transparent. Includes representative strings with escape characters printed. Encapsulates all fields in double-quotes to avoid SQL/Excel parsing mistakes when commas are present in field values._  


Module (pydoc) instructions:

```python
"""Converts a tab delimited file to a CSV
BASH FORMAT: $ python convert_tab_to_csv.py input_file.txt output_file.csv
Will OVERWRITE existing output file if one is present.
NOTE: Will wrap fields in quotes to prevent comma-interference if
      commas exist within fields"""
```

---

### rpn.py
**A very useless reverse-polish notation calculator script**

_Also stores ongoing expressions as you calculate. This calculator was made as part of a workshop exercise_

---
