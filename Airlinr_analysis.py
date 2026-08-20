print("Airline Data Analysis Project Started")

import pandas as pd

df = pd.read_csv("Invistico_Airline.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()
# ==============================
# DATA CLEANING
# ==============================

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing arrival delay values with 0
df["Arrival Delay in Minutes"] = df["Arrival Delay in Minutes"].fillna(0)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ==============================
# BASIC ANALYSIS
# ==============================

print("\nPassenger Satisfaction:")
print(df["satisfaction"].value_counts())

satisfaction_percentage = (
    df["satisfaction"]
    .value_counts(normalize=True) * 100
)

print("\nSatisfaction Percentage:")
print(satisfaction_percentage.round(2))


print("\nCustomer Type:")
print(df["Customer Type"].value_counts())


print("\nType of Travel:")
print(df["Type of Travel"].value_counts())


print("\nClass:")
print(df["Class"].value_counts())


print("\nGender:")
print(df["Gender"].value_counts())
import matplotlib.pyplot as plt
import seaborn as sns


# ==============================
# 1. SATISFACTION BY CUSTOMER TYPE
# ==============================

customer_satisfaction = pd.crosstab(
    df["Customer Type"],
    df["satisfaction"],
    normalize="index"
) * 100

print("\nSatisfaction by Customer Type (%):")
print(customer_satisfaction.round(2))

plt.figure(figsize=(9, 6))

customer_satisfaction.plot(
    kind="bar",
    stacked=True
)

plt.title("Passenger Satisfaction by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Percentage")
plt.xticks(rotation=0)
plt.legend(title="Satisfaction")

plt.tight_layout()
plt.show()


# ==============================
# 2. SATISFACTION BY TRAVEL TYPE
# ==============================

travel_satisfaction = pd.crosstab(
    df["Type of Travel"],
    df["satisfaction"],
    normalize="index"
) * 100

print("\nSatisfaction by Travel Type (%):")
print(travel_satisfaction.round(2))

plt.figure(figsize=(9, 6))

travel_satisfaction.plot(
    kind="bar",
    stacked=True
)

plt.title("Passenger Satisfaction by Type of Travel")
plt.xlabel("Type of Travel")
plt.ylabel("Percentage")
plt.xticks(rotation=0)
plt.legend(title="Satisfaction")

plt.tight_layout()
plt.show()


# ==============================
# 3. SATISFACTION BY CLASS
# ==============================

class_satisfaction = pd.crosstab(
    df["Class"],
    df["satisfaction"],
    normalize="index"
) * 100

print("\nSatisfaction by Class (%):")
print(class_satisfaction.round(2))

plt.figure(figsize=(9, 6))

class_satisfaction.plot(
    kind="bar",
    stacked=True
)

plt.title("Passenger Satisfaction by Class")
plt.xlabel("Class")
plt.ylabel("Percentage")
plt.xticks(rotation=0)
plt.legend(title="Satisfaction")

plt.tight_layout()
plt.show()
# ============================================================
# AIRLINE DATA ANALYSIS PROJECT
# Remaining EDA + Visualizations + Final Insights
# ============================================================

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create folder for charts
os.makedirs("charts", exist_ok=True)

# Set visual style
sns.set_theme(style="whitegrid")


# ============================================================
# 4. SERVICE RATINGS ANALYSIS
# ============================================================

service_columns = [
    "Seat comfort",
    "Departure/Arrival time convenient",
    "Food and drink",
    "Gate location",
    "Inflight wifi service",
    "Inflight entertainment",
    "Online support",
    "Ease of Online booking",
    "On-board service",
    "Leg room service",
    "Baggage handling",
    "Checkin service",
    "Cleanliness",
    "Online boarding"
]

service_means = df[service_columns].mean().sort_values(ascending=False)

print("\nAverage Service Ratings:")
print(service_means.round(2))


# Service ratings chart
plt.figure(figsize=(12, 7))

service_means.sort_values().plot(kind="barh")

plt.title("Average Rating of Airline Services")
plt.xlabel("Average Rating")
plt.ylabel("Service")

plt.tight_layout()
plt.savefig("charts/average_service_ratings.png", dpi=300)
plt.show()


# ============================================================
# 5. SATISFACTION BY GENDER
# ============================================================

gender_satisfaction = pd.crosstab(
    df["Gender"],
    df["satisfaction"],
    normalize="index"
) * 100

print("\nSatisfaction by Gender (%):")
print(gender_satisfaction.round(2))

plt.figure(figsize=(8, 6))

gender_satisfaction.plot(
    kind="bar",
    stacked=True
)

plt.title("Passenger Satisfaction by Gender")
plt.xlabel("Gender")
plt.ylabel("Percentage")
plt.xticks(rotation=0)
plt.legend(title="Satisfaction")

plt.tight_layout()
plt.savefig("charts/satisfaction_by_gender.png", dpi=300)
plt.show()


# ============================================================
# 6. SATISFACTION BY AGE GROUP
# ============================================================

df["Age Group"] = pd.cut(
    df["Age"],
    bins=[0, 18, 30, 45, 60, 100],
    labels=[
        "Under 18",
        "18-30",
        "31-45",
        "46-60",
        "60+"
    ]
)

age_satisfaction = pd.crosstab(
    df["Age Group"],
    df["satisfaction"],
    normalize="index"
) * 100

print("\nSatisfaction by Age Group (%):")
print(age_satisfaction.round(2))

plt.figure(figsize=(9, 6))

age_satisfaction.plot(
    kind="bar",
    stacked=True
)

plt.title("Passenger Satisfaction by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Percentage")
plt.xticks(rotation=0)
plt.legend(title="Satisfaction")

plt.tight_layout()
plt.savefig("charts/satisfaction_by_age_group.png", dpi=300)
plt.show()


# ============================================================
# 7. FLIGHT DISTANCE ANALYSIS
# ============================================================

print("\nFlight Distance Summary:")
print(df["Flight Distance"].describe().round(2))

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Flight Distance",
    bins=30
)

plt.title("Distribution of Flight Distance")
plt.xlabel("Flight Distance")
plt.ylabel("Number of Passengers")

plt.tight_layout()
plt.savefig("charts/flight_distance_distribution.png", dpi=300)
plt.show()


# ============================================================
# 8. FLIGHT DISTANCE BY SATISFACTION
# ============================================================

distance_satisfaction = df.groupby(
    "satisfaction"
)["Flight Distance"].mean()

print("\nAverage Flight Distance by Satisfaction:")
print(distance_satisfaction.round(2))

plt.figure(figsize=(8, 6))

distance_satisfaction.plot(kind="bar")

plt.title("Average Flight Distance by Satisfaction")
plt.xlabel("Satisfaction")
plt.ylabel("Average Flight Distance")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("charts/flight_distance_by_satisfaction.png", dpi=300)
plt.show()


# ============================================================
# 9. DEPARTURE DELAY ANALYSIS
# ============================================================

print("\nDeparture Delay Summary:")
print(df["Departure Delay in Minutes"].describe().round(2))

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Departure Delay in Minutes",
    bins=40
)

plt.xlim(0, 100)

plt.title("Distribution of Departure Delays")
plt.xlabel("Departure Delay (Minutes)")
plt.ylabel("Number of Passengers")

plt.tight_layout()
plt.savefig("charts/departure_delay_distribution.png", dpi=300)
plt.show()


# ============================================================
# 10. ARRIVAL DELAY ANALYSIS
# ============================================================

print("\nArrival Delay Summary:")
print(df["Arrival Delay in Minutes"].describe().round(2))

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Arrival Delay in Minutes",
    bins=40
)

plt.xlim(0, 100)

plt.title("Distribution of Arrival Delays")
plt.xlabel("Arrival Delay (Minutes)")
plt.ylabel("Number of Passengers")

plt.tight_layout()
plt.savefig("charts/arrival_delay_distribution.png", dpi=300)
plt.show()


# ============================================================
# 11. DELAY BY SATISFACTION
# ============================================================

delay_comparison = df.groupby(
    "satisfaction"
)[
    [
        "Departure Delay in Minutes",
        "Arrival Delay in Minutes"
    ]
].mean()

print("\nAverage Delays by Satisfaction:")
print(delay_comparison.round(2))

delay_comparison.plot(
    kind="bar",
    figsize=(9, 6)
)

plt.title("Average Flight Delays by Passenger Satisfaction")
plt.xlabel("Satisfaction")
plt.ylabel("Average Delay (Minutes)")
plt.xticks(rotation=0)
plt.legend(
    title="Delay Type",
    labels=["Departure Delay", "Arrival Delay"]
)

plt.tight_layout()
plt.savefig("charts/delays_by_satisfaction.png", dpi=300)
plt.show()


# ============================================================
# 12. SATISFACTION BY TRAVEL TYPE
# ============================================================

travel_satisfaction = pd.crosstab(
    df["Type of Travel"],
    df["satisfaction"],
    normalize="index"
) * 100

print("\nSatisfaction by Travel Type (%):")
print(travel_satisfaction.round(2))

travel_satisfaction.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 6)
)

plt.title("Passenger Satisfaction by Type of Travel")
plt.xlabel("Type of Travel")
plt.ylabel("Percentage")
plt.xticks(rotation=0)
plt.legend(title="Satisfaction")

plt.tight_layout()
plt.savefig("charts/satisfaction_by_travel_type.png", dpi=300)
plt.show()


# ============================================================
# 13. SATISFACTION BY CLASS
# ============================================================

class_satisfaction = pd.crosstab(
    df["Class"],
    df["satisfaction"],
    normalize="index"
) * 100

print("\nSatisfaction by Class (%):")
print(class_satisfaction.round(2))

class_satisfaction.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 6)
)

plt.title("Passenger Satisfaction by Class")
plt.xlabel("Class")
plt.ylabel("Percentage")
plt.xticks(rotation=0)
plt.legend(title="Satisfaction")

plt.tight_layout()
plt.savefig("charts/satisfaction_by_class.png", dpi=300)
plt.show()


# ============================================================
# 14. CUSTOMER TYPE VS SATISFACTION
# ============================================================

customer_satisfaction = pd.crosstab(
    df["Customer Type"],
    df["satisfaction"],
    normalize="index"
) * 100

print("\nSatisfaction by Customer Type (%):")
print(customer_satisfaction.round(2))

customer_satisfaction.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 6)
)

plt.title("Passenger Satisfaction by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Percentage")
plt.xticks(rotation=0)
plt.legend(title="Satisfaction")

plt.tight_layout()
plt.savefig("charts/satisfaction_by_customer_type.png", dpi=300)
plt.show()


# ============================================================
# 15. TOP SERVICE AREAS FOR SATISFIED PASSENGERS
# ============================================================

satisfied_df = df[df["satisfaction"] == "satisfied"]

satisfied_service_means = (
    satisfied_df[service_columns]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Service Ratings - Satisfied Passengers:")
print(satisfied_service_means.round(2))


# ============================================================
# 16. LOWEST RATED SERVICES
# ============================================================

lowest_services = service_means.sort_values().head(5)

print("\nLowest Rated Services:")
print(lowest_services.round(2))

lowest_services.sort_values().plot(
    kind="barh",
    figsize=(9, 6)
)

plt.title("Lowest Rated Airline Services")
plt.xlabel("Average Rating")
plt.ylabel("Service")

plt.tight_layout()
plt.savefig("charts/lowest_rated_services.png", dpi=300)
plt.show()


# ============================================================
# 17. SATISFACTION BY CLASS + TRAVEL TYPE
# ============================================================

class_travel_satisfaction = pd.crosstab(
    [df["Class"], df["Type of Travel"]],
    df["satisfaction"],
    normalize="index"
) * 100

print("\nSatisfaction by Class and Travel Type (%):")
print(class_travel_satisfaction.round(2))


# ============================================================
# 18. CORRELATION ANALYSIS
# ============================================================

numeric_columns = [
    "Age",
    "Flight Distance",
    "Seat comfort",
    "Departure/Arrival time convenient",
    "Food and drink",
    "Gate location",
    "Inflight wifi service",
    "Inflight entertainment",
    "Online support",
    "Ease of Online booking",
    "On-board service",
    "Leg room service",
    "Baggage handling",
    "Checkin service",
    "Cleanliness",
    "Online boarding",
    "Departure Delay in Minutes",
    "Arrival Delay in Minutes"
]

correlation = df[numeric_columns].corr()

plt.figure(figsize=(14, 10))

sns.heatmap(
    correlation,
    cmap="coolwarm",
    center=0
)

plt.title("Correlation Between Numerical Variables")

plt.tight_layout()
plt.savefig("charts/correlation_heatmap.png", dpi=300)
plt.show()


# ============================================================
# 19. FINAL PROJECT SUMMARY
# ============================================================

total_passengers = len(df)

satisfied_count = (
    df["satisfaction"] == "satisfied"
).sum()

dissatisfied_count = (
    df["satisfaction"] == "dissatisfied"
).sum()

satisfaction_rate = (
    satisfied_count / total_passengers
) * 100

top_class = df["Class"].value_counts().idxmax()

top_travel_type = df["Type of Travel"].value_counts().idxmax()

top_customer_type = df["Customer Type"].value_counts().idxmax()

average_flight_distance = df["Flight Distance"].mean()

average_departure_delay = (
    df["Departure Delay in Minutes"].mean()
)

average_arrival_delay = (
    df["Arrival Delay in Minutes"].mean()
)


print("\n")
print("=" * 60)
print("AIRLINE DATA ANALYSIS PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"\nTotal Passengers: {total_passengers:,}")

print(
    f"Satisfied Passengers: "
    f"{satisfied_count:,} ({satisfaction_rate:.2f}%)"
)

print(
    f"Dissatisfied Passengers: "
    f"{dissatisfied_count:,} "
    f"({100 - satisfaction_rate:.2f}%)"
)

print(f"Most Common Class: {top_class}")

print(f"Most Common Travel Type: {top_travel_type}")

print(f"Most Common Customer Type: {top_customer_type}")

print(
    f"Average Flight Distance: "
    f"{average_flight_distance:.2f}"
)

print(
    f"Average Departure Delay: "
    f"{average_departure_delay:.2f} minutes"
)

print(
    f"Average Arrival Delay: "
    f"{average_arrival_delay:.2f} minutes"
)

print("\nTop 5 Services by Average Rating:")

for service, rating in service_means.head(5).items():
    print(f"- {service}: {rating:.2f}")

print("\nLowest 5 Services by Average Rating:")

for service, rating in lowest_services.items():
    print(f"- {service}: {rating:.2f}")

print("\nCharts saved in: charts")

print("\n" + "=" * 60)
print("PROJECT FINISHED")
print("=" * 60)