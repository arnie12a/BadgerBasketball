import streamlit as st
import pandas as pd

def AboutPlayers(df):
    cols = ['Player', '#', 'Class', 'Height', 'Weight', 'Summary']
    return df[cols]
    

def EachGameStatistics(df):
    return

def PerGamePlayerStatistics(df):
    return

def PerGameTeamStatistics(df):
    return

def getData(year):

    aboutPlayers = pd.read_csv('./data/about_players/about_players_' + year + '.csv')
    aboutPlayers = aboutPlayers[aboutPlayers['seasonYear'] == int(year)]
    aboutPlayers = AboutPlayers(aboutPlayers)

    eachGameStats = pd.read_csv('./data/each_game_stats/each_game_stats_' + year + '.csv')
    eachGameStats = eachGameStats[eachGameStats['seasonYear'] == int(year)]

    perGamePlayerStats = pd.read_csv('./data/per_game_player_stats/per_game_player_stats' + year + '.csv')
    perGamePlayerStats = perGamePlayerStats[perGamePlayerStats['seasonYear'] == int(year)]

    perGameTeamStats = pd.read_csv('./data/per_game_team_stats/per_game_team_stats_' + year + '.csv')
    perGameTeamStats = perGameTeamStats[perGameTeamStats['seasonYear'] == int(year)]

    return aboutPlayers, eachGameStats, perGamePlayerStats, perGameTeamStats

# Sidebar title
st.sidebar.title("Badger Basketball Analysis")

# Dropdown with 6 options
option = st.sidebar.selectbox(
    "Select a year:",
    ("2020", "2021", "2022", "2023", "2024", "2025")
)

# Conditional inputs based on option
if option == "2020":
    pass
elif option == "2021":
    pass
elif option == "2022":
    pass
elif option == "2023":
    pass
elif option == "2024":
    pass
elif option == "2025":
    pass

# Submit button
submit = st.sidebar.button("Submit")

# Display dummy output
if submit:
    if option == "2020":
        df1, df2, df3, df4 = getData(option)
        st.dataframe(df1)
        st.dataframe(df2)
        st.dataframe(df3)
        st.dataframe(df4)

    elif option == "2021":
        df1, df2, df3, df4 = getData(option)
        st.dataframe(df1)
        st.dataframe(df2)
        st.dataframe(df3)
        st.dataframe(df4)

    elif option == "2022":
        df1, df2, df3, df4 = getData(option)
        st.dataframe(df1)
        st.dataframe(df2)
        st.dataframe(df3)
        st.dataframe(df4)

    elif option == "2023":
        df1, df2, df3, df4 = getData(option)
        st.dataframe(df1)
        st.dataframe(df2)
        st.dataframe(df3)
        st.dataframe(df4)

    elif option == "2024":
        df1, df2, df3, df4 = getData(option)
        st.dataframe(df1)
        st.dataframe(df2)
        st.dataframe(df3)
        st.dataframe(df4)

    elif option == "2025":
        df1, df2, df3, df4 = getData(option)
        st.dataframe(df1)
        st.dataframe(df2)
        st.dataframe(df3)
        st.dataframe(df4)