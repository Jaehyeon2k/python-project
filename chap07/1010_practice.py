import pandas as pd
import matplotlib.pyplot as plt

# 출산율 그래프
data = pd.read_csv("babies.csv")

# plt.plot(data.Year, data.Babies, color='green', marker='o', linestyle='solid')
plt.bar(data.Year, data.Babies)
plt.title("Newborns per year")
plt.ylabel("Number of newborns")

# plt.savefig("newborns_per_year.png", dpi=300)
plt.show()
