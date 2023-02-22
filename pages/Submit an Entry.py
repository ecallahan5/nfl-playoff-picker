# To-dos
# 1. Refactor to pass values from lookups.py thru the code
# 2. Create place to spit out pick data

# *************************


import numpy as np
import pandas as pd
import streamlit as st
import lookups
st.set_page_config(layout="wide")

st.title("Thanks for Playing!  See you in 2024")
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
df_teams = pd.DataFrame(lookups.team_list)
# Input Data Model

nfc1 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "1")]["slug"].values[0]
nfc2 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "2")]["slug"].values[0]
nfc3 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "3")]["slug"].values[0]
nfc4 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "4")]["slug"].values[0]
nfc5 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "5")]["slug"].values[0]
nfc6 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "6")]["slug"].values[0]
nfc7 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "7")]["slug"].values[0]
afc1 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "1")]["slug"].values[0]
afc2 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "2")]["slug"].values[0]
afc3 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "3")]["slug"].values[0]
afc4 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "4")]["slug"].values[0]
afc5 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "5")]["slug"].values[0]
afc6 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "6")]["slug"].values[0]
afc7 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "7")]["slug"].values[0]
nfcp = "NFC"
afcp = "AFC"


# Function for the beginning
st.title("NFL 2023 Playoff Picker")

st.header("What is your name?")
name = st.text_input("Name")

st.header('1. Wild Card Simulation')

with st.expander("Choose Your Wild Card Winners First"):
    buffer1, col_wca, buffer2, col_wcn, buffer3= st.columns(5)

    with col_wca:
        with st.form(key='wca'):
            st.header("AFC Wild Card Games")
            st.image(lookups.afc_logo)

            afc_wc1_select = st.selectbox(
                "AFC Wild Card 1",
                ('Who Wins?', 
                str(df_teams.loc[df_teams["slug"] == afc7]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc7]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == afc2]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc2]["name"].values[0])))

            afc_wc2_select = st.selectbox(
                "AFC Wild Card 2",
                ('Who Wins?', 
                str(df_teams.loc[df_teams["slug"] == afc6]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc6]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == afc3]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc3]["name"].values[0])))

            afc_wc3_select = st.selectbox(
                "AFC Wild Card 3",
                ('Who Wins?', 
                str(df_teams.loc[df_teams["slug"] == afc5]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc5]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == afc4]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc4]["name"].values[0])))

            submitButton = st.form_submit_button(label = 'Submit AFC Wild Card Picks')

    with col_wcn:
        with st.form(key='wcn'):
            st.header("NFC Wild Card Games")
            st.image(lookups.nfc_logo)

            nfc_wc1_select = st.selectbox(
                "NFC Wild Card 1",
                ('Who Wins?', 
                str(df_teams.loc[df_teams["slug"] == nfc7]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc7]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == nfc2]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc2]["name"].values[0])))

            nfc_wc2_select = st.selectbox(
                "NFC Wild Card 2",
                ('Who Wins?', 
                str(df_teams.loc[df_teams["slug"] == nfc6]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc6]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == nfc3]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc3]["name"].values[0])))

            nfc_wc3_select = st.selectbox(
                "NFC Wild Card 3",
                ('Who Wins?', 
                str(df_teams.loc[df_teams["slug"] == nfc5]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc5]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == nfc4]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc4]["name"].values[0])))

            submitButton = st.form_submit_button(label = 'Submit NFC Wild Card Picks')


st.header('2. Divisional Round Simulation')

with st.expander("Choose Your Divisional Round Winners Second"):
    buffer4, col_diva, buffer5, col_divn, buffer6= st.columns(5)

    nfc_div_teams = [nfc_wc1_select, nfc_wc2_select, nfc_wc3_select, \
        str(df_teams.loc[df_teams["slug"] == nfc1]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc1]["name"].values[0])]
    nfc_div_teams.sort()

    afc_div_teams = [afc_wc1_select, afc_wc2_select, afc_wc3_select, \
        str(df_teams.loc[df_teams["slug"] == afc1]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc1]["name"].values[0])]
    afc_div_teams.sort()

    with col_diva:
        with st.form(key='diva'):
            st.header("AFC Divisional Games")
            st.image(lookups.afc_logo)

            afc_div1_select = st.selectbox(
                "AFC Divisional 1",
                ('Who Wins?', afc_div_teams[3], afc_div_teams[0]))

            afc_div2_select = st.selectbox(
                "AFC Divisional 2",
                ('Who Wins?', afc_div_teams[2], afc_div_teams[1]))

            submitButton = st.form_submit_button(label = 'Submit AFC Divisional Picks')

    with col_divn:
        with st.form(key='divn'):
            st.header("NFC Divisional Games")
            st.image(lookups.nfc_logo)

            nfc_div1_select = st.selectbox(
                "NFC Divisional 1",
                ('Who Wins?', nfc_div_teams[3], nfc_div_teams[0]))

            nfc_div2_select = st.selectbox(
                "NFC Divisional 2",
                ('Who Wins?', nfc_div_teams[2], nfc_div_teams[1]))

            submitButton = st.form_submit_button(label = 'Submit NFC Divisional Picks')

st.header('3. Conference Championship Simulation')
with st.expander("Choose Your Conference Champions Third"):
    buffer7, col_confa, buffer8, col_confn, buffer9= st.columns(5)

    nfc_conf_teams = [nfc_div1_select, nfc_div2_select]
    nfc_conf_teams.sort()

    afc_conf_teams = [afc_div1_select, afc_div2_select]
    afc_conf_teams.sort()

    with col_confa:
        with st.form(key='confa'):
            st.header("AFC Championship Game")
            st.image(lookups.afc_logo)

            afc_champ_select = st.selectbox(
                "AFC Champion",
                ('Who Wins?', afc_conf_teams[1], afc_conf_teams[0]))

            submitButton = st.form_submit_button(label = 'Submit AFC Champion')

    with col_confn:
        with st.form(key='confn'):
            st.header("NFC Championship Game")
            st.image(lookups.nfc_logo)

            nfc_champ_select = st.selectbox(
                "NFC Champion",
                ('Who Wins?', nfc_conf_teams[1], nfc_conf_teams[0]))

            submitButton = st.form_submit_button(label = 'Submit NFC Champion')

st.header('4. Pro Bowl Games Simulation')
with st.expander("Choose Your Pro Bowl Games Winner"):
    buffer10, col_pb, buffer11= st.columns(3)

    with col_pb:
        with st.form(key='pro_bowl'):
            st.header("Pro Bowl Games")
            st.image(lookups.pro_bowl_logo)

            pro_bowl_select = st.selectbox(
                "Pro Bowl Games Winner",
                ('Who Wins?', nfcp, afcp))

            submitButton = st.form_submit_button(label = 'Submit Pro Bowl Games Winner')

st.header('5. Super Bowl Simulation')
with st.expander("Choose Your Super Bowl Champion"):
    buffer12, col_sb, buffer13= st.columns(3)

    with col_sb:
        with st.form(key='super_bowl'):
            st.header("Super Bowl")
            st.image(lookups.super_bowl_logo)

            super_bowl_select = st.selectbox(
                "Super Bowl Winner",
                ('Who Wins?', nfc_champ_select, afc_champ_select))

            submitButton = st.form_submit_button(label = 'Submit Super Bowl Winner')



# Function for after WC Week
# Function for after Div Week
# Function for after Conf Week
# Function for after Pro Bowl
# Function for end
# Date picker to choose function
# Simulator based on elo

#Something with helmets?

#************************************************************************





