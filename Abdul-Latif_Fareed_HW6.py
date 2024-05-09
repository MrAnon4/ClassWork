import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


cars = pd.read_csv("car_info.csv")
print('#1- Shape of DataFrame:')
print(cars.shape)
print()

print('#2- Japanese cars having v6 engines:')
jcars_v6 = cars[(cars["cylinders"] == 6) & (cars["origin"] == "japan")]
print(jcars_v6.name)
print()

print('#3- Cars with missing horsepower data:')
print(cars[cars["horsepower"].isnull()].name)
print()

print('#4- Number of cars with mpg >= 20:')
print(len( cars[cars["mpg"] >= 20] ))
print()

print('#5- Car with highest mpg:')
print( cars[cars["mpg"] == cars["mpg"].max(axis=0)].name )
print()

print('#6- Min, Max, Avg car weights:')
print( f"Minimum weight: {cars['weight'].min(axis=0)}; Maximum weight: {cars['weight'].max(axis=0)}; Average weight: {round(cars['weight'].mean(axis=0), 2)} " )
print()

print('#7- Drop rows with missing data and print shape:')
cars = cars.dropna(axis=0)
print( cars.shape )
print()

# pie chart proportion of cars manufactured in different countries
cars.groupby(["origin"]).size().plot(kind="pie", autopct="%.2f%%")
plt.ylabel("Proportion of Cars Manufactured in Different Countries")
plt.show()

# scatter plot mpg vs. weight
plt.subplot(1,2,1)
plt.scatter(cars["weight"], cars["mpg"], label="m/(g*lbs)")
plt.title("MPG vs. Weight")
plt.xlabel("Weight (lbs)")
plt.ylabel("Miles Per Gallon (m/g)")
plt.legend()

# scatter plot mpg vs. displacement
plt.subplot(1,2,2)
plt.scatter(cars["displacement"], cars["mpg"], label="m/(g*in^3)")
plt.title("MPG vs. Displacement")
plt.xlabel("Displacement (in^3)")
plt.ylabel("Miles Per Gallon (m/g)")
plt.legend()
plt.show()
