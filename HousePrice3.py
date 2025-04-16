import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
input_data = "Housing.csv"
df = pd.read_csv(input_data)

# Initialize the scaler
print("Case 3: Only Area, Bedrooms, Bathrooms")
scaler = MinMaxScaler(feature_range=(0, 1))
# Apply scaling to the 'area' column
df['area_scaled'] = scaler.fit_transform(df[['area']])
df['bedrooms_scaled'] = scaler.fit_transform(df[['bedrooms']])
df['bathrooms_scaled'] = scaler.fit_transform(df[['bathrooms']])
# Print the updated DataFrame
print(df[['area', 'area_scaled', 'bedrooms', 'bedrooms_scaled',
          'bathrooms', 'bathrooms_scaled']])
# Split the data into 80% for training and 20% for testing
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
# Print the shapes of the training and testing sets
print(f"Training set shape: {train_df.shape}")
print(f"Testing set shape: {test_df.shape}")
# Separate the features (X) and target (y)
X_train = train_df[['area_scaled', 'bedrooms_scaled', 'bathrooms_scaled']]  # Using multiple scaled features
y_train = train_df['price']  # Target variable is 'price'
X_test = test_df[['area_scaled', 'bedrooms_scaled', 'bathrooms_scaled']]  # Using multiple scaled features
y_test = test_df['price']  # Target variable is 'price'
# Initialize and fit the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Make predictions on the test set
y_predict = model.predict(X_test)
# Compute the Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_predict)
print(f"Mean Squared Error on the test set: {mse}")
# Compute the R² score
r2 = r2_score(y_test, y_predict)
print(f"R² Score on the test set: {r2}")
# The Linear Equation is Y = A + B1X1 + B2X2 -> Y: Price, X1: area_scaled,
# X2: bedrooms_scaled, X3: bathrooms_scaled in this case
A = model.intercept_
B1, B2, B3 = model.coef_[0], model.coef_[1], model.coef_[2]
print(f"Linear Equation: Y = {A} + ({B1} * X1) + ({B2} * X2) + ({B3} * X3)")
