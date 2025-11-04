### 🏡 AI House Price Predictor


## 🏗️ Folder Structure

HousePricePrediction/
│
├── app.py                # Main Streamlit app (Python file)
├── house_data.csv        # Dataset file used for model training
├── requirements.txt      # All dependencies needed to run the project
└── README.md             # (optional) Project documentation


---

## 📘 File Descriptions

### 1️⃣ app.py

* This is your *main Python file* that runs the Streamlit web app.
* It:

  * Loads and preprocesses the dataset
  * Trains a LinearRegression model
  * Takes user input (Sqft, Bedrooms, Bathrooms, City)
  * Predicts the house price instantly
  * Displays the result beautifully using a modern UI

### 2️⃣ house_data.csv

* This is your *dataset* file that contains training data for the model.
* Example:

  
  Sqft,Bedrooms,Bathrooms,City,Price
  1400,3,2,Hyderabad,12000000
  1600,3,2,Vijayawada,10000000
  ...
  
* It helps the app learn the relationship between house features and their prices.

### 3️⃣ requirements.txt

This file lists all the libraries needed to run your app.
Create it in your folder with this content 👇


streamlit
pandas
scikit-learn


---

### 1️⃣ What the project does

👉 It predicts *house prices* based on inputs like *area (sqft), bedrooms, bathrooms, and city*.
The app uses *Machine Learning (Linear Regression)* to estimate the price instantly with a *beautiful Streamlit UI*.

---

### 2️⃣ How to install or run it:**

* First, install Python on your computer.
* Open your command prompt or VS Code terminal.
* Type and run this command to install the required packages:

  ```
  pip install streamlit pandas scikit-learn
  ```
* Save your code as `app.py` and your dataset as `house_data.csv` in the same folder.
* Then type this command to run your app:

  ```
  streamlit run app.py
  ```
* The app will open in your browser automatically.

---

---

### 3️⃣ What technologies it uses

* *Python 🐍* — main programming language
* *Pandas 📊* — for reading and handling dataset
* *Scikit-learn 🤖* — for building and training the Linear Regression model
* *Streamlit 🌐* — for creating the interactive web interface
* *HTML and CSS — for design and styling
---

### 4️⃣ Who created it

👤 *Created by:* Venkata Dharani Neeli
💡 As part of a Machine Learning mini project using Python & Streamlit.

---

### 5️⃣ How to contribute or report issues

If you want others to contribute or report bugs:

* 🧑‍💻 Fork this repository on GitHub
* 💬 Report issues under the *"Issues"* tab
* 🔧 Suggest UI/feature improvements via pull requests

---
