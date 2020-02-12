import pandas
from sklearn import preprocessing
from sklearn.datasets import load_iris()

# Load Datasets
label_encoder = preprocessing.LabelEncoder()
iris_datasets = load_iris()
tennis_datasets = pandas.read_csv("play_tennis.csv")

