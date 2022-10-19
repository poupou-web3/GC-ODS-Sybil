import pandas as pd

import sys
absolute_path = 'd:\\Perso\\Gitcoin\\Hackathon_open_data'
sys.path.append('d:\\Perso\\Gitcoin\\Hackathon_open_data')
print(sys.path)
from src.main.utils.MinePolygonTx import MinePolygonTx



PER_PAGE = 100
API_KEY = 'DJ7M8MNPMSI46VQKRRCYPCCIT2VJKVG68K'
TX_CHAIN ='eth_polygon'
from_address_number = 0
to_address_number = 200000


miner = MinePolygonTx(API_KEY, PER_PAGE, 0)

df_contrib = pd.read_csv(absolute_path + '/data/hackathon-contributions-dataset_v2.csv')


df_eth_std = df_contrib[df_contrib['chain'] == TX_CHAIN]
unique_eth_std_address = df_eth_std['address'].unique()
print("Unique polygon adresses : " + str(len(unique_eth_std_address)))

path_to_export = absolute_path + '/data/transactions/' + TX_CHAIN

full_path_to_logs = absolute_path + '/logs/log_' + TX_CHAIN + ".txt"
f = open(full_path_to_logs, "a")

for ads in unique_eth_std_address[from_address_number:to_address_number]:
    f.write('Address'+ ' #' + str(from_address_number) + ' ' + ads + 'api call #' + str(miner.api_counter) + '\n')
    print('Address'+ ' #' + str(from_address_number) + ' ' + ads+ 'api call #' + str(miner.api_counter))
    miner.create_csv(path_to_export, ads, 'normal', TX_CHAIN)
    from_address_number += 1

f.close()
print("End mining polygon transactions")