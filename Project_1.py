# Product Performance Dashboard-Project

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

ecommerce_data = {
    "Product_ID": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010"],
    "Product_Name": [
        "Wireless Mouse", "Yoga Mat", "Bluetooth Speaker", "Cotton T-shirt", "Stainless Water Bottle",
        "Noise Cancelling Headphones", "Leather Wallet", "LED Desk Lamp", "Running Shoes", "Smart Watch"],
    "Category": [
        "Electronics", "Fitness", "Electronics", "Apparel", "Home",
        "Electronics", "Accessories", "Home", "Apparel", "Electronics"],
    "Price": [799, 499, 1499, 299, 399, 3499, 899, 699, 1999, 2499],
    "Discount (%)": [10, 5, 15, 25, 8, 20, 12, 10, 18, 22],
    "Rating": [4.3, 4.0, 4.6, 3.9, 4.1, 4.7, 4.2, 4.5, 4.4, 4.6],
    "Reviews": [231, 85, 300, 110, 67, 450, 155, 210, 390, 510],
    "In_Stock": ["Yes", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes"],
    "Return_Rate (%)": [2.1, 3.2, 1.7, 6.3, 2.5, 1.9, 2.8, 2.0, 3.0, 2.2],
    "Delivery_Days": [4, 3, 5, 2, 3, 6, 4, 3, 5, 4],
    "Sales" : [120, 60, 180, 90, 40, 200, 75, 130, 160, 220]
}




x=pd.DataFrame(ecommerce_data)
print(x)

numeric_data = x.select_dtypes(include='number')
corr = numeric_data.corr()

# Total Revenue
x["Total_revenue"] = x["Price"] * (1 - x["Discount (%)"]/100) * x["Sales"]
print(x)

# Average Rating Per Category

x["Average_Rating"]=x.groupby("Category")["Rating"].transform("mean")
print(x)

# Return rate comparison across categories

x["Comparison"]=x.groupby("Category")["Return_Rate (%)"].transform("mean")
print(x)

# Bar plot of product vs average rating
a=sns.barplot(x="Product_Name",y="Average_Rating",data=x)
plt.xlabel("Product Name")
plt.ylabel("Average Rating")
plt.grid(True)
plt.title("Product vs Average rating")
plt.xticks(rotation=95)
plt.show()

# Heatmap of category vs. return rate
b=sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Average Rating Per Category")
plt.show()


# Line chart of products by revenue
c=sns.lineplot(x="Product_Name",y="Total_revenue",data=x,markers="o")
plt.xlabel("Product Name")
plt.ylabel("Total revenue")
plt.xticks(rotation=95)
plt.grid(True)
plt.show()