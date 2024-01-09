# To-dos
# 1. Refactor to pass values from lookups.py thru the code
# 2. Create place to spit out pick data

# *************************


import numpy as np
import pandas as pd
import streamlit as st
import lookups
import json
import config
from google.oauth2 import service_account
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(layout="wide")

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
st.title("NFL 2024 Playoff Picker")

st.header("What is your name?", divider=True)
name = st.text_input("Name")

st.subheader('1. Wild Card Picks', divider=True)

with st.expander("Choose Your Wild Card Winners First"):
    buffer1, col_wca, buffer2, col_wcn, buffer3= st.columns(5)

    with col_wca:
        with st.form(key='wca'):
            st.subheader("AFC Wild Card Games")
            st.image(lookups.afc_logo)

            afc_wc1_select = st.selectbox(
                "AFC Wild Card 1",
                (str(df_teams.loc[df_teams["slug"] == afc7]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc7]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == afc2]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc2]["name"].values[0])),
                index= None, placeholder="Who Wins?")

            afc_wc2_select = st.selectbox(
                "AFC Wild Card 2",
                (
                str(df_teams.loc[df_teams["slug"] == afc6]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc6]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == afc3]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc3]["name"].values[0])),
                index= None, placeholder="Who Wins?")

            afc_wc3_select = st.selectbox(
                "AFC Wild Card 3",
                (
                str(df_teams.loc[df_teams["slug"] == afc5]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc5]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == afc4]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc4]["name"].values[0])),
                index= None, placeholder="Who Wins?")

            submitButton = st.form_submit_button(label = 'Select AFC Wild Card Picks')
            if submitButton:
                st.toast('Your AFC Wild Card Picks have been recorded!', icon = '✅')

    with col_wcn:
        with st.form(key='wcn'):
            st.subheader("NFC Wild Card Games")
            st.image(lookups.nfc_logo)

            nfc_wc1_select = st.selectbox(
                "NFC Wild Card 1",
                (
                str(df_teams.loc[df_teams["slug"] == nfc7]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc7]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == nfc2]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc2]["name"].values[0])),
                index= None, placeholder="Who Wins?")

            nfc_wc2_select = st.selectbox(
                "NFC Wild Card 2",
                (
                str(df_teams.loc[df_teams["slug"] == nfc6]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc6]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == nfc3]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc3]["name"].values[0])),
                index= None, placeholder="Who Wins?")

            nfc_wc3_select = st.selectbox(
                "NFC Wild Card 3",
                (
                str(df_teams.loc[df_teams["slug"] == nfc5]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc5]["name"].values[0]), 
                str(df_teams.loc[df_teams["slug"] == nfc4]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc4]["name"].values[0])),
                index= None, placeholder="Who Wins?")

            submitButton = st.form_submit_button(label = 'Select NFC Wild Card Picks')
            if submitButton:
                st.toast('Your NFC Wild Card Picks have been recorded!', icon = '✅')

st.subheader('2. Divisional Round Picks', divider=True)

with st.expander("Choose Your Divisional Round Winners Second"):
    buffer4, col_diva, buffer5, col_divn, buffer6= st.columns(5)

    try:
        nfc_div_teams = [nfc_wc1_select, nfc_wc2_select, nfc_wc3_select, \
            str(df_teams.loc[df_teams["slug"] == nfc1]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc1]["name"].values[0])]
        nfc_div_teams.sort()

        afc_div_teams = [afc_wc1_select, afc_wc2_select, afc_wc3_select, \
            str(df_teams.loc[df_teams["slug"] == afc1]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc1]["name"].values[0])]
        afc_div_teams.sort()

        with col_diva:
            with st.form(key='diva'):
                st.subheader("AFC Divisional Games")
                st.image(lookups.afc_logo)

                afc_div1_select = st.selectbox(
                    "AFC Divisional 1",
                    (afc_div_teams[3], afc_div_teams[0]), index= None, placeholder="Who Wins?")

                afc_div2_select = st.selectbox(
                    "AFC Divisional 2",
                    (afc_div_teams[2], afc_div_teams[1]), index= None, placeholder="Who Wins?")

                submitButton = st.form_submit_button(label = 'Select AFC Divisional Picks')
                if submitButton:
                    st.toast('Your AFC Divisional Round Picks have been recorded!', icon = '✅')

        with col_divn:
            with st.form(key='divn'):
                st.subheader("NFC Divisional Games")
                st.image(lookups.nfc_logo)

                nfc_div1_select = st.selectbox(
                    "NFC Divisional 1",
                    (nfc_div_teams[3], nfc_div_teams[0]),index= None, placeholder="Who Wins?")

                nfc_div2_select = st.selectbox(
                    "NFC Divisional 2",
                    ('Who Wins?', nfc_div_teams[2], nfc_div_teams[1]))

                submitButton = st.form_submit_button(label = 'Select NFC Divisional Picks')
                if submitButton:
                    st.toast('Your NFC Divisional Round Picks have been recorded!', icon = '✅')

    except:
        st.write("Choose your Wild Card Winners first!")

st.subheader('3. Conference Championship Picks', divider=True)
with st.expander("Choose Your Conference Champions Third"):
    buffer7, col_confa, buffer8, col_confn, buffer9= st.columns(5)
    try:
        nfc_conf_teams = [nfc_div1_select, nfc_div2_select]
        nfc_conf_teams.sort()

        afc_conf_teams = [afc_div1_select, afc_div2_select]
        afc_conf_teams.sort()

        with col_confa:
            with st.form(key='confa'):
                st.subheader("AFC Championship Game")
                st.image(lookups.afc_logo)

                afc_champ_select = st.selectbox(
                    "AFC Champion",
                    (afc_conf_teams[1], afc_conf_teams[0]), index= None, placeholder="Who Wins?")

                submitButton = st.form_submit_button(label = 'Select AFC Champion')
                if submitButton:
                    st.toast('Your AFC Champion has been recorded!', icon = '✅')

        with col_confn:
            with st.form(key='confn'):
                st.subheader("NFC Championship Game")
                st.image(lookups.nfc_logo)

                nfc_champ_select = st.selectbox(
                    "NFC Champion",
                    (nfc_conf_teams[1], nfc_conf_teams[0]), index= None, placeholder="Who Wins?")

                submitButton = st.form_submit_button(label = 'Select NFC Champion')
                if submitButton:
                    st.toast('Your NFC Champion has been recorded!', icon = '✅')
    except:
        st.write('Choose the Divisional winners first!')

st.subheader('4. Pro Bowl Games Pick', divider=True)
with st.expander("Choose Your Pro Bowl Games Winner"):
    buffer10, col_pb, buffer11= st.columns(3)

    with col_pb:
        with st.form(key='pro_bowl'):
            st.subheader("Pro Bowl Games")
            st.image(lookups.pro_bowl_logo)

            pro_bowl_select = st.selectbox(
                "Pro Bowl Games Winner",
                ( nfcp, afcp), index= None, placeholder="Who Wins?")

            submitButton = st.form_submit_button(label = 'Select Pro Bowl Games Winner')
            if submitButton:
               st.toast('Your Pro Bowl Games Winner has been recorded!', icon = '✅')


st.subheader('5. Super Bowl Pick', divider = True)
with st.expander("Choose Your Super Bowl Champion"):
    buffer12, col_sb, buffer13= st.columns(3)

    try:
        with col_sb:
            with st.form(key='super_bowl'):
                st.subheader("Super Bowl")
                st.image(lookups.super_bowl_logo)

                super_bowl_select = st.selectbox(
                    "Super Bowl Winner",
                    (nfc_champ_select, afc_champ_select), index= None, placeholder="Who Wins?")

                submitButton = st.form_submit_button(label = 'Select Super Bowl Winner')
                if submitButton:
                    st.toast('Your Super Bowl 58 Champion has been recorded!', icon = '✅')

    except:
        st.write("Choose your Conference Champions First!")

st.subheader('6. Submit Your Bracket!', divider = True)
with st.expander("Check Your Picks and Send Them!"):
    col_picks, col_submit= st.columns(2)
    
    try:
        with col_picks:

            picks_row = [name, afc_wc1_select, afc_wc2_select, afc_wc3_select, nfc_wc1_select, nfc_wc2_select, nfc_wc3_select, \
                afc_div1_select, afc_div2_select, nfc_div1_select, nfc_div2_select, nfc_champ_select, afc_champ_select, \
                pro_bowl_select, super_bowl_select ]
            
            st.subheader("AFC Wild Card Picks")
            for pick in picks_row[1:4]:
                st.write(pick)
            st.subheader("NFC Wild Card Picks")
            for pick in picks_row[4:7]:
                st.write(pick)
            st.subheader("AFC Divisional Round Picks")
            for pick in picks_row[7:9]:
                st.write(pick)
            st.subheader("NFC Divisional Round Picks")
            for pick in picks_row[9:11]:
                st.write(pick)
            st.subheader("Conference Champion Picks")
            for pick in picks_row[11:13]:
                st.write(pick)
            st.subheader("Pro Bowl Pick")
            for pick in picks_row[13:14]:
                st.write(pick)
        

        with col_submit:
            st.subheader("Super Bowl Pick")
            buffer14, helmet, buffer15= st.columns(3)
            with helmet:
                for pick in picks_row[14:15]:
                    st.image(df_teams.loc[df_teams["name"] == pick[3:]]["helmet"].values[0])

            pick_submitButton = st.button(label = 'Submit Your Picks!', type = "primary", use_container_width=True)

            # Load the Google Sheets credentials
            scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(config.google_credentials, strict=False), scope)

            # Initialize the Google Sheets client
            client = gspread.authorize(creds)

            # Define the Google Sheet destination URL 
            sheet_url = config.google_sheet_url

            # Write the form submission to the Google Sheet
            def write_to_google_sheet(submission):
                sheet = client.open_by_url(sheet_url).sheet1
                transposed_row = [submission]
                sheet.append_rows(transposed_row)

            if pick_submitButton:
                write_to_google_sheet(picks_row)
                st.success("Picks submitted successfully!")

    except:
        st.write("Finish your Picks First!") 

# Function for after WC Week
# Function for after Div Week
# Function for after Conf Week
# Function for after Pro Bowl
# Function for end
# Date picker to choose function
# Simulator based on elo

#Something with helmets?

#************************************************************************





