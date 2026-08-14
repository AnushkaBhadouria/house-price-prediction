# house-price-prediction
INTERNID - CITS7524


🏠 House Price Prediction using Machine Learning
A Machine Learning project that predicts house prices based on various property features such as area, number of bedrooms, bathrooms, floors, and other house-related attributes. The model is trained using Linear Regression and deployed with Streamlit for an interactive web interface.

📌 Project Overview
This project demonstrates the complete Machine Learning workflow, including:

Data Loading
Data Preprocessing
Exploratory Data Analysis (EDA)
Feature Selection
Model Training
Model Evaluation
Model Saving
Streamlit Web Application Deployment
The application allows users to enter house details and instantly receive the predicted house price.

🚀 Features
Predicts house prices using Machine Learning
User-friendly Streamlit interface
Data preprocessing and feature scaling
Model evaluation using R² Score and Mean Squared Error (MSE)
Saved trained model using Joblib
Easy to run locally
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Streamlit
Joblib
📂 Project Structure
House-Price-Prediction/
│
├── dataset/
│   └── data.csv
│
├── model/
│   ├── house_model.pkl
│   └── scaler.pkl
│
├── notebook/
│   └── house_price_prediction.ipynb
│
├── app.py
📊 Dataset
The project uses the House Sales Dataset containing property information such as:

Bedrooms
Bathrooms
Living Area
Lot Area
Floors
Waterfront
View
Condition
Above Ground Area
Basement Area
Year Built
Year Renovated
Target Variable:

House Price
⚙️ Installation
Clone the repository

git clone https://github.com/yourusername/House-Price-Prediction.git
Go to the project folder

cd House-Price-Prediction
Install dependencies

pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py
Open your browser and visit:

http://localhost:8501
📈 Machine Learning Workflow
Load Dataset
Data Cleaning
Feature Selection
Train-Test Split
Feature Scaling
Train Linear Regression Model
Evaluate Model Performance
Save Model
Deploy with Streamlit
📏 Evaluation Metrics
R² Score
Mean Squared Error (MSE)
💻 User Inputs
The application accepts the following inputs:

Bedrooms
Bathrooms
Living Area
Lot Area
Floors
Waterfront
View
Condition
Above Ground Area
Basement Area
Year Built
Year Renovated
🎯 Output
The application predicts the estimated house price based on the user-provided property details.

📸 Future Improvements
Add Random Forest and XGBoost models
Improve prediction accuracy
Deploy on Streamlit Community Cloud
Add feature importance visualization
Improve UI design
👩‍💻 Author
Anushka Bhadouria

⭐ If you found this project helpful, please consider giving it a star on GitHub!
