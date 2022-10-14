

from main.utils.MineTx import MineTx


class MineEthTx(MineTx):

    def __init__(self, api_key, per_page_txn, api_counter):
        super().__init__(self, per_page_txn, api_counter)
        self.eth = Etherscan(api_key)

    