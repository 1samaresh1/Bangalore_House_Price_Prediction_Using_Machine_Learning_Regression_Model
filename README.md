<h1 align="center">Bangalore House Price Prediction Using Machine Learning Regression Model</h1>

![logo](https://github.com/1samaresh1/Bangalore_House_Price_Prediction_Using_Machine_Learning_Regression_Model/blob/main/image.png)
The Bengaluru House Prediction project is a machine learning solution designed to help people in Bangalore predict home prices accurately. This is useful because buying a home involves many factors that affect prices and can be confusing.

## Dataset is downloaded from here:
## 🔗  https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data



## Roadmap

- Data Collection and Preprocessing

      Obtain the Bangalore home prices dataset from Kaggle.
      Load the dataset and examine its structure.
      Perform data cleaning to handle missing values and outliers.
      Explore the data distribution and perform necessary transformations.

-  Feature Engineering and Selection

       Identify relevant features for the prediction model.
       Perform feature engineering to create new features if needed.
      
- Model Building with Sklearn and Linear Regression

      Split the dataset into training and testing sets.
      Import necessary libraries like sklearn.
      Build a linear regression model using sklearn.
      Train the model on the training data.
      Evaluate the model's performance on the testing data using appropriate metrics.

- Hyperparameter Tuning 



      Find the best combination of hyperparameters using cross-validation.
- Saving the Model

      Save the trained model to a file using joblib.
      This saved model will be used for making predictions later.
- Python Flask Server

      Set up a Python Flask web server.
      Create an API endpoint that accepts input data (square ft area, bedrooms, etc.).
      Load the saved model and use it to predict prices for the given input.
- Website Frontend Development

      Design a user-friendly website using HTML, CSS, and JavaScript.
      Create input fields for users to enter property details.
      Implement a button to trigger the prediction request.
- Connecting Frontend with Flask Server

       Use JavaScript to capture user inputs from the website.
       Send HTTP requests to the Flask server's prediction endpoint.
       Receive the predicted price from the server's response.
- Display Predicted Price to User

      Update the website's interface to display the predicted price.
      Provide clear visual feedback to the user with the predicted price.

## Required Libraries:
- Python - Primary programming language used for developing the machine learning model.
- pandas: For data manipulation and cleaning.
- numpy: For numerical operations on data.
- scikit-learn: For machine learning algorithms, including linear regression, hyperparameter tuning, and cross-validation.
- matplotlib / seaborn: For data visualization and analysis.
- scipy: For advanced statistical functions.
- Joblib - Used for storing the trained machine learning model.
- flask: For creating a web server and exposing APIs.
- HTML: For structuring the web content.
- CSS: For styling the web page.
- JavaScript: For interactive elements and communication with the Flask server
