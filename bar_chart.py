import pandas as pd
import matplotlib.pyplot as plt


def clean_data(world_cup_data):
    """
    This function takes data as parameter, loops through all row items,
    and removes rows that contain non-numeric or 'NAN' values.
    The cleaned data is converted into a DataFrame for plotting.
    """
    cleaned_data = []

    for index, row in world_cup_data.iterrows():
        is_valid_row = True

        # Check each column in the row
        for column in world_cup_data.columns:
            cell_value = row[column]

            # Check if the cell is None or contains 'NAN' as a string
            if cell_value is None or cell_value == "NAN":
                is_valid_row = False
                break

        if is_valid_row:
            cleaned_data.append(row)

    cleaned_data_frame = pd.DataFrame(
        cleaned_data, columns=world_cup_data.columns)
    return cleaned_data_frame


def read_data():
    """
    Read World cup 2023 matches data from csv file
    Pass data to clean function to exclude any entry
    with value NAN
    Extract Columns required for bar graph
    """
    # Load your dataset
    world_cup_data = pd.read_csv("wc_matches.csv")
    # Calling clean_data function
    cleaned_data = clean_data(world_cup_data)

    # Extracting two teams and their score columns
    columns_to_extract = ['team1', 'team2', 'score1', 'score2']
    all_matches = cleaned_data[columns_to_extract]
    dataframe_allmatches = pd.DataFrame(all_matches)
    return dataframe_allmatches


# Create a function to determine the winner
def get_winner(row):
    if row['score1'] > row['score2']:
        return row['team1'], row['score1']
    elif row['score1'] < row['score2']:
        return row['team2'], row['score2']
    else:
        return row['score2']


# Apply the function to each row to get the winners
def get_scores_of_winning_team(world_cup_data):
    """
    Get data of every match played by teams
    Use get_winner function to decide which team won the match
    add winner team and winning score columns
    use group by to calculate all winning score by each team
    """
    world_cup_data[['winner', 'winning_score']] = world_cup_data.apply(
        get_winner, axis=1, result_type='expand')
    world_cup_data['winning_score'] = world_cup_data['winning_score'].astype(
        int)
    # Display the winners and winning scores
    team_total_score = world_cup_data.groupby(
        'team1')[['winning_score']].sum().reset_index()
    # Display the winners
    teams_and_scores = team_total_score.sort_values(
        by='winning_score', ascending=False)
    return teams_and_scores


def show_bar_graph(teams_and_scores):
    plt.figure(figsize=(12, 6))

    plt.bar(teams_and_scores['team1'], teams_and_scores['winning_score'])

    plt.xlabel('Teams')
    plt.xticks(rotation=90)
    plt.ylabel('Total Score')
    plt.title('Football World Cup 2023 Goals Scored by Each Team ')

    plt.xticks(rotation=90)

    plt.show()


# Calling Function 1
world_cup_data = read_data()
# Calling Function 2
teams_and_scores = get_scores_of_winning_team(world_cup_data)
# Calling Function 3
show_bar_graph(teams_and_scores)
