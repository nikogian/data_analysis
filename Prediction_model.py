import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv('Clean_data.csv')

print(df.dtypes)

df_no_outliers = df[(df['bedrooms'] <= 6) & (df['bathrooms'] <= 6)]

# Separate the features (X) and the target variable (y)
# Assuming 'Price' is the target variable and the rest are features
X = df_no_outliers.drop(columns=['title', 'region', 'price', 'price_per_m2'])
y = df_no_outliers['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the regression model (using Linear Regression as an example)
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Average price calculation for comparison with mae
average_price = df_no_outliers['price'].mean()
print(f"Average Price per m2: {average_price:.2f}")


# Display evaluation metrics
print("\nModel Performance:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2): {r2:.2f}")

# Extracting model parameters (coefficients) to see which features impact the price
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values(by='Coefficient', ascending=False)

print("\nFeature Importance:")
print(feature_importance)

