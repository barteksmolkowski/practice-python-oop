import logging

logger = logging.getLogger("logger")


class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0) -> None:
        self.owner = owner
        self.__balance = initial_balance if initial_balance >= 0 else 0
        logger.info(f"[__init__] Konto utworzone dla {owner} z saldem {self.__balance}")

    def deposit(self, amount: float) -> None:
        """Wpłata środków, tylko dla kwot dodatnich."""
        if amount > 0:
            self.__balance += amount
            logger.info(f"[deposit] Dodano {amount}. Nowe saldo: {self.__balance}")
        else:
            logger.error(
                f"[deposit] Błąd! Próbowano wpłacić kwotę: {amount}. Wpłata musi być > 0."
            )

    def withdraw(self, amount: float) -> None:
        """Wypłata środków, tylko jeśli kwota jest dodatnia i jest pokrycie na koncie."""
        if amount > self.__balance:
            logger.warning(
                f"[withdraw] Brak środków! Próbowano wypłacić {amount}, dostępne: {self.__balance}"
            )
        elif amount <= 0:
            logger.error(
                f"[withdraw] Błąd! Kwota wypłaty ({amount}) musi być dodatnia."
            )
        else:
            self.__balance -= amount
            logger.info(f"[withdraw] Wypłacono {amount}. Pozostało: {self.__balance}")

    def get_balance(self) -> str:
        """Zwraca sformatowane aktualne saldo."""
        return f"Właściciel: {self.owner} | Aktualne saldo konta: {self.__balance}"


if __name__ == "__main__":
    account = BankAccount("Jan Kowalski", 1000)

    account.deposit(500)
    account.withdraw(200)
    account.deposit(-50)
    account.withdraw(2000)

    print(account.get_balance())
