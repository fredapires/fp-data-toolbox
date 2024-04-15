# fp-data-toolbox

---

maintain this project as a central repo for data management functions

## Tech Stack setup guide

### Core setup

1. [ ] Download and install [Github Desktop](https://desktop.github.com/)
2. [ ] clone this repo to local machine
3. [ ] Download and install [VS Code](https://code.visualstudio.com/)
    1. [ ] Make sure to sign in to personal account for settings sync
4. [ ] download and install [Docker Desktop](https://www.docker.com/products/docker-desktop)
5. [ ] download and install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
6. [ ] download and install [Python 3.11](https://www.python.org/downloads/)
    1. [ ] make sure to add to PATH
7. [ ] download and install [Poetry](https://python-poetry.org/docs/)
    1. [ ] using poetry setup general python virtual env in users folder structure

#### Testing the Python setup

1. [ ] connect to general python virtual env in users folder structure
    1. `poetry shell`
    2. `poetry install`
    3. `poetry update`
2. [ ] connect to virtual env with template jupyter notebook and test venv

### Addtional Setup

1. [ ] Download and install [AutoHotKey](https://www.autohotkey.com/)
    1. Setup for replacing CapsLock with Ctrl
2. [ ] download and install [Ditto Clipboard Manager](https://ditto-cp.sourceforge.io/)

#### QMK keyboard reflashing setup

1. [ ] download and install [qmk_toolbox](https://github.com/qmk/qmk_toolbox?tab=readme-ov-file)
2. [ ] download and install [QMK MSYS](https://msys.qmk.fm/)
3. [ ] clone our personal fork of `qmk_firmware` repo
    1. [ ] Test building firmware with QMK MSYS
    2. [ ] Test flashing firmware with `qmk_toolbox`

<br><br><br>

## Folder structure explanation

```

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

<br><br><br>
