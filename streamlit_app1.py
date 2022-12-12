import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
st.set_page_config(layout="wide")

st.header("MLB Starting Pitcher Comparision Tool")
@st.cache
def get_data():
    path = r'Pitching.csv'
    return pd.read_csv(path)
df = get_data()
df2= get_data()
tab1, tab2, tab3= st.tabs(["Player Comparision", "select player 1", "select player 2"])
with tab2:
    years = df['yearID'].drop_duplicates()
    year_choice = st.selectbox('Please select a year', years) 
    teams = df["TeamName"].loc[df["yearID"] == year_choice].drop_duplicates()
    team_choice = st.selectbox('Please Select a team:', teams)

    st.header(f" Pitching Stats for the {team_choice} in {year_choice} ")



    #placeholder
    startdf = df[(df.yearID == year_choice) & (df.TeamName == team_choice) & (df.GS >= 1) ] 
    player = st.selectbox("Please Select a player",startdf['FullName'])
    list = st.write(startdf[["FullName","ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]])
    teamrankavg = startdf[["ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]].mean()
    player1stats = startdf[(df.FullName == player)]
    playerstatsavg = player1stats[["ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]].mean()
    st.write(player1stats)
with tab3:
    years2 = df2['yearID'].drop_duplicates()
    year_choice2 = st.selectbox('Please select a year for player 2', years2) 
    teams2 = df2["TeamName"].loc[df2["yearID"] == year_choice2].drop_duplicates()
    team_choice2 = st.selectbox('Please Select a team for player 2:', teams2)

    st.header(f" Pitching Stats for the {team_choice2} in {year_choice2} ")

    year2df = df2[(df2.yearID == year_choice2)]
    #placeholder
    startdf2 = df2[(df2.yearID == year_choice2) & (df2.TeamName == team_choice2) & (df2.GS >= 1) ] 
    player2 = st.selectbox("Please Select a 2nd player",startdf2['FullName'])
    list2 = st.write(startdf2[["FullName","ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]])
    teamrankavg = startdf2[["ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]].mean()
    player2stats = startdf2[(df2.FullName == player2)]
    playerstatsavg = player2stats[["ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]].mean()
    st.write(player2stats)
with tab1:
    st.write("Please select a player on each of the tabs to generate the comparion below")
    comparision = pd.concat([player1stats,player2stats])
    st.header(f" You Have selected {year_choice} {player} and {year_choice2} {player2}")
    
    ChartERA = alt.Chart(comparision).mark_bar().encode(
        x='FullName:N',
        y='ERA:Q',
        color='FullName:N',
        )
    ChartSO = alt.Chart(comparision).mark_bar().encode(
        x='FullName:N',
        y='SO:Q',
        color='FullName:N',
        )    
    ChartW = alt.Chart(comparision).mark_bar().encode(
        x='FullName:N',
        y='W:Q',
        color='FullName:N',
        ) 
    ChartL = alt.Chart(comparision).mark_bar().encode(
        x='FullName:N',
        y='L:Q',
        color='FullName:N',
        ) 
    ChartG = alt.Chart(comparision).mark_bar().encode(
        x='FullName:N',
        y='G:Q',
        color='FullName:N',
        ) 
    ChartH = alt.Chart(comparision).mark_bar().encode(
        x='FullName:N',
        y='H:Q',
        color='FullName:N',
        ) 
    ChartER = alt.Chart(comparision).mark_bar().encode(
        x='FullName:N',
        y='ER:Q',
        color='FullName:N',
        ) 
    ChartHR = alt.Chart(comparision).mark_bar().encode(
        x='FullName:N',
        y='HR:Q',
        color='FullName:N',
        ) 
    ChartBB = alt.Chart(comparision).mark_bar().encode(
        x='FullName:N',
        y='BB:Q',
        color='FullName:N',
        ) 
    ChartIPouts = alt.Chart(comparision).mark_bar().encode(
        x='FullName:N',
        y='IPouts:Q',
        color='FullName:N',
        ) 
    charts = st.altair_chart(ChartERA | ChartSO | ChartW | ChartL | ChartG | ChartH | ChartBB | ChartHR |ChartER |ChartIPouts)    
    st.write(charts)
