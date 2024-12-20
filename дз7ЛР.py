class Polynomial:
    def __init__(self, coefficients):
        self._coefficients = coefficients

    @property
    def degree(self):
        return len(self._coefficients) - 1

    def __repr__(self):
        t1 = []
        for i, cf in enumerate(reversed(self._coefficients)):
            if cf == 0:
                continue
            cas = self.degree - i
            if cas == 0:
                t1.append(f"{cf}")
            elif cas == 1:
                t1.append(f"{cf}x")
            else:
                t1.append(f"{cf}x^{cas}")
        return " + ".join(t1) if t1 else "0"

    def __call__(self, x):
        return self.evaluate(x)

    def __add__(self, other):
        ml = max(self.degree, other.degree) + 1
        ncf = [0] * ml
        for i in range(len(self._coefficients)):
            ncf[i] += self._coefficients[i]
        for i in range(len(other._coefficients)):
            ncf[i] += other._coefficients[i]
        return Polynomial(ncf)

    def __sub__(self, other):
        ml = max(self.degree, other.degree) + 1
        ncf = [0] * ml
        for i in range(len(self._coefficients)):
            ncf[i] += self._coefficients[i]
        for i in range(len(other._coefficients)):
            ncf[i] -= other._coefficients[i]
        return Polynomial(ncf)

    def __mul__(self, other):
        ncf = [0] * (self.degree + other.degree + 1)
        for i in range(len(self._coefficients)):
            for j in range(len(other._coefficients)):
                ncf[i + j] += self._coefficients[i] * other._coefficients[j]
        return Polynomial(ncf)

    def derivative(self):
        if self.degree == 0:
            return Polynomial([0])
        dcf = [self._coefficients[i] * i for i in range(1, len(self._coefficients))]
        return Polynomial(dcf)

    def evaluate(self, x):
        result = 0
        for i, cf in enumerate(self._coefficients):
            result += cf * (x ** i)
        return result


class QuadraticPolynomial(Polynomial):
    def __init__(self, coefficients):
        super().__init__(coefficients)

    def discriminant(self):
        a, b, c = self._coefficients
        return b ** 2 - 4 * a * c

    def find_roots(self):
        c, b, a = self._coefficients
        disc = self.discriminant()
        root1 = (-b + disc ** 0.5) / (2 * a)
        root2 = (-b - disc ** 0.5) / (2 * a)
        return root1, root2


# Пример использования

# Создаем два полинома
p1 = Polynomial([1, 2, 3])  # 3x^2 + 2x + 1
p2 = Polynomial([0, -1, 1])  # x^2 - x

# Вывод полиномов
print("P1:", p1)  # 3x^2 + 2x + 1
print("P2:", p2)  # x^2 - x

# Операции
print("P1 + P2:", p1 + p2)  # Результат сложения
print("P1 - P2:", p1 - p2)  # Результат вычитания
print("P1 * P2:", p1 * p2)  # Результат умножения

# Вычисление значения в точке x = 2
print("P1(2):", p1(2))  # Значение P1 при x = 2

# Производная
print("P1 derivative:", p1.derivative())  # Производная P1

# Примеры входа и выходов
# P1: 3x^2 + 2x + 1
# P2: x^2 - x
# P1 + P2: 4x^2 + x + 1
# P1 - P2: 2x^2 + 3x + 1
# P1 * P2: 3x^4 - x^3 - x^2 - 1
# P1(2): 17
# P1 derivative: 6x + 2

test = QuadraticPolynomial([1, -3, 2])
print('Discriminant:', test.discriminant())
print('Roots:', test.find_roots())
