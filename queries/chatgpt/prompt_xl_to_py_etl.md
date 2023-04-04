# **ChatGPT Prompt**

<br>

## Prompt:

---

I have an excel workbook with the following structure to its sheet names:
```
data1_in | data2_in | data3_in | data1_out | data2_out | data3_out
```

Please write a python function that will read the data in each sheet and return a list of pandas dataframes with the following structure:
[
    {
        'data1_in': data1_in_df,
        'data2_in': data2_in_df,
        'data3_in': data3_in_df,
    },
    {
        'data1_in': data1_in_df,
        'data2_in': data2_in_df,
        'data3_in': data3_in_df,
    },
    ...
]

This should only apply to sheets that have the 'in' suffix. The 'out' suffix should be ignored.
```


<br>

## Results:

---



<br>
