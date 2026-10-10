COINS = (200, 100, 50, 20, 10, 5, 2, 1)
cache = {}


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    return ways_to_make_change_helper(total, 0)


def ways_to_make_change_helper(total: int, coin_index: int) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    key = (total, coin_index)

    if key in cache:
        return cache[key]
    
    if total == 0:
        return 1

    if total < 0 or coin_index >= len(COINS):
        return 0

    coin = COINS[coin_index]

    # Option 1: Skip this coin and move to the next denomination.
    ways = ways_to_make_change_helper(total, coin_index + 1)

    # Option 2: Use this coin and consider it again.
    if coin <= total:
        ways += ways_to_make_change_helper(total - coin, coin_index)

    cache[key] = ways
    return ways
