import numpy as np
import pandas as pd
import streamlit as st
import lookups


wc_winners = ["BUF", "CIN", "JAX", "SF", "DAL", "NYG"]
div_winners = ["PHI", "SF", "KC", "CIN"]
conf_winners = ["PHI", "KC"]
pro_winner = ["NFC"]
sb_winner = ["KC"]

standings_df = lookups.picks_df

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

st.header('Final 2023 Standings')
current_standings = standings_df[["Name", "Total"]].sort_values(by=['Total'], ascending=False).set_index(["Name"])
st.dataframe(current_standings, use_container_width=True)


