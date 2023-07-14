# useful JQL queries

## examples

<br>

---

- Desc:
    - project key filter

```
project IN (FPT, PDHS, FMP, FDSP)
```

```
project IN (FPT, PDHS)
```

```
project IN (FPT)
```

<br>

---

- Desc:
    - typical ordering

```
order by priority DESC, duedate DESC, updated DESC, created DESC
```

<br>

---

- Desc:
    - filter on what has been recently updated
    - variable date

```
updatedDate >= -1d
```

<br>

---

- Desc:
    - Unresolved issues

```
statusCategory != Done
```

<br>

---

- Desc:
    - issue type filters

```
issuetype NOT IN (Story, Epic)
```

```
s
```

```
s
```

<br>

---

- Desc:
    - Only my issues

```
assignee = currentUser()
```

---

<br>

---

- Desc:
    - Stalled issues
    - variable date range

```
NOT updated >= -4d
```

assignee in (currentUser())
AND issuetype in (Bug, Task, Sub-task)
order by priority DESC, duedate DESC, updated DESC, created DESC
