
[![Data visualization for Covid-19](https://res.cloudinary.com/marcomontalbano/image/upload/v1654684839/video_to_markdown/images/youtube--2EKIGCL_9A8-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=2EKIGCL_9A8 "Data visualization for Covid-19")

# 📊 Data Visualization and Prediction Models for COVID-19

📅 **Project Duration:** August 2020 – September 2020  
🔗 **GitHub Repository:** [Covid-19_Data_visualization-prediction_models](https://github.com/Chin-Sun/Covid-19_Data_visualization-prediction_models)

## 📌 Overview

This project presents a comprehensive analysis and forecasting system for COVID-19 pandemic trends across global regions. It combines **data scraping**, **interactive web visualization**, and **mathematical modeling** using compartmental epidemiological frameworks (SIR-family models) to **simulate and predict** infection dynamics. Special focus was placed on **Brazil** as a case study for one-month forecasting.

---

## 🧩 Key Features

- **Dynamic data visualization** of real-time COVID-19 trends by country  
- **Mathematical model fitting** using multiple SEIR-based epidemiological models  
- **Forecasting simulations** for short-term trend analysis (e.g., next 30 days)  
- **Interactive web interface** enabling country selection and trend exploration  

---

## 🧪 Data Processing

- **Data Sources:** Public health and government websites, including WHO and Johns Hopkins CSSE  
- **Collection Strategy:**
  - Automated data scraping for case numbers, recoveries, and deaths from March to August 2020
  - Preprocessing steps included handling missing data, smoothing noisy entries, and normalizing by population
- **Storage:** CSV-formatted datasets structured by country and date

---

## 🧠 Predictive Modeling

- **Models Implemented:**  
  - Logistic Growth  
  - SI, SIS, SIR, SIRS, SEIR, SEIRS Models  
- **Fitting Methods:**
  - Non-linear least squares for parameter estimation
  - Model selection based on goodness-of-fit and RMSE comparison  
- **Simulation Focus:**
  - Brazil selected as a target country for short-term (1-month) outbreak forecasting  
  - Evaluated sensitivity of infection rates and recovery rates on model behavior

---

## 💻 Technology Stack

- **Programming Language:** Python  
- **Libraries & Tools:**
  - `NumPy`, `Pandas` – Data processing  
  - `Matplotlib`, `Seaborn`, `Plotly` – Data visualization  
  - `SciPy.optimize` – Parameter fitting and model calibration  
  - `Flask` – Web interface backend  
  - `HTML/CSS` – Frontend design for user interaction

---

## 🖥️ Web Interface

- Developed using **Flask** framework  
- Enabled users to:
  - Select a country from dropdown menu  
  - View time-series plots for confirmed cases, deaths, and recoveries  
  - Compare actual data with model predictions in interactive graphs  
- Responsive layout supporting desktop and tablet browsers

---

## 📚 Core Skills Demonstrated

- **Data pipeline creation** from acquisition to cleaning and analysis  
- **Mathematical modeling** using compartmental disease models  
- **Model fitting and evaluation** with real-world epidemiological data  
- **Full-stack web development** with Python (Flask)  
- **Data visualization** and interactive dashboard creation  
- **Scientific analysis communication** through clear visual outputs and simulations  

---

## 🧠 Reflections
This project not only sharpened my skills in mathematical modeling and data visualization, but also demonstrated how computational tools can be used for real-time decision support in public health crises.



---
