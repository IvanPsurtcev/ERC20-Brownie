from brownie import accounts, config, Token
from scripts.helpful_scripts import get_account


initial_supply = 1000000000000000000000  # 1000
token_name = "Token"
token_symbol = "TKN"


def main():
    account = get_account()
    token = Token.deploy(initial_supply, token_name, token_symbol, {"from": account})
