from brownie import SimpleStorage, accounts  # type: ignore


def test_deploy():
    account = accounts[0]

    simple_storage = SimpleStorage.deploy({"from": account})
    initial_value = simple_storage.retrieve()
    assert initial_value == 0


def test_update_simple_storage():
    account = accounts[0]

    simple_storage = SimpleStorage.deploy({"from": account})
    transaction = simple_storage.store(7, {"from": account})
    transaction.wait(1)
    assert simple_storage.retrieve() == 7
