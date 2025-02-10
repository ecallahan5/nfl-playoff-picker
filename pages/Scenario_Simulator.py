import numpy as np
import pandas as pd
import streamlit as st
import pages
from pages import Live_Standings as ls
import lookups
# import Submit_an_Entry

st.set_page_config(layout="wide")


st.title('See you Next Year!')

# # st.title('Scenario Simulator Coming Soon!')
# st.title('Let\'s Play What If!')
# st.caption('Choose different outcomes for the remaining playoff games to see who will win!')

# sim_df = ls.standings_for_sim.copy() 

# df_teams = pd.DataFrame(lookups.team_list)

# # Input Data Model

# nfc1 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "1")]["slug"].values[0]
# nfc2 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "2")]["slug"].values[0]
# nfc3 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "3")]["slug"].values[0]
# nfc4 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "4")]["slug"].values[0]
# nfc5 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "5")]["slug"].values[0]
# nfc6 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "6")]["slug"].values[0]
# nfc7 = df_teams.loc[(df_teams["conf"] == 'NFC') & (df_teams["seed"] == "7")]["slug"].values[0]
# afc1 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "1")]["slug"].values[0]
# afc2 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "2")]["slug"].values[0]
# afc3 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "3")]["slug"].values[0]
# afc4 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "4")]["slug"].values[0]
# afc5 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "5")]["slug"].values[0]
# afc6 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "6")]["slug"].values[0]
# afc7 = df_teams.loc[(df_teams["conf"] == 'AFC') & (df_teams["seed"] == "7")]["slug"].values[0]
# nfcp = "NFC"
# afcp = "AFC"

# st.divider()
# buffer1, img_a, buffer2, buffer3, img_n, buffer4 = st.columns(6)


# with img_a:
#     st.image(lookups.afc_logo)

# with img_n:
#     st.image(lookups.nfc_logo)

# # st.subheader("Divisional Round", divider=True)
# # picks_a1, picks_a2, picks_n1, picks_n2 = st.columns(4)

# # with picks_a1:

# #     afc1_select = st.selectbox(
# #         "AFC Divisional 1",
# #         (str(df_teams.loc[df_teams["slug"] == afc3]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc3]["name"].values[0]), 
# #          str(df_teams.loc[df_teams["slug"] == afc2]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc2]["name"].values[0])),
# #          index= None, placeholder="Who Wins?")

# afc1_select = str(df_teams.loc[df_teams["slug"] == afc2]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc2]["name"].values[0])

# # with picks_a2:

# #     afc2_select = st.selectbox(
# #         "AFC Divisional 2",
# #         (str(df_teams.loc[df_teams["slug"] == afc4]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc4]["name"].values[0]), 
# #          str(df_teams.loc[df_teams["slug"] == afc1]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc1]["name"].values[0])),
# #          index= None, placeholder="Who Wins?")

# afc2_select = str(df_teams.loc[df_teams["slug"] == afc1]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc1]["name"].values[0])

# # with picks_n1:

# #     nfc1_select = st.selectbox(
# #         "NFC Divisional 1",
# #         (str(df_teams.loc[df_teams["slug"] == nfc4]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc4]["name"].values[0]), 
# #          str(df_teams.loc[df_teams["slug"] == nfc2]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc2]["name"].values[0])),
# #          index= None, placeholder="Who Wins?")

# nfc1_select = str(df_teams.loc[df_teams["slug"] == nfc6]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc6]["name"].values[0])

# # with picks_n2:

# #     nfc2_select = st.selectbox(
# #         "NFC Divisional 2",
# #         (str(df_teams.loc[df_teams["slug"] == nfc6]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc6]["name"].values[0]), 
# #          str(df_teams.loc[df_teams["slug"] == nfc1]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc1]["name"].values[0])),
# #          index= None, placeholder="Who Wins?")

# nfc2_select = str(df_teams.loc[df_teams["slug"] == nfc2]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc2]["name"].values[0])

# # st.divider()
# # st.subheader("Conference Championship Round", divider=True)
# # hlmt_a1, pick_a, hlmt_a2, hlmt_n1, pick_n, hlmt_n2 = st.columns(6)

# # with hlmt_a1:
# #     try:
# #         st.image(df_teams.loc[df_teams['name'] == afc1_select[3:]]["helmet"].values[0])
# #     except:
# #         st.caption("Choose AFC Divisional 1")

# # with hlmt_a2:
# #     try:
# #         st.image(df_teams.loc[df_teams['name'] == afc2_select[3:]]["helmet"].values[0])
# #     except:
# #         st.caption("Choose AFC Divisional 2")

# # with hlmt_n1:
# #     try:
# #         st.image(df_teams.loc[df_teams['name'] == nfc1_select[3:]]["helmet"].values[0])
# #     except:
# #         st.caption("Choose NFC Divisional 1")

# # with hlmt_n2:
# #     try:
# #         st.image(df_teams.loc[df_teams['name'] == nfc2_select[3:]]["helmet"].values[0])
# #     except:
# #         st.caption("Choose NFC Divisional 2")

# # with pick_a:

# #     afc_select = st.selectbox(
# #         "AFC Championship",
# #         (afc1_select, afc2_select), index= None, placeholder="Who Wins?")

# afc_select = str(df_teams.loc[df_teams["slug"] == afc1]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == afc1]["name"].values[0])

# # with pick_n:

# #     nfc_select = st.selectbox(
# #         "NFC Championship",
# #         (nfc1_select, nfc2_select), index= None, placeholder="Who Wins?")
    

# nfc_select = str(df_teams.loc[df_teams["slug"] == nfc2]["seed"].values[0])+". "+str(df_teams.loc[df_teams["slug"] == nfc2]["name"].values[0])

# # st.divider()
# # st.subheader("Pro Bowl Games", divider=True)

# # img_aa, buffer5,  pb_pick,  buffer6, img_nn = st.columns(5)

# # with img_aa:
# #     st.image(lookups.afc_logo)


# # with pb_pick:
# #     pb_select = st.selectbox(
# #         "Pro Bowl Winner",
# #         ("AFC", "NFC"), index= None, placeholder="Who Wins?")

# # with img_nn:
# #     st.image(lookups.nfc_logo)

# pb_select = "NFC"
# st.divider()
# st.subheader("Super Bowl LVIII ", divider=True)

# img_afc_champ, buffer7,  sb_pick,  buffer8, img_nfc_champ = st.columns(5)

# with img_afc_champ:
#     try:
#         st.image(df_teams.loc[df_teams['name'] == afc_select[3:]]["helmet"].values[0])
#     except:
#         st.caption("Choose AFC Champion")

# with sb_pick:
#     sb_select = st.selectbox(
#         "Super Bowl Winner",
#         (afc_select, nfc_select), index= None, placeholder="Who Wins?")

# with img_nfc_champ:
#     try:
#         st.image(df_teams.loc[df_teams['name'] == nfc_select[3:]]["helmet"].values[0])
#     except:
#         st.caption("Choose NFC Champion" )

# st.divider()
# st.subheader("Simulated Standings", divider=True)
# st.caption('If the above scenario comes true, here are the standings:')

# div_winners = [afc1_select, afc2_select, nfc1_select, nfc2_select]
# conf_winners = [afc_select, nfc_select]
# pro_winner = [pb_select]
# sb_winner = [sb_select]

# # Points Multipliers for each Round
# wc_mult = 1
# div_mult = 2
# conf_mult = 4
# pro_mult = 1
# sb_mult = 6



# sim_df["div_pts"] = np.where(sim_df["D1"].str.strip().isin(div_winners),div_mult,0) + np.where(sim_df["D2"].str.strip().isin(div_winners),div_mult,0) +\
#                 np.where(sim_df["D3"].str.strip().isin(div_winners),div_mult,0) + np.where(sim_df["D4"].str.strip().isin(div_winners),div_mult,0)
# sim_df["conf_pts"] = np.where(sim_df["AFC"].str.strip().isin(conf_winners),conf_mult,0) + np.where(sim_df["NFC"].str.strip().isin(conf_winners),conf_mult,0) 
# sim_df["pro_pts"] = np.where(sim_df["PB"].str.strip().isin(pro_winner),pro_mult,0)
# sim_df["sb_pts"] = np.where(sim_df["SB"].str.strip().isin(sb_winner),sb_mult,0)
# sim_df["Simulated Total"] = sim_df["wc_pts"] + sim_df["div_pts"] + sim_df["conf_pts"]+sim_df["pro_pts"]+sim_df["sb_pts"]


# sim_standings = sim_df[["Name", "Total", "Simulated Total"]].sort_values(by=['Simulated Total'], ascending=False).set_index(["Name"])
# st.dataframe(sim_standings, use_container_width=True)
