import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import joblib

X = np.array([
    [800, 2],
    [1000, 2],
    [1200, 3],
    [1500, 3]
])

y = np.array([30, 40, 50, 65])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "house_model.pkl")
print("Model trained and saved as house_model.pkl")


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

