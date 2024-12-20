from sys import flags

import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [20, 21, 22, 20, 23],
    "Department": ["Math", "Physics", "CS", "Math", "CS"],
    "GPA": [3.9, 3.5, 3.8, 3.7, 3.6],
    "Credits": [30, 28, 32, 30, 26]
}

data_fame = pd.DataFrame(data)

gpa = data_fame[data_fame["GPA"] > 3.7]
print(gpa, '\n')
dep = data_fame[data_fame["Department"] == "Math"]
print(dep, '\n')

age_s = data_fame.sort_values(by="Age")
print(age_s, '\n')
gpa_s = data_fame.sort_values(by="GPA", ascending=False)
print(gpa_s, '\n')

gpa_sred = data_fame.groupby("Department")["GPA"].mean()
print(gpa_sred, '\n')
studentsa = data_fame["Department"].value_counts()
print(studentsa, '\n')

data_fame["Internship"] = [False, False, np.nan, True, np.nan]
pprr = data_fame[data_fame.isnull().any(axis=1)]
data_fame["Internship"].fillna(False, inplace=True)

data_fame["Final Credits"] = data_fame["Credits"] * data_fame["GPA"]
print(data_fame)

vtorye_studenty = data_fame.iloc[1]
print(vtorye_studenty, '\n')
three_studenta = data_fame.iloc[:3, [0, 3]]
print(three_studenta, '\n')
data_fame.iloc[3, 3] = 3.95

posledniy = data_fame.iloc[:, -2:]
print(posledniy)
