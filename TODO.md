# **To Dos**

---

<br>

- TODO: add o-rings to wireless redox :2024-04-14

<br>

- TODO: Redox QMK remap
- [x] compile list of changes that I would make to the mapping.
    - [x] figure out how to flash QMK to this keyboard, again...
    - [ ] take notes in our fork of qmk_firmware and make sure that the notes are the most visible thing at the top of the `README.md`

------

- TODO: IDEA: "Jira tracker -> TODO.md sync process" :2023-07-04

```mermaid
graph LR
    A[Jira Tracker] -->|JQL query through Jira add-in| B(Excel / .csv file) -->|Python script| C(TODO.md file)
    
```

---

<br>

- TODO figure out how to properly publish this package with `poetry` venv setup :2023-04-20
    - i.e.: with setup.py not in bare bones state
        - do I need to somehow automatically populate setup.py on commit with info from `pyproject.toml`?
    - [ ] to pypi
        - [ ] test installing from other venv
    - [ ] to github
        - [ ] test installing from other venv

<br>

### **In Progress...**

---

<br><br>

### **Low Priority**

---

<br>

- TODO: continue to add cleaning functions to [clean.py](fp_data_toolbox/clean.py) :2022-10-11
    - from `mtg-etl`
    - and from more abstract and general data cleaning ideas

- TODO improve [master .bat script](scripts/batch/_master_script.bat)
    - add more automatic orchestration to be run regularly

<br><br>
