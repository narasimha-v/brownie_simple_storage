import os

from brownie import SimpleStorage  # type: ignore


def read_contract():
    simple_storage = SimpleStorage[-1]
    print(f"Stored value: {simple_storage.retrieve()}")


def main():
    read_contract()
