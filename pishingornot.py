from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
import joblib

data = pd.read_csv("phishing.csv")

X = data.drop(["class"], axis=1)
y = data["class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

gbc = GradientBoostingClassifier(max_depth=4, learning_rate=0.7)
gbc.fit(X_train, y_train)

# Save the trained model to a file
model_filename = "trained_gbc_model.joblib"
joblib.dump(gbc, model_filename)
