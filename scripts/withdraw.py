from brownie import Fundraiser
from scripts.helper import get_account


def withdraw():
  fundraiser = Fundraiser[-1]
  account = get_account() #owner
  print("Withdrawing...")
  fundraiser.withdraw({"from": account})

def main():
  withdraw()
