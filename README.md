# Manufacturing Robot Predictive Maintenance

## 1. Use Case

This project focuses on predictive maintenance for a manufacturing robot. Robot data is collected and analyzed to monitor its condition, identify unusual behavior, and support early detection of possible maintenance needs.

## 2. Problem Definition

Manufacturing robots generate a large amount of sensor and operational data. The project aims to process this data, store it, visualize it, and analyze it to identify anomalies and patterns that could indicate potential maintenance issues.

## 3. Team Members

- Arya vinodbhai Patel - 9084843
- Preethi Vasudevan Nair - 9125985
- Asangika Hettiarachchi - 
  

## 4. Dataset

The project uses the provided manufacturing robot dataset.

*Dataset:* RMBR4-2_export_test.csv

## 5. Project Description

The project simulates robot data streaming from a CSV file. Data is collected one record at a time and processed for different purposes, including database storage, visualization, anomaly detection, and energy consumption analysis.

The project includes:

- Data collection and streaming
- Database management
- Robot dashboard and visualization
- Anomaly detection
- Energy consumption analysis
- Data analysis and processing

```text
project/
│
├── anomalies/
│   └── anomalyReport.ipynb
│
├── data_service/
│   ├── database_manager.py
│   └── datacollection.py
│
├── web_ui/
│   └── web_ui_interface.py
│
├── README.md
└── requirements.txt

```


Anomalies

**anomalyReport.ipynb** - 
Analyzes the collected data to identify and report unusual or abnormal values.

**Data Service**

**datacollection.py** - 
Reads the robot data and provides the data records for processing.

database_manager.py - 
Manages storing and retrieving data from the database.

**Energy Consumption**

**enery_consumption.ipynb** - 
Analyzes energy-related data and provides information about energy consumption.

**StatisticalAnalysis.py** - 
Performs basic statistical analysis on the movie data.

**Web_ui_interface.py** - 
Contains the dashboard and visualization components used to display the processed data.

**Technologies Used**
Python
Pandas
Matplotlib
Jupyter Notebook
Database

