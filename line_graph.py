import matplotlib.pyplot as plt
import pandas as pd


def read_data():
    """
    Read UK crime data from year 1960 to 2014 from CSV File
    """
    # Read the CSV file using pandas
    UK_crime_data = pd.read_csv("US_Crime_Rates_1960_2014.csv")
    UK_crime_data = UK_crime_data.iloc[::3]

    # Extracting the 'Year' column
    years = UK_crime_data['Year']
    columns_to_extract = ['Violent', 'Property', 'Murder', 'Forcible_Rape',
                          'Robbery', 'Aggravated_assault', 'Burglary', 'Larceny_Theft', 'Vehicle_Theft']
    # Extracting columns of different crime categories
    crimes = UK_crime_data[columns_to_extract]

    return years, crimes


def line_graph(years, crimes):
    """
    Plot line graph for different Crime categories against year
    """
    for crime_category in crimes:
        plt.plot(years, crimes[crime_category], label=crime_category)


plt.figure(figsize=(12, 6))

# Calling Function 1 to read, extract
years, crimes = read_data()
# Calling Function 2 to plot line graph
line_graph(years, crimes)

plt.title('Crime Trends Over the Years (1960-2014)')
plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.legend(loc='upper left')
plt.show()
