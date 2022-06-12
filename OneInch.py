import requests


class OneInchApi:
    base_url = 'https://api.1inch.io/v4.0/'
    wallet: str

    def __init__(self, wallet: str):
        self.wallet = wallet

    def liquidity_source(self, chain_id: str):
        url = 'https://api.1inch.io/v4.0/' + chain_id + '/liquidity-sources'
        return requests.get(url)

    def quote(self, from_token: str, to_token: str, amount: str, chain_id: str, protocol_ids: str = ''):
        url = self.base_url + chain_id + "/quote?fromTokenAddress=" + from_token + \
              "&toTokenAddress=" + to_token + \
              "&amount=" + amount
        if protocol_ids != '':
            url += '&protocols=' + protocol_ids
        return requests.get(url)

    def do_swap(self, chain_id, from_token_addr, to_token_addr, amount, slippage, protocol_ids: str) -> any:
        url = self.base_url + chain_id + '/swap?fromTokenAddress=' + from_token_addr + \
              '&toTokenAddress=' + to_token_addr + \
              '&amount=' + amount + '&fromAddress=' + self.wallet + \
              '&slippage=' + slippage + \
              '&disableEstimate=false&burnChi=false&allowPartialFill=false'
        if protocol_ids != '':
            url += '&protocols=' + protocol_ids
        return requests.get(url)

    def check_allowance(self, token, chain_id):
        url = self.base_url + chain_id + '/approve/allowance?tokenAddress=' + token + \
              '&walletAddress=' + self.wallet
        return requests.get(url)

    def approve_tx(self, token, amount, chain_id):
        url = self.base_url + chain_id + '/approve/transaction?tokenAddress=' + token + \
              '&amount=' + amount
        return requests.get(url)
