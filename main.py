import json
import requests
from web3 import Web3

# User address
USER_ADDRESS = "0x9B974aF13ae64775E7E96fd92d9089b479cB57C5"


# Setup Web3 provider
# docs for web3 provider: https://web3py.readthedocs.io/en/stable/providers.html
# basic rpc methods: https://web3py.readthedocs.io/en/stable/web3.eth.html
w3 = Web3(Web3.HTTPProvider("https://mainnet.base.org"))

# ABI files
with open("ierc20_abi.json", "r") as f:
    erc20_abi = json.load(f)
with open("ierc4626_abi.json", "r") as f:
    erc4626_abi = json.load(f)

# Contract addresses
USDC_ADDRESS = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
METAMORPHO_VAULT_ADDRESS = "0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A"

# Create contract instances
usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=erc20_abi)
vault_contract = w3.eth.contract(address=METAMORPHO_VAULT_ADDRESS, abi=erc4626_abi)

# view contract code and functions at basescan.org
# https://basescan.org/address/0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 <- USDC
# https://basescan.org/address/0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A <- Metamorpho Spark USDC

# docs for web3 contracts: https://web3py.readthedocs.io/en/stable/web3.contract.html
# prices by token symbol: https://prices.augustdigital.io/price/{symbol}
# price API docs: https://prices.augustdigital.io/docs


def main():
    """Log portfolio state every 5 seconds"""


if __name__ == "__main__":
    main()
