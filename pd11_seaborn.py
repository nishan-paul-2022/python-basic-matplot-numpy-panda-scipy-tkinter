from sklearn import datasets
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Patal_Length', 'Petal_Width'])
iris_df['Target'] = iris.target
iris_df['Target'].replace([0], 'Iris_Setosa', inplace=True)
iris_df['Target'].replace([1], 'Iris_Vercicolor', inplace=True)
iris_df['Target'].replace([2], 'Iris_Virginica', inplace=True)

sns.kdeplot(iris_df.loc[(iris_df['Target'] == 'Iris_Virginica'), 'Sepal_Length'], color='b', shade=True, Label='Iris_Virginica')
plt.xlabel('Sepal Length')
plt.ylabel('Probability Density')
plt.show()

sns.kdeplot(iris_df.loc[(iris_df['Target'] == 'Iris_Setosa'), 'Sepal_Length'], color='r', shade=True, Label='Iris_Setosa')
sns.kdeplot(iris_df.loc[(iris_df['Target'] == 'Iris_Virginica'), 'Sepal_Length'], color='b', shade=True, Label='Iris_Virginica')
plt.xlabel('Sepal Length')
plt.ylabel('Probability Density')
plt.show()

iris_setosa = iris_df.query("Target=='Iris_Setosa'")
iris_virginica = iris_df.query("Target=='Iris_Virginica'")
sns.kdeplot(iris_setosa['Sepal_Length'], iris_setosa['Sepal_Width'], color='r', shade=True, Label='Iris_Setosa', cmap="Reds", shade_lowest=False)
plt.show()

sns.kdeplot(iris_setosa['Sepal_Length'], iris_setosa['Sepal_Width'], color='r', shade=True, Label='Iris_Setosa', cmap="Reds", shade_lowest=False)
sns.kdeplot(iris_virginica['Sepal_Length'], iris_virginica['Sepal_Width'], color='b', shade=True, Label='Iris_Virginica', cmap="Blues", shade_lowest=False)
plt.show()

# https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/