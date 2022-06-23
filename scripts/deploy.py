from scripts.helper import get_account, deploy_mocks
from brownie import Fundraiser, MockV3Aggregator, network


def deploy_fundraiser(account, price_feed_address):
  print(f'Deploying from account {account} with price_feed_address {price_feed_address} ...')
  fundraiser = Fundraiser.deploy(price_feed_address, {"from": account})
  print(f"Contract deployed to {fundraiser.address}")
  return fundraiser

def main():
  if network.show_active() != "ganache-local":
    sys.exit("Only ganache-local network is supported.")
  account = get_account()
  deploy_mocks()
  price_feed_address = MockV3Aggregator[-1].address
  fundraiser = deploy_fundraiser(account, price_feed_address)

