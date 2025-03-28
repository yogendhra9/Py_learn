import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
l = df.groupby("Species")['SepalWidthCm'].mean()
plt.subplots_adjust(hspace=1
                    )  # Adjust space between subplots
plt.subplot(3,1,1)
l.plot(kind="bar", title="Average Sepal Width by Species", color=['#FF9999', '#66B2FF', '#99FF99'])
plt.ylabel("Sepal Width (cm)")
plt.subplot(3, 1, 2)  #this line should always be there above this 
plt.plot(k,l, marker='o', linestyle='--', color='b')
plt.title("Average Sepal Length by Species")
plt.ylabel("Sepal Width (cm)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Length (cm)")
plt.subplot(3,1,3)  #this line should always be there above this
k.plot(kind="bar", title="Average Sepal Length by Species",color=['#FF9999', '#66B2FF', '#99FF99'])
plt.show()
input("Press Enter to close...")
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

#day one, the age and speed of 13 cars: 
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()


# xpoints = np.array([1,4,3,5])
# ypoints = np.array([1, 4, 3, 4])
# plt.subplot(2,1,1)
# plt.plot(xpoints, ypoints,marker= 'o',color='g',linestyle='dashed',linewidth=2,markersize=12)
# plt.title("Simple Plot")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.grid(color='gray', linestyle='--', linewidth=0.5)

# plt.show()

# y1 = np.array([10.4, 20.5, 30.6, 40.7, 50.8])
# y2 = np.array([12.3, 45.6, 23.4, 56.7, 34.5])
# plt.subplot(2,1,2)
# plt.plot(y1,y2,marker= 'o',color='c',linestyle='dotted',linewidth=2,markersize=12)
# plt.title("Simple Plot")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()