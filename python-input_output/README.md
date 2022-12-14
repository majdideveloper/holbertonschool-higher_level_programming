# Python - Input/Output

In this project, I practiced file handling in Python. I used the builtin `with`,
`open`, and `read` functions with the `json` module to read and write files and
serialize and deserialize objects with JSON.



## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File        | Prototype               |
| ----------- | ----------------------- |
| `0-read_file.py` | `def read_file(filename=""):` |
| `1-write_file` | `def write_file(filename="", text=""):` |
| `2-append_write.py` | `def append_write(filename="", text=""):` |
| `3-to_json_string.py` | `def to_json_string(my_obj):` |
| `4-from_json_string.py` | `def from_json_string(my_str):` |
| `5-save_to_json_file.py` | `def save_to_json_file(my_obj, filename):` |
| `6-load_from_json_file.py` | `def load_from_json_file(filename):` |
| `7-add_item.py` | `script that adds all arguments to a Python list, and then save them to a file` |
| `8-class_to_json.py` | `def class_to_json(obj):` |
| `9-student.py` | `class Student:` |
| `10-student.py` | `class Student:` |


* **0. Read file**
  * [0-read_file.py](./0-read_file.py): Python function that prints the contents of a UTF8 text
  file to standard output.

* **1. Write file**
  * [1-write_file.py](./1-write_file.py): Python function that writes a string to a text file (UTF8) and returns the number of characters written

* **2. Append write**
  * [2-append_write.py](./2-append_write.py): Python function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

* **3.Json To String**
  * [3-to_json_string.py](./3-to_json_string.py): Python function that returns the JSON representation of an object (string).

* **4.From Json String**
  * [4-from_json_string.py](./4-from_json_string.py): Python function that returns an object (Python data structure) represented by a JSON string.

* **5.Save To Json File**
  * [5-save_to_json_file.py](./5-save_to_json_file.py): Python function that writes an Object to a text file, using a JSON representation. 

* **6.Load from Json File**
  * [6-load_from_json_file.py](./6-load_from_json_file.py): Python function that creates an Object from a ???JSON file???

* **7. Load, add, save**
  * [7-add_item.py](./7-add_item.py): Python script that stores all command line arguments to a
  Python list saved in the file `add_item.json`.

* **8. Class to JSON**
  * [8-class_to_json.py](./8-class_to_json.py): Python function that returns the dictionary
  description for simple Python data structures (lists, dictionaries, strings,
  integers and booleans).

* **9. Student to JSON**
  * [9-student.py](./9-student.py): Python class `Student` that defines a student. Includes:
    * Public instance attributes `first_name`, `last_name`, and `age`.
    * Instantiation with `first_name`, `last_name`, and `age`:
    `def __init__(self, first_name, last_name, age):`.
    * Public method `def to_json(self):` that returns the dictionary
    representation of a `Student` instance.

* **10. Student to JSON with filter**
  * [10-student.py](./10-student.py): Python class `Student` that defines a student. Builds on
  [9-student.py](./9-student.py) with:
    * Public method `def to_json(self, attrs=None):` that returns the
    dictionary representation of a `Student` instance.
    * If `attrs` is a list of strings, only the attributes listed are
    represented in the dictionary.
