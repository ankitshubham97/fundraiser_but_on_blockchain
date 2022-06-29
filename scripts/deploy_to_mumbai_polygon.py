from scripts.helper import get_account, deploy_mocks
from brownie import Fundraiser, network, config


def deploy_fundraiser(account, price_feed_address):
  print(f'Deploying from account {account} with price_feed_address {price_feed_address} ...')
  fundraiser = Fundraiser.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"),)
  print(f"Contract deployed to {fundraiser.address}")
  return fundraiser

def main():
  if network.show_active() != "polygon-test":
    sys.exit("Only polygon-test network is supported.")
  account = get_account()
  price_feed_address = config["networks"][network.show_active()]["matic_usd_price_feed"]
  fundraiser = deploy_fundraiser(account, price_feed_address)

