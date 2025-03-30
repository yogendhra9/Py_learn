import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r"C:\Users\yogen\Downloads\iris.csv")
sns.set(style="whitegrid")
sns.set_palette("pastel")
plt.figure(figsize=(12,6))
sns.barplot(x="Species", y="SepalLengthCm", data=df, ci=None, palette="dark:.3")
plt.title("Average Sepal Length by Species")

sns.pairplot(df, hue="Species", diag_kind="hist", palette="bright")
plt.show()
df = df.drop(columns=['Id'])
sns.pairplot(df,hue="Species", diag_kind="hist", palette="pastel")
plt.title("Pairplot of Iris Dataset")
plt.title("Sepal Length Distribution")
plt.show() 