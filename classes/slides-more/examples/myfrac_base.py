""" Fractions library """

class Fraction:
    """ Class for fractions """
    def __init__(self, nominator, denominator=1):
        if isinstance(nominator, Fraction):
            self.__nominator = nominator.nominator
            self.__denominator = nominator.denominator * denominator
        elif isinstance(nominator, int):
            self.__nominator = nominator
            self.__denominator = denominator
        else:
            raise TypeError(f"can't create fraction from {type(nominator)}")

    @property
    def nominator(self):
        """nominator getter"""
        return self.__nominator

    @property
    def denominator(self):
        """demoninator getter"""
        return self.__denominator

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def __float__(self):
        return self.nominator / self.denominator


def main():
    """Test program"""
    test_frac = Fraction(1, 2)
    print(test_frac)
    print(float(test_frac))

if __name__ == "__main__":
    main()
