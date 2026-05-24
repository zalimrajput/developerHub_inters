Task 1

1. Task objective
   The objective of this task is to understand the structure and patterns of a dataset by performing basic data exploration
   and   visualization. Using tools like pandas, matplotlib, and seaborn, the goal is to inspect the dataset, analyze summary
   statistics, and visualize relationships between features to gain meaningful insights.
   
3. Dataset used
   kaggle iris dataset
   https://www.kaggle.com/datasets/uciml/iris/data
 

5. Models applied
   no model applied

7. Key results and findings
   The dataset contains multiple features such as sepal length, sepal width, petal length, and petal width, which help
   distinguish  different flower species.
   Using .info() and .describe() revealed that the dataset is clean (no missing values) and provides useful statistical
   summaries like mean, standard deviation, and range.
   Scatter plots showed clear relationships between features:
   Petal length and petal width have a strong correlation.
   Different species form distinct clusters, making classification easier.
   Histograms indicated how values are distributed:
   Some features follow a near-normal distribution.
   Others show slight skewness depending on species.
   Box plots helped identify:
   Presence of a few outliers
   Variation in feature values across species
   Visualization made it easier to see that certain features

   
--------------------------------------------------------------------------------------------------------------------------------------------
Task 2 (predict future stock prices)


1. Task objective
   To build a predictive model that estimates the next day’s closing price of a selected stock using historical data and machine learning    techniques.

3. Dataset used
   # Download latest version
   https://finance.yahoo.com/quote/AAPL/history/


5. Models applied
   linear regression or random forest

7. Key results and findings
   The machine learning models successfully learned patterns from historical stock data and were able to predict the next day’s closing      price with reasonable accuracy.
   Linear Regression performed well for capturing overall trends, but it struggled with sudden market fluctuations and
   non-linear patterns.
   Random Forest provided better accuracy in most cases because it can handle complex and non-linear relationships in stock data.
   
------------------------------------------------------------------------------------------------------------------------------------------

Task 3 (Heart Disease Prediction)


1. Task objective
   The objective of this task is to develop a machine learning model that can predict whether a person is at risk of heart disease
   based on medical and health-related data. The model uses classification algorithms such as Logistic Regression or Decision Tree
   to analyze patterns in patient data and assist in early risk detection.

3. Dataset used
   # Download latest version
   https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset


5. Models applied
   logistic regression and decision tree
  

7. Key results and findings
   The dataset requires cleaning and preprocessing before modeling,but this data is clean and short for prediction.
   Certain features (e.g., age, cholesterol, chest pain) strongly influence predictions.
   Classification models can effectively predict heart disease risk.but misclassify some cases beacuse it doesnot learn complex pattern.
   Logistic Regression gives stable results, while Decision Tree captures complex patterns.
   Evaluation metrics like accuracy, ROC curve, and confusion matrix help measure model performance.
   The model can support early detection, but cannot replace medical diagnosis

-----------------------------------------------------------------------------------------------------------------------------------------

 
Task 4 (Health chatbot)


1. Task objective
   The objective of this task is to develop a chatbot that can answer general health-related questions using a Large Language
   Model (LLM). The chatbot should generate clear, friendly, and informative responses through prompt engineering while ensuring
   safety by avoiding harmful or misleading medical advice.
  

3. Dataset used
   not used


5. Models applied
   llm model (gpt-3.5-turbo)
  

7. Key results and findings
   Prompt engineering helps control the tone and quality of chatbot responses.
   LLMs can effectively answer general health questions in simple language.
   Safety filters are essential to prevent harmful or misleading advice.
   The chatbot performs well for basic guidance, but not for diagnosis.
   Clear instructions like “act as a helpful medical assistant” improve responses.
   The system should always encourage consulting a doctor for serious symptoms.

-----------------------------------------------------------------------------------------------------------------------------------------

Task 6 (house price prediction)


1. Task objective
   The objective of this task is to build a machine learning model that can predict house prices based on property features such as
   size, number of bedrooms, and location. By applying regression techniques, the goal is to estimate property values accurately
   and analyze the relationship between different features and price.
  

3. Dataset used
   # Download latest version
   https://www.kaggle.com/datasets/jacksondivakarr/house-price-prediction-dataset 


5. Models applied
   linear regression and gradient boosting 
  

7. Key results and findings
   Data preprocessing is important to handle missing values and feature scaling.
   Features like square footage and location have the strongest impact on price.
   Linear Regression works well for simple relationships, while Gradient Boosting improves accuracy.
   Evaluation metrics like MAE and RMSE help measure prediction performance.
   Model accuracy depends on data quality and feature selection.


-----------------------------------------------------------------------------------------------------------------------------------------
 Adanced Tasks of Developer Hub Corporation
-----------------------------------------------------------------------------------------------------------------------------------------

Task 1 (News Topic Classifier Using BERT)


1. Task objective
   The objective of this project is to fine-tune a transformer-based language model (BERT) to classify news headlines into
   predefined categories. The model learns to automatically understand and categorize text into four classes: World, Sports, Business, and
   Sci/Tech. Finally, the trained model is deployed using a web interface (Streamlit) for real-time prediction of news headlines.
  

3. Dataset used
   # Download latest version
   https://www.kaggle.com/code/mohsinsial/ag-news-classifications/notebook


5. Models applied
   bert-base-uncased from BERT 
  

7. Key results and findings
   | Metric   | Value      |
   | -------- | ---------- |
   | Accuracy |   94.59%   |
   | F1 Score |   94.59%   |
   | Loss     |   0.176    |

   The fine-tuned BERT model successfully classifies news headlines into four categories with high accuracy (~95%). The
   model demonstrates strong generalization and is effectively deployed using a Streamlit-based interactive web application for
   real-time predictions.


-----------------------------------------------------------------------------------------------------------------------------------------

Task 2 (End-to-End ML Pipeline with Scikit-learn Pipeline API)


1. Task objective
   The objective of this project was to build an end-to-end machine learning pipeline to predict customer churn and identify
   customers likely to leave a telecom service. The goal was to improve prediction performance using preprocessing, model tuning,
   and threshold optimization. 
  

3. Dataset used
   # Download latest version
   https://www.kaggle.com/code/tugceeeds/telco-churn-dataset/notebook


5. Models applied
   Logistic Regression (with class balancing)
   Random Forest Classifier (with class balancing)
   GridSearchCV for hyperparameter tuning
   Threshold tuning for classification optimization 
  

7. Key results and findings
   Logistic Regression performed well for baseline linear patterns in data.
   Random Forest improved handling of non-linear relationships.
   Class imbalance handling (class_weight="balanced") improved recall for churn customers.
   Threshold tuning improved F1-score and reduced misclassification.
   Final model achieved balanced performance but still showed some FP and FN due to overlapping customer behavior patterns.

   Important Insights 
   Adding feature engineering significantly improves model performance, especially for reducing:
   False Positives (FP) → customers wrongly predicted to churn,
   False Negatives (FN) → customers wrongly predicted as non-churn


-----------------------------------------------------------------------------------------------------------------------------------------

Task 3 (Multimodal ML – Housing Price Prediction Using Images + Tabular Data)


1. Task objective
   The objective of this project was to develop a multimodal machine learning model for predicting housing prices using both:
   Structured tabular data (e.g., no.of bedrooms, city, area, location,price, etc.)
   House images processed through deep learning techniques
  

3. Dataset used
   # Download latest version
   https://www.kaggle.com/datasets/jacksondivakarr/house-price-prediction-dataset


5. Models applied
   A Convolutional Neural Network (CNN) was used to extract meaningful visual features from house images. 
  

7. Key results and findings
   Final Evaluation Metrics
   MAE (Mean Absolute Error): 2,418,070.31
   RMSE (Root Mean Squared Error): 5,644,552.74
   | Actual Price | Predicted Price |
   | ------------ | --------------- |
   | 11,399,999   | 10,535,612      |
   | 9,382,000    | 9,403,644       |
   | 9,640,000    | 9,442,722       |
   | 15,000,000   | 15,445,524      |
   | 7,300,000    | 7,107,063       |

   
   These examples show that the model achieved good prediction accuracy for many medium-range properties. 
   The multimodal model successfully learned from both image and tabular data.
   Predictions were reasonably accurate for standard housing prices.
   Large errors occurred for extreme or outlier properties and because of small dataset of 200 , it is not possible to take 29k+ images
   for train a cnn because we can use one row with one image and our dataset has 29k+ rows .
   and another issue is we randomly take images of houses so it also effect the price of house .

-----------------------------------------------------------------------------------------------------------------------------------------

