from brownie import Token, accounts

def test_deploy():
    owner = accounts[0]
    # не знаю как у нас происходит определение, кто owner контракта в brownie, 
    # поэтому по аналогии с hardhat пусть будет 1й кто получает подпись
    token = Token.deploy(1000)
    # не знаю как вызвать метод address у owner поэтому пока что закидываю в balanceOf объект, аналогично для других тестов 
    balance_owner = token.balanceOf(owner)
    expected = 1000

    assert balance_owner == expected

def test_transfer():
    owner = accounts[0]
    user = accounts[1]
    token = Token.deploy(1000)
    # не знаю как у нас происходит определение, кто owner контракта в brownie, 
    # поэтому по аналогии с hardhat пусть будет 1й аккаунт, кто получает подпись
    balance_owner_before = token.balanceOf(owner) 
    expected_owner_before = 1000
    assert balance_owner_before == expected_owner_before

    balance_user_before = token.balanceOf(user) 
    expected_user_before = 0
    assert balance_user_before == expected_user_before

    token.transfer(user, 400)

    balance_owner_after = token.balanceOf(owner) 
    expected_owner_after = 600
    assert balance_owner_after == expected_owner_after

    balance_user_after = token.balanceOf(user) 
    expected_user_after = 400
    assert balance_user_after == expected_user_after

def test_burn():
    owner = accounts[0]
    token = Token.deploy(1000)
    balance_owner_before = token.balanceOf(owner) 
    expected_owner_before = 1000
    assert balance_owner_before == expected_owner_before
    # как коннектиться к функциям в hardhat просто connect(owner) и тд?
    token.burn(400)

    balance_owner_after = token.balanceOf(owner) 
    expected_owner_after = 600
    assert balance_owner_after == expected_owner_after




