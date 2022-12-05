import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.txt', sep=",", header=None,
                 names=["loc", "vg", "evg", "ivg", "n", "v", "l", "d", "i", "e", "b", "t",
                        "lOCode", "lOComment", "lOBlank", "locCodeAndComment", "uniq_Op", "uniq_Opnd", "total_Op",
                        "total_Opnd", "branchCount", "defects"])
sns.pairplot(df, hue='defects')
sns.stripplot(df)
plt.show()
print(df)
