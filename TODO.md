# **To Dos**

---

<br>

- TODO: Excel data sheet -> ydata report :2023-02-25
    - build and test out end 2 end process
    - [ ] python function for opening sheet and loading to df
        - must take in workbook path and sheet names as variables
        - [x] develop
        - [ ] test
    - [ ] python function for setting up ydata_config.yaml
        - based on professional version. should work the same
        - [ ] develop
            - [ ] some small changes to default config
        - [ ] test
    - [ ] simple python script orchestrating the following:
        - [ ] develop
            - [x] takes in sys.args from .bat script
            - [x] load data from excel sheet using passed in variables
            - [x] load data into pandas df
            - [ ] cleaning / prep operations
            - [ ] use data to generate ydata_profiling report
                - in same directory as excel file
        - [ ] test
    - [ ] VBA script for:
        - [ ] develop
            - [ ] passing variables to batch
            - [ ] kicking off python
        - [ ] test

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
