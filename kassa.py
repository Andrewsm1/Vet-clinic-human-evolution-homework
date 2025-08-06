class Kassa:
    def __init__(self):
        # Текущее количество денег в кассе
        self.balance = 0

    def top_up(self, amount):
        """Пополнить кассу на amount рублей"""
        if amount < 0:
            raise ValueError("Нельзя пополнить на отрицательную сумму.")
        self.balance += amount

    def count_1000(self):
        """Вернуть количество полных тысяч в кассе"""
        return self.balance // 1000

    def take_away(self, amount):
        """Снять amount рублей из кассы"""
        if amount < 0:
            raise ValueError("Нельзя снять отрицательную сумму.")
        if amount > self.balance:
            raise ValueError("Недостаточно денег в кассе.")
        self.balance -= amount