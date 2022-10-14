import os.path
import pandas as pd

import sys
absolute_path = 'd:\\Perso\\Gitcoin\\Hackathon_open_data'
sys.path.append('d:\\Perso\\Gitcoin\\Hackathon_open_data')
print(sys.path)
from src.main.utils.MinePolygonTx import MinePolygonTx


API_KEY = '3YXDJSVUU8S9UBESZHFEPFCZYCVH72MN77'
tx_chain ='eth_polygon'
current_address_number = 0


miner = MinePolygonTx(API_KEY, 10, 0)

df_contrib = pd.read_csv(absolute_path + '/data/hackathon-contributions-dataset_v2.csv')


df_eth_std = df_contrib[df_contrib['chain'] == tx_chain]
unique_eth_std_address = df_eth_std['address'].unique()

path_to_export = absolute_path + '/data/transactions/' + tx_chain

full_path_to_logs = absolute_path + '/logs/log_' + tx_chain + ".txt"
f = open(full_path_to_logs, "a")

for ads in unique_eth_std_address[current_address_number:10000]:
    f.write('Address'+ ' #' + str(current_address_number) + ' ' + ads + '\n')
    print('Address'+ ' #' + str(current_address_number) + ' ' + ads)
    miner.create_csv(path_to_export, ads, 'normal', tx_chain)
    current_address_number += 1

f.close()
