# py_script_print_folder_structure_in_markdown

## Prompt

Please write a python script that will print the folder structure of a given directory in the following example format:

```

├── LICENSE
├── README.md          <- The top-level README for developers using this project.
│
├── data
│   ├── temp           <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── notebooks          <- Jupyter notebooks.
│
├── src                <- Source code for use in this project.
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── 

```

Please only include folders (not files) in the structure print out.

## Response

Here is a Python script that uses the os and os.path libraries to traverse through a directory structure and print out only the folders in a tree structure similar to your example:

```python
import os

def print_directory_structure(startpath):
    for root, dirs, _ in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}├── {}'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)

        if level == 0:
            print('{}│'.format(indent))

        for d in dirs:
            print('{}├── {}'.format(subindent, d))

        if dirs:
            print('{}│'.format(subindent))

print_directory_structure("/path/to/your/directory")
```

This script will print out each directory as a tree structure, indented by 4 spaces for each level in the directory structure. To use this script, replace `"/path/to/your/directory"` with the path to the directory you want to print.

Please note that the directories are listed in the order they are returned by the os.walk function, which can vary depending on the underlying file system. If you want a specific order, you might need to sort the directories before printing them.

This script currently outputs an additional pipe symbol ('|') after each directory that contains subdirectories to mimic the example you provided. If you don't want this additional line, you can simply remove or comment out the `if dirs: print('{}│'.format(subindent))` line.
