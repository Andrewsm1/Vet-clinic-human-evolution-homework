class Turtle:
    def __init__(self, x=0, y=0, s=1):
        """
        x, y — начальные координаты черепашки
        s — шаг (на сколько клеток перемещается за раз)
        """
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        """Движение вверх (увеличиваем y)"""
        self.y += self.s

    def go_down(self):
        """Движение вниз (уменьшаем y)"""
        self.y -= self.s

    def go_left(self):
        """Движение влево (уменьшаем x)"""
        self.x -= self.s

    def go_right(self):
        """Движение вправо (увеличиваем x)"""
        self.x += self.s

    def evolve(self):
        """Увеличить шаг на 1"""
        self.s += 1

    def degrade(self):
        """Уменьшить шаг на 1. Шаг не может быть меньше 1"""
        if self.s <= 1:
            raise ValueError("Шаг не может быть меньше 1.")
        self.s -= 1

    def count_moves(self, x2, y2):
        """
        Подсчёт количества шагов до точки (x2, y2)
        """
        dx = abs(self.x - x2)
        dy = abs(self.y - y2)

        # Сколько нужно шагов по x и y с учётом текущего шага s
        moves_x = dx // self.s + (1 if dx % self.s != 0 else 0)
        moves_y = dy // self.s + (1 if dy % self.s != 0 else 0)

        return moves_x + moves_y