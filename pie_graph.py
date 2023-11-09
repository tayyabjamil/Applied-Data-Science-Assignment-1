import pandas as pd
import matplotlib.pyplot as plt


def read_data():
    """
    Read Glassdoor jobs data with gender salaries from csv file
    Extract Columns of job title, gender, and base pay
    Group data by gender
    """
    raw_data = pd.read_csv("Glassdoor Gender Pay Gap.csv")
    glassdoor_data = pd.DataFrame(
        raw_data, columns=['JobTitle', 'Gender', 'BasePay'])
    glassdoor_data['BasePay'] = glassdoor_data['BasePay']

    # Group the data by gender
    female_data = glassdoor_data[glassdoor_data['Gender'] == 'Female']
    male_data = glassdoor_data[glassdoor_data['Gender'] == 'Male']

    return male_data, female_data


def create_pie_chart(data, title, ax):
    """
    Define color for each job category to show the same color
    for both male and female data
    plot a pie chart by grouping data with JobTitles and Basepay sum
    """
    job_title_colors = {
        'Graphic Designer': 'tab:blue',
        'Warehouse Associate': 'tab:orange',
        'Software Engineer': 'tab:green',
        'IT': 'tab:red',
        'Sales Associate': 'tab:green',
        'Driver': (0.9, 0.3, 0.1, 1),
        'Financial Analyst': 'tab:purple',
        'Marketing Associate': 'tab:brown',
        'Data Scientist': 'pink'
        # Add more job titles and colors as needed
    }

    job_titles = data['JobTitle'].unique()
    colors = [job_title_colors.get(title, 'tab:gray') for title in job_titles]

    ax.pie(data.groupby('JobTitle')['BasePay'].sum(), startangle=140, colors=colors, textprops={
           'fontsize': 25}, labels=data['JobTitle'].unique(), autopct='%1.1f%%')
    ax.set_title(title, fontsize=35)
    ax.axis('equal')


def create_sub_plot(male_data, female_data):
    fig, axes = plt.subplots(1, 2, figsize=(26, 16))
    # Create pie charts in subplots
    create_pie_chart(female_data, 'Female Percentage of Jobs', axes[0])
    fig.legend(fontsize=20, loc="upper right")
    create_pie_chart(male_data, 'Male Percentage of Jobs', axes[1])
    plt.show()


# Calling Function 1
male_data, female_data = read_data()

# Calling Function 2
create_sub_plot(male_data, female_data)
