import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\yogen\Downloads\iris.csv")

# Overall means
print("Overall Means:")
print(f"Sepal Length: {df['SepalLengthCm'].mean():.2f}")
print(f"Sepal Width: {df['SepalWidthCm'].mean():.2f}")
print(f"Petal Width: {df['PetalWidthCm'].mean():.2f}")
print(f"Petal Length: {df['PetalLengthCm'].mean():.2f}")

# Group by species for SepalLengthCm
print("\nAverage Sepal Length by Species:")
k = df.groupby("Species")["SepalLengthCm"].mean()
print(k)

# Filter petal length > 6
filtered_species = df[df['PetalLengthCm'] > 6].shape[0]
print(f"\nNumber of flowers with Petal Length > 6: {filtered_species}")

# Top 10 PetalWidthCm stats
print("\nStats of 10 Largest Petal Widths:")
l = df['PetalWidthCm'].nlargest(10).describe()
print(l)

# Virginica stats
print("\nIris-virginica Means:")
virginica = df[df['Species'] == 'Iris-virginica'].mean(numeric_only=True)  # Avoid non-numeric cols
print(virginica)
avg_sepal_length = virginica['SepalLengthCm']
print(f"Average Sepal Length of Iris-virginica: {avg_sepal_length:.2f}")