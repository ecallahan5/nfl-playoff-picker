import pandas as pd

afc_logo = "https://content.sportslogos.net/logos/7/1010/full/4cgcwgzbffxlpcbuj94601x5c.gif"
nfc_logo = "https://content.sportslogos.net/logos/7/1012/full/rkqnfgtgwky3sf8viwrmze8me.gif"

pro_bowl_logo = "https://static.www.nfl.com/image/private/t_q-best/league/rxd0qrygbde1lyvyg4hs"
super_bowl_logo = 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d7/Super_Bowl_LVIII_logo.svg/640px-Super_Bowl_LVIII_logo.svg.png'

team_list = [
{"slug": 'BUF', "name": "Buffalo Bills", "conf": "AFC", "seed" : "2", "helmet": "https://content.sportslogos.net/logos/7/149/full/buffalo_bills_logo_helmet_2021_sportslogosnet-4815.png"},
{"slug": 'NE', "name": "New England Patriots", "conf": "AFC", "seed" : "5", "helmet": "https://content.sportslogos.net/logos/7/151/full/ki7ghgfrfy7ufmkza3fetxz64.png"},
{"slug": 'NYJ', "name": "New York Jets", "conf": "AFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/152/full/8989_new_york_jets-helmet-2019.png"},
{"slug": 'MIA', "name": "Miami Dolphins", "conf": "AFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/150/full/5586_miami_dolphins-helmet-2018.png"},

{"slug": 'CIN', "name": "Cincinnati Bengals", "conf": "AFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/154/full/ftn3942al0p6xnzh9lv9v11hl.png"},
{"slug": 'BAL', "name": "Baltimore Ravens", "conf": "AFC", "seed" : "1", "helmet": "https://content.sportslogos.net/logos/7/153/full/317.png"},
{"slug": 'PIT', "name": "Pittsburgh Steelers", "conf": "AFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/156/full/972.png"},
{"slug": 'CLE', "name": "Cleveland Browns", "conf": "AFC", "seed" : "7", "helmet": "https://content.sportslogos.net/logos/7/155/full/8711_cleveland_browns-helmet-2015.png"},

{"slug": 'JAX', "name": "Jacksonville Jaguars", "conf": "AFC", "seed" : "4", "helmet": "https://content.sportslogos.net/logos/7/159/full/3944_jacksonville_jaguars-helmet-2018.png"},
{"slug": 'HOU', "name": "Houston Texans", "conf": "AFC", "seed" : "6", "helmet": "https://content.sportslogos.net/logos/7/157/full/569.png"},
{"slug": 'IND', "name": "Indianapolis Colts", "conf": "AFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/158/full/2ufhm4emsi0ga30iwqjru46mm.png"},
{"slug": 'TEN', "name": "Tennessee Titans", "conf": "AFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/160/full/6034_tennessee_titans-helmet-2018.png"},

{"slug": 'KC', "name": "Kansas City Chiefs", "conf": "AFC", "seed" : "3", "helmet": "https://content.sportslogos.net/logos/7/162/full/mbtef36mxmdxosrpvl4hf3e8i.png"},
{"slug": 'LV', "name": "Las Vegas Raiders", "conf": "AFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/6708/full/4168_las_vegas_raiders-helmet-2020.png"},
{"slug": 'LAC', "name": "Los Angeles Chargers", "conf": "AFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/6446/full/4290_los_angeles__chargers-helmet-2020.png"},
{"slug": 'DEN', "name": "Denver Broncos", "conf": "AFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/161/full/gvbg3heqpbbmfh36ece0v7b67.png"},

{"slug": 'PHI', "name": "Philadelphia Eagles", "conf": "NFC", "seed" : "5", "helmet": "https://content.sportslogos.net/logos/7/167/full/58p6tm0b3zr4dsrhevp12uva4.png"},
{"slug": 'DAL', "name": "Dallas Cowboys", "conf": "NFC", "seed" : "3", "helmet": "https://content.sportslogos.net/logos/7/165/full/o1wgfvp4km9109vj1p4fkq212.png"},
{"slug": 'NYG', "name": "New York Giants", "conf": "NFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/166/full/80fw425vg3404shgkeonlmsgf.png"},
{"slug": 'WAS', "name": "Washington Commanders", "conf": "NFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/6832/full/washington_commanders_logo_helmet_2022_sportslogosnet-9702.png"},

{"slug": 'MIN', "name": "Minnesota Vikings", "conf": "NFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/172/full/4790_minnesota_vikings-helmet-2013.png"},
{"slug": 'GB', "name": "Green Bay Packers", "conf": "NFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/171/full/559.png"},
{"slug": 'CHI', "name": "Chicago Bears", "conf": "NFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/169/full/a8zlwo4e91wi3srhc2f18l5w6.png"},
{"slug": 'DET', "name": "Detroit Lions", "conf": "NFC", "seed" : "2", "helmet": "https://content.sportslogos.net/logos/7/170/full/5885_detroit_lions-helmet-2017.png"},

{"slug": 'TB', "name": "Tampa Bay Buccaneers", "conf": "NFC", "seed" : "4", "helmet": "https://content.sportslogos.net/logos/7/176/full/5717_tampa_bay_buccaneers-helmet-2020.png"},
{"slug": 'NO', "name": "New Orleans Saints", "conf": "NFC", "seed" : "7", "helmet": "https://content.sportslogos.net/logos/7/175/full/910.pngv"},
{"slug": 'CAR', "name": "Carolina Panthers", "conf": "NFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/174/full/8708_carolina_panthers-helmet-2012.png"},
{"slug": 'ATL', "name": "Atlanta Falcons", "conf": "NFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/173/full/3438_atlanta_falcons-helmet-2020.png"},

{"slug": 'SF', "name": "San Francisco 49ers", "conf": "NFC", "seed" : "1", "helmet": "https://content.sportslogos.net/logos/7/179/full/vj3mzax8z0hvgafjtsccwcqde.png"},
{"slug": 'SEA', "name": "Seattle Seahawks", "conf": "NFC", "seed" : "6", "helmet": "https://content.sportslogos.net/logos/7/180/full/3736_seattle_seahawks-helmet-2012.png"},
{"slug": 'ARI', "name": "Arizona Cardinals", "conf": "NFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/177/full/arizona_cardinals_logo_helmet_20059980.png"},
{"slug": 'LAR', "name": "Los Angeles Rams", "conf": "NFC", "seed" : "", "helmet": "https://content.sportslogos.net/logos/7/5941/full/3521_los_angeles_rams-helmet-2020.png"}
]

picks_df = pd.read_csv("picks.csv", index_col = False)
