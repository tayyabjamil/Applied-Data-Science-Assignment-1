import pandas as pd
import matplotlib.pyplot as plt


def read_data():
    """
    Read World cup 2023 matches data from csv file
    Extract Coloumns required for bar grpah
    """
# Load your dataset
    world_cup_data = pd.read_csv("wc_matches.csv")

# Extracting two teams and their score columns
    columns_to_extract = ['team1', 'team2', 'score1', 'score2']
    all_matches = world_cup_data[columns_to_extract]
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


def getScoresofWinningTeam(world_cup_data):
    """
    Get data of every match played by teams 
    Use getWinner function to decide which team won the match
    add winner team and winning score columns
    use group by of calculate all winning score by each team

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
teams_and_scores = getScoresofWinningTeam(world_cup_data)
# Calling Function 3
show_bar_graph(teams_and_scores)
