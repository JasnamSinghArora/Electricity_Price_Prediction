import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import os

# Define the data folder and read the Excel files
data_folder = '/Users/jasnamsingharora/Desktop/Electricity_Price_Prediction/'
files = [f for f in os.listdir(data_folder) if f.startswith('Power Exchange Data_') and f.endswith('.xlsm')]

# Combine the data from all files into a single DataFrame
df_list = []
for file in files:
    file_path = os.path.join(data_folder, file)
    temp_df = pd.read_excel(file_path, engine='openpyxl')
    df_list.append(temp_df)
df = pd.concat(df_list, ignore_index=True)

# Clean the data
df.dropna(inplace=True)
df.columns = df.columns.str.strip()

# Convert 'Date' column to datetime and extract features
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Year'] = df['Date'].dt.year

# Prepare the features and target variable
X = df[['Month', 'Day', 'Year']]
y = df['Prices (EUR/MWh)']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model using Adjusted R^2
predictions = model.predict(X_test)
r2 = r2_score(y_test, predictions)
n = len(y_test)
p = X_test.shape[1]
adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
print(f'Adjusted R^2: {adjusted_r2}')

# Generate features for 2018 to predict
dates_2018 = pd.date_range(start='2018-01-01', end='2018-12-31', freq='D')
features_2018 = pd.DataFrame({
    'Month': dates_2018.month,
    'Day': dates_2018.day,
    'Year': dates_2018.year
})

# Predict prices for 2018
predictions_2018 = model.predict(features_2018)

# Export the predictions for 2018 to a CSV file
predictions_df_2018 = pd.DataFrame({
    'Date': dates_2018,
    'Predicted Average Price (EUR/MWh)': predictions_2018
})
predictions_df_2018.to_csv('predicted_prices_2018.csv', index=False)
print(f"CSV file saved: ./predicted_prices_2018.csv")

desktop_path = '/Users/jasnamsingharora/Desktop/'
csv_file_path = os.path.join(desktop_path, 'predicted_prices_2018.csv')

predictions_df_2018.to_csv(csv_file_path, index=False)
print(f"CSV file saved: {csv_file_path}")
