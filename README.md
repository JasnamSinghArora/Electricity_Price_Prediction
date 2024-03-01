# Electricity_Price_Prediction

This project aims to predict electricity prices for the year 2018 using historical data. It utilizes a RandomForestRegressor model to analyze past data, identify patterns, and forecast future prices. The project is designed to help in understanding market trends and assisting in planning and decision-making processes.

Features:-

1)Data Preprocessing and Cleaning:
Used pandas to read Excel files, combine them into one DataFrame, and clean the data by removing missing values.

2)Date-related Feature Extraction:
Extracted 'Month', 'Day', and 'Year' from the 'Date' column to help the model understand time-related patterns in electricity prices.

3)Price Forecasting with RandomForestRegressor:
Applied the RandomForestRegressor model to predict future electricity prices, training it on historical data with date features.

4)Model Performance Evaluation:
Evaluated the model's accuracy using the R^2 metric, which shows how well the predictions match the actual prices.

5)Output Predictions to CSV:
Saved the model's 2018 price predictions to a CSV file, making it easy to share and analyze the forecasted data.

Required Prequisities:-

1)Python 3.8 or higher
2)pandas
3)scikit-learn

Usage:-

1)Make sure to download the Electricity_Price_Prediction Folder and save it on your desktop.

2)Change the username while defining the file location.

3)Change the username when defining the desktop path for the CSV file to be saved.
