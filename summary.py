from os.path import getmtime, exists
from datetime import datetime
from matplotlib import pyplot as plt
import seaborn as sns

tt = []
for i in range(100):
    path = "{:02}.py".format(i)
    if not exists(path):
        path = "{:02}.jl".format(i)
    assert exists(path)
    dt = datetime.fromtimestamp(getmtime(path))
    tt.append(dt.strftime("%Y-%m-%d"))

plt.figure(figsize=(30, 20))
p = sns.barplot(x=tt, y=range(100))
plt.xticks(rotation=20)
p.tick_params(axis='both', which='major', labelsize=36)
p.tick_params(axis='both', which='minor', labelsize=36)
plt.xlabel("Day", fontsize=40)
plt.ylabel("Acheivement", fontsize=40)

# plt.show()
plt.savefig("summary.png")
