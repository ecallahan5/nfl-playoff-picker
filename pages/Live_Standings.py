import numpy as np
import pandas as pd
import streamlit as st
import lookups
import json
import config
from google.oauth2 import service_account
import gspread
from oauth2client.service_account import ServiceAccountCredentials

wc_winners = ["4. Houston Texans"]
div_winners = []
conf_winners = []
pro_winner = []
sb_winner = []

# Load the Google Sheets credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(config.google_credentials, strict=False), scope)
gc = gspread.authorize(credentials)

# Open the spreadsheet by URL
spreadsheet = gc.open_by_url(config.google_sheet_url)

# Select a worksheet
worksheet = spreadsheet.get_worksheet(0)

# Get all records from the worksheet
data = worksheet.get_all_records()

# Convert the data to a DataFrame
standings_df = pd.DataFrame(data)

# Points Multipliers for each Round
wc_mult = 1
div_mult = 2
conf_mult = 4
pro_mult = 1
sb_mult = 6

standings_df["wc_pts"] = np.where(standings_df["WC1"].str.strip().isin(wc_winners),wc_mult,0) + np.where(standings_df["WC2"].str.strip().isin(wc_winners),wc_mult,0) + np.where(standings_df["WC3"].str.strip().isin(wc_winners),wc_mult,0)  +\
              np.where(standings_df["WC4"].str.strip().isin(wc_winners),wc_mult,0) + np.where(standings_df["WC5"].str.strip().isin(wc_winners),wc_mult,0) + np.where(standings_df["WC6"].str.strip().isin(wc_winners),wc_mult,0) 
standings_df["div_pts"] = np.where(standings_df["D1"].str.strip().isin(div_winners),div_mult,0) + np.where(standings_df["D2"].str.strip().isin(div_winners),div_mult,0) +\
                np.where(standings_df["D3"].str.strip().isin(div_winners),div_mult,0) + np.where(standings_df["D4"].str.strip().isin(div_winners),div_mult,0)
standings_df["conf_pts"] = np.where(standings_df["AFC"].str.strip().isin(conf_winners),conf_mult,0) + np.where(standings_df["NFC"].str.strip().isin(conf_winners),conf_mult,0) 
standings_df["pro_pts"] = np.where(standings_df["PB"].str.strip().isin(pro_winner),pro_mult,0)
standings_df["sb_pts"] = np.where(standings_df["SB"].str.strip().isin(sb_winner),sb_mult,0)
standings_df["Total"] = standings_df["wc_pts"] + standings_df["div_pts"] + standings_df["conf_pts"]+standings_df["pro_pts"]+standings_df["sb_pts"]

st.header('Live 2025 Standings')
current_standings = standings_df[["Name", "Total"]].sort_values(by=['Total'], ascending=False).set_index(["Name"])
st.dataframe(current_standings, use_container_width=True)


