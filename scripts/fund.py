from brownie import Fundraiser
from scripts.helper import get_account


def fund():
  fundraiser = Fundraiser[-1]
  account = get_account(id=2)
  entrance_fee = 99 * 10**18
  print(entrance_fee)
  print(f"The current entry fee is {entrance_fee}")
  print("Funding...")
  fundraiser.fund({"from": account, "value": entrance_fee})

def main():
  fund()
