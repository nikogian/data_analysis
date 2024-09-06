import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_excel('Regional_data.xlsx', sheet_name='Business Bay')


# GRAPHS (box plot for outliers)

# plt.figure(figsize=(10, 6))
# plt.boxplot([df['bathrooms'], df['bedrooms']], labels=['No of bathrooms', 'No of bedrooms'], vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue'))

# plt.title('Box Plot Demonstrating Outliers')
# plt.xlabel('Outliers')

# plt.show()


# plt.figure(figsize=(10, 6))
# plt.boxplot(df['price_per_m2'], vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue'))

# plt.title('Box Plot Demonstrating Outliers')
# plt.xlabel('Price per m2')

# plt.show()


# plt.figure(figsize=(10, 6))
# plt.boxplot(df['sizeMin'], vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue'))

# plt.title('Box Plot Demonstrating Outliers')
# plt.xlabel('Size in m2')

# plt.show()


# OUTLIERS

def outliers_detection(column):
    # Step 1: Calculate Q1 (25th percentile) and Q3 (75th percentile)
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    # Step 2: Calculate the Interquartile Range (IQR)
    IQR = Q3 - Q1
    print(Q1,Q3,IQR)
    # Step 3: Define the lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Step 4: Identify outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)][column]
    outliers = set(outliers)  # Convert to set to remove duplicates
    return outliers


for col in ['bathrooms', 'bedrooms', 'price_per_m2','sizeMin']:
    outliers = outliers_detection(col)
    mask = df[col].isin(outliers)
    df_no_outliers = df[~mask]


print(df.dtypes)


X = df_no_outliers.drop(columns=['title', 'region', 'price', 'price_per_m2', 'Region_number'])
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
print(f"Average Price: {average_price:.2f}")


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

