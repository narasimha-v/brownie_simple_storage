import os

from brownie import SimpleStorage  # type: ignore

from .get_account import get_account


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(f"Initial value: {stored_value}")
    transaction = simple_storage.store(7, {"from": account})
    transaction.wait(1)
    stored_value = simple_storage.retrieve()
    print(f"Updated value: {stored_value}")


def main():
    deploy_simple_storage()
