# Airline Passenger Satisfaction Analysis using Python

## Project Overview

This project analyzes airline passenger data to understand customer satisfaction and identify the factors that influence the overall passenger experience.

The analysis covers passenger demographics, travel characteristics, service ratings, flight distance, delays, and satisfaction levels using Python.

## Dataset

The dataset contains airline passenger information including:

* Passenger satisfaction
* Gender
* Customer type
* Age
* Type of travel
* Travel class
* Flight distance
* Service ratings
* Departure and arrival delays

**Dataset size:** 129,880 passenger records and 23 columns.

## Tools & Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* VS Code

## Data Cleaning

The following data-cleaning steps were performed:

* Loaded and inspected the dataset
* Checked dataset shape and column information
* Identified missing values
* Handled missing arrival-delay values
* Checked for duplicate records
* Verified data types
* Prepared the dataset for exploratory analysis

After cleaning, there were **0 missing values** and **0 duplicate rows**.

## Exploratory Data Analysis

The project analyzes:

* Overall passenger satisfaction
* Satisfaction by customer type
* Satisfaction by type of travel
* Satisfaction by travel class
* Satisfaction by gender
* Satisfaction by age group
* Average airline service ratings
* Flight distance distribution
* Flight distance by satisfaction
* Departure delay distribution
* Arrival delay distribution
* Average delays by satisfaction
* Class and travel-type satisfaction
* Correlation between numerical variables

## Key Insights

* The dataset contains **129,880 passengers**.
* **54.73%** of passengers are satisfied.
* **45.27%** of passengers are dissatisfied.
* **Business Class** passengers show a significantly higher satisfaction rate than Economy and Economy Plus passengers.
* Business travel is the most common type of travel in the dataset.
* Loyal customers represent the majority of passengers.
* Flight distance and service ratings were analyzed to understand their relationship with satisfaction.
* Departure and arrival delays were analyzed to compare the experience of satisfied and dissatisfied passengers.
* Service-level analysis helps identify stronger and weaker areas of the passenger experience.

## Visualizations

The project includes visualizations created using Matplotlib and Seaborn.

Charts include:

* Passenger satisfaction
* Satisfaction by customer type
* Satisfaction by travel type
* Satisfaction by class
* Satisfaction by gender
* Satisfaction by age group
* Average service ratings
* Flight distance distribution
* Delay distributions
* Average delays by satisfaction
* Correlation heatmap

All generated charts are stored in the `charts` folder.

## Project Structure

```text
Airline-Data-Analysis/
│
├── Airlinr_analysis.py
├── Invistico_Airline.csv
├── charts/
│   ├── average_service_ratings.png
│   ├── satisfaction_by_class.png
│   ├── satisfaction_by_travel_type.png
│   ├── satisfaction_by_customer_type.png
│   ├── satisfaction_by_gender.png
│   ├── satisfaction_by_age_group.png
│   ├── flight_distance_distribution.png
│   ├── departure_delay_distribution.png
│   ├── arrival_delay_distribution.png
│   ├── delays_by_satisfaction.png
│   ├── lowest_rated_services.png
│   └── correlation_heatmap.png
│
└── README.md
```

## How to Run

Install the required Python libraries:

```bash
pip install pandas matplotlib seaborn numpy
```

Keep the dataset in the same folder as the Python file.

Run the project using:

```bash
python Airlinr_analysis.py
```

The analysis results will be displayed in the terminal and the generated charts will be saved inside the `charts` folder.

## Project Outcome

This project demonstrates an end-to-end Python data analysis workflow:

**Data Loading → Data Cleaning → Exploratory Data Analysis → Visualization → Insights**

The project provides practical experience in analyzing customer satisfaction data and presenting data-driven insights using Python.

## Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Manipulation with Pandas
* Data Visualization
* Statistical Analysis
* Categorical Analysis
* Correlation Analysis
* Business Insight Generation
