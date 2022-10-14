from this import s
import pandas as pd
import time


class MineTx:
    def __init__(self, api_key, per_page_txn, api_counter):
        self.api_key = api_key
        self.per_page_txn = per_page_txn
        self.api_counter = api_counter

    def get_df_txn(self, address, tx_type):

        per_page = self.per_page_txn
        page = 0
        list_txn = []
        total_time = 1

        while per_page == self.per_page_txn:
            start_time = time.time()
            if total_time < 1:
                time.sleep(1.001 - total_time)

            if tx_type == "normal":
                txn_dict =  self.get_txn_normal(address, page)
                self.api_counter += 1
            else:  # transaction are considered internal
                txn_dict = self.get_txn_internal(address, page)
                self.api_counter += 1

            if page == 0:
                list_txn = txn_dict
            else:
                list_txn.append(txn_dict)

            per_page = len(txn_dict)
            page += 1
            total_time = time.time() - start_time

        txn_df = pd.DataFrame(list_txn)
        return txn_df

    def save_csv(self, df, csv_path, address, tx_type, network):
        df.to_csv(csv_path + "/" + network + "_" + address + "_tx_" + tx_type)

    def create_csv(self, csv_path, address, tx_type, network):
        try:
            df = self.get_df_txn(address, tx_type)
            # TODO assert path exist and create it
            self.save_csv(df, csv_path, address, tx_type, network)
        except AssertionError as err:
            print(
                "No transaction found for address #{0} {1} /n error: {2}".format(
                    self.api_counter, address, err
                )
            )
