import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020],
    'Sales': [50, 60, 70, 80, 90, 100]
}

# Create a Seaborn line plot
sns.lineplot(x='Year', y='Sales', data=data)

# Add labels and title
plt.title('Yearly Sales Growth')
plt.xlabel('Year')
plt.ylabel('Sales (in units)')

# Show the plot
plt.show()
