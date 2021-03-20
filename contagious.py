import pandas as pd
import numpy as np

variables = ["danceability", "energy", "valence", "tempo", "loudness", "mode", "key",
             "acousticness", "instrumentalness", "liveness", "speechiness", "duration_ms" ]

# arr1 = [-189179.874424269, 1374.82878098807, -124.238712209394, 11.9261178713891, -11.1019048361094]
# arr2 = [-266541.080101775, 1215.78754734219, -108.435380140004, 20.6861721754478, -7.55734435171545]
arr1 = [0, 0, 0, 0, 1]
arr2 = [0.9, 0.8, 0.9, 0.7, 0.5]
sum = 0
for i in range(len(arr1)):
    sum += arr1[i] * arr2[i]
print(sum)
v1 = np.array(arr1)
v2 = np.array(arr2)
print(np.linalg.norm(v1))
print(np.linalg.norm(v2))
base = np.linalg.norm(v1) * np.linalg.norm(v2)
print(sum/base)

# print(base)
# print(sum/base)
# str = "[455]"
# result = str.split('[')[1].split(']')[0]
# print(result)
# year_data = pd.read_csv("data_by_year.csv")
# vary = []
# for i in range(len(variables)):
#     vary.append([])
#     vary[i].append(np.mean(year_data[variables[i]]))
#     vary[i].append(np.var(year_data[variables[i]]))
# for i in range(len(vary)):
#     print(variables[i], ":")
#     print("mean:", vary[i][0])
#     print("var:", vary[i][1])

