from math import floor


def make_payment(cost: int, cash_inserted: int) -> dict:
    if cost < 0 or cash_inserted < 0:
        raise Exception("Cost or cash is negative but must be positive.")

    result = {
        "change-due": 0,
        10000: 0,
        5000: 0,
        2000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0,
        5: 0,
        1: 0,
    }
    bills_and_coins = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]

    change_due = calculate_change_due(cost, cash_inserted, result)
    calculate_bills_and_coins(result, bills_and_coins, change_due)

    return result


def calculate_bills_and_coins(
    result: dict, bills_and_coins: list, change_due: int
) -> None:
    for bill_or_coin in bills_and_coins:
        if bill_or_coin > change_due:
            continue
        number_of_bills_or_coins = int(change_due / bill_or_coin)
        result[bill_or_coin] += number_of_bills_or_coins
        change_due -= bill_or_coin * number_of_bills_or_coins


def calculate_change_due(cost: int, cash_inserted: int, result: dict) -> int:
    if cash_inserted < cost:
        change_due = cash_inserted
    else:
        change_due = cash_inserted - cost
    result["change-due"] = change_due
    return change_due


if __name__ == "__main__":
    # Cost equals cash inserted, expected no change, bills, or coins.
    print(make_payment(cost=5000, cash_inserted=5000))
    print()

    # Cost greater than cash inserted, not enough cash, return the 5000 bill.
    print(make_payment(cost=10000, cash_inserted=5000))
    print()

    # Cost less than cash inserted, change due 5000, return 1 5000 bill.
    print(make_payment(cost=5000, cash_inserted=10000))
    print()

    # No change due or bills or coins.
    print(make_payment(cost=0, cash_inserted=0))
    print()

    print(make_payment(cost=6574, cash_inserted=1358))
    print()

    print(make_payment(cost=23984, cash_inserted=57399))
    print()

    # Test errors and exceptions.
    # print(make_payment(cost=-3, cash_inserted=500))
    # print(make_payment(cost=3, cash_inserted=-500))
    # print(make_payment(cost=-3, cash_inserted=-500))
    # print(make_payment(cost="asd", cash_inserted=4.0))
