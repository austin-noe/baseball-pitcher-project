import configuration as config
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.graph_objects as go
import plotly.offline as pyo
import numpy as np
import plotly as pl

@st.cache
def get_data():
    path = r'Pitching.csv'
    return pd.read_csv(path)
df = get_data()

years = df['yearID'].drop_duplicates()
year_choice = st.sidebar.selectbox('select year', years) 
teams = df["TeamName"].loc[df["yearID"] == year_choice].drop_duplicates()
team_choice = st.sidebar.selectbox('Select your team:', teams)

st.header(f" Pitching Stats for the {team_choice} in {year_choice} ")

yeardf = df[(df.yearID == year_choice) & (df.IPouts >= 125)]

yearrank = yeardf[["FullName","TeamName","ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]]
yearrankavg = yearrank[["ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]].mean()
stats = [" ","ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]



#placeholder
PitcherType = [" ", "Starting", "Relief"]
pitchtype = st.selectbox('Pitcher Type', PitcherType)
if pitchtype == "Starting":
    startdf = df[(df.yearID == year_choice) & (df.TeamName == team_choice) & (df.IPouts >= 125) & (df.GS > 0)] 
    list = st.write(startdf[["FullName","ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]])
    player = st.selectbox("Please Select a player",startdf['FullName'])
    teamrankavg = startdf[["ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]].mean()
    playerstats = startdf[(df.FullName == player)]
    playerstatsavg = playerstats[["ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]].mean()
    st.write(playerstatsavg)
    import pandas as pd
    from matplotlib import pyplot as plt
    graph = (
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    df1 = playerstatsavg

    df2 = teamrankavg

    ax = df1.plot(x='stat', y='avg')
    df2.plot(ax=ax, x='subject', y='marks'))

    st.write(plt.show(graph))
   


elif pitchtype == "Relief" :
    reliefdf = df[(df.yearID == year_choice) & (df.TeamName == team_choice) & (df.IPouts >= 75) & (df.GS == 0)] 
    list = st.write(reliefdf[["FullName","ERA","R","W","L","G","GS","CG","SHO","SV","IPouts","H","ER","HR","BB","SO"]])
    player = st.selectbox("Please Select a player",reliefdf['FullName']) 