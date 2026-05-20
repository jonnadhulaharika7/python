def bank_account(name, balance=0, **kwargs):
    print(f"account holder: {name}")
    print(f"balance: {balance}")
    print("/n other details:")
    for keys, values in kwargs.items():
     print(f"{keys} : {values}")
bank_account(
    "Haru",
    5000,
    age = 16,
    accounttype = "savings"
)
            