#!/usr/bin/env python3.9
import pandas as pd
from pandas.core.arrays.categorical import cache_readonly
from sklearn_extra.cluster import KMedoids
import numpy as np
from datetime import datetime
from sklearn import metrics

import matplotlib.pyplot as plt

import sys

n = int(sys.argv[2])
# n = int(n/2)
path = str(sys.argv[1])
dm = pd.read_csv(path, delimiter=',')
df1 = dm.iloc[:, 1:]
dm = dm.iloc[:, 1:]

df1 = df1.to_records(index=False)
df1 = df1.tolist()
df1 = np.array(df1, dtype=object)
fileName=path[33:-4]


k_max = 0
best_clusterization = {}
silhouettes = []
for k in range(2, n):
    # with open("./log_new_kmedoid", mode="a") as f:
        # f.write(f"[{datetime.now()}] - k:{k} started\n")
    kmedoids_instance = KMedoids(n_clusters=k, metric="precomputed", method="pam", init="heuristic", max_iter=30000, random_state=n-1).fit(df1)

    score = metrics.silhouette_score(df1, kmedoids_instance.labels_, metric="precomputed")
    silhouettes.append(score)
    if score > best_clusterization.get('silhouette', -1):
        best_clusterization['silhouette'] = score
        best_clusterization['k'] = k
        best_clusterization['labels'] = kmedoids_instance.labels_
    # with open("./log_new_kmedoid", mode="a") as f:
        # f.write(f"Silhoutte {score}\n")
        # f.write(f"[{datetime.now()}] - k:{k} ended\n")

plt.plot(np.arange(2, n), silhouettes)
plt.savefig(f"silhouette_plot_{fileName}.png")

# save silhouettes on file
fileName=fileName+"_("+str(best_clusterization['k'])+"--"+str(best_clusterization['silhouette'])+")"
with open(f"./silhouettes_{fileName}.txt", mode="w") as f:
    f.write(f"k: {best_clusterization['k']} - silhouette = {best_clusterization['silhouette']}\n")
    for index, silhouette in enumerate(silhouettes):
        # silhouettes are saved from 2 to 'n'
        f.write(f"{index+2}: {silhouette}\n")

with open(f"./kmedoids_clustering_{fileName}.csv", mode="w") as f:
    # f.write(f"k: {best_clusterization['k']} - silhouette = {best_clusterization['silhouette']}\n")
    f.write("NomeLog,ClusterId,\n")
    for index, label in enumerate(best_clusterization['labels']):
        f.write(f"{dm.columns[index]},{label},\n")
    # print(f"[{datetime.now()}] - {k} ended")
    # print(silhouette_max)
    # print(k_max)
