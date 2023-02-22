import numpy as np
import pandas as pd
import streamlit as st


st.title("See You in 2024!")



# st.header('Let\'s Play What If!')

# afc_select = st.selectbox(
#     "AFC Champ",
#     ('Who Wins?', '3 CIN', '1 KC'))

# if afc_select == '3 CIN':
#     df["Simulated Total a"] = np.where(df["AFC"].str.strip() == '3 CIN', df["Total"] + 4, df["Total"])
# elif afc_select == '1 KC':
#     df["Simulated Total a"] = np.where(df["AFC"].str.strip() == '1 KC', df["Total"] + 4, df["Total"])
# else:
#     df["Simulated Total a"] = df["Total"]

# nfc_select = st.selectbox(
#     "NFC Champ",
#     ('Who Wins?', '2 SF', '1 PHI'))

# if nfc_select == '2 SF':
#     df["Simulated Total n"] = np.where(df["NFC"].str.strip() == '2 SF', df["Simulated Total a"] + 4, df["Simulated Total a"])
# elif nfc_select == '1 PHI':
#     df["Simulated Total n"] = np.where(df["NFC"].str.strip() == '1 PHI', df["Simulated Total a"] + 4, df["Simulated Total a"])
# else:  
#     df["Simulated Total n"] = df["Simulated Total a"]

# pb_select = st.selectbox(
#     "Pro Bowl Winner",
#     ('Who Wins?', 'AFC', 'NFC', 'Tie'))

# if pb_select == 'NFC':
#     df["Simulated Total p"] = np.where(df["PB"].str[:3] == 'NFC', df["Total"] + 1, df["Total"])
# elif pb_select == 'AFC':
#     df["Simulated Total p"] = np.where(df["PB"].str[:3] == 'AFC', df["Total"] + 1,df["Total"])
# elif pb_select == 'Tie':
#     df["Simulated Total p"] = np.where(df["PB"].str[:3] == 'Tie', df["Total"] + 1, df["Total"])
# else:  
#     df["Simulated Total p"] = df["Total"]

# sb_select = st.selectbox(
#     "Super Bowl Champion",
#     ('Who Wins?', "1 PHI", "1 KC"))

# if sb_select == "1 PHI":
#     df["Simulated Total"] = np.where(df["SB"].str.strip() == "1 PHI", df["Simulated Total p"] + 6, df["Simulated Total p"])
# elif sb_select == "1 KC":
#     df["Simulated Total"] = np.where(df["SB"].str.strip() == "1 KC", df["Simulated Total p"] + 6, df["Simulated Total p"])
# else:  
#     df["Simulated Total"] = df["Simulated Total p"]


# if sb_select == '1 PHI':
#     st.image(phi_hel)
# elif sb_select == '1 KC':
#     st.image(kc_hel)
# # elif sb_select == '2 SF':
# #     st.image(sf_hel)
# # if sb_select == '3 CIN':
# #     st.image(cin_hel)


# sim_standings = df[["Name", "Total", "Simulated Total"]].sort_values(by=['Simulated Total'], ascending=False).set_index(["Name"])
# st.dataframe(sim_standings, use_container_width=True)
# # col1, col2, col3, col4 = st.columns(4)

