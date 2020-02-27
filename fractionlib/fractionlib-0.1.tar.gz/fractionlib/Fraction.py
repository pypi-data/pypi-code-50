import math

simplificate = False

class Error(Exception):
    pass

class Fraction(object):
    """A library allowing easier arithmetic operations on fractions. """
    global simplificate
    def __init__(self, numerator, denominator):
        """Initialize the Object"""
        if type(numerator) is not int:
            raise Error('Numerator must be an integer. ')
        elif type(denominator) is not int:
            raise Error('Denominator must be an integer. ')
        elif denominator == 0:
            raise Error('Division by Zero error. ')
        else:
            self.numerator = numerator
            self.denominator = denominator
    def __repr__(self):
        """What is this for anyways"""
        if self.denominator != 1:
            return str(self.numerator) + ' / ' + str(self.denominator)
        else:
            return str(self.numerator)
    def __str__(self):
        """What printing a Fraction object returns. """
        if self.denominator != 1:
            return str(self.numerator) + ' / ' + str(self.denominator)
        else:
            return str(self.numerator)
    def __mul__(self, other):
        """Multiplying two fraction objects. """
        if simplificate == False:
            #Returning unsimplified multiplication
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif simplificate == True:
            #Prime factorizing the numerator and denominator, and then sorts them and removes anything within both lists
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            nplist = []
            dplist = []
            if numerator < 0 and denominator < 0:
                numerator = abs(numerator)
                denominator = abs(denominator)
            elif numerator < 0 and denominator > 0:
                nplist.append(-1)
                numerator = abs(numerator)
            elif numerator >= 0 and denominator < 0:
                dplist.append(-1)
                denominator = abs(denominator)
            while numerator % 2 == 0:
                nplist.append(2)
                numerator //= 2
            for i in range(3, int(math.sqrt(numerator)) + 1, 2):
                while numerator % i == 0:
                    nplist.append(i)
                    numerator = numerator // i
            if numerator > 2:
                nplist.append(numerator)


            while denominator % 2 == 0:
                dplist.append(2)
                denominator //= 2
            for i in range(3, int(math.sqrt(denominator)) + 1, 2):
                while denominator % i == 0:
                    dplist.append(i)
                    denominator = denominator // i
            if denominator > 2:
                dplist.append(denominator)

            nplist.sort()
            dplist.sort()

            for i in nplist[:]:
                if i in dplist[:]:
                    nplist.remove(i)
                    dplist.remove(i)

            newnum = 1
            newdenom = 1
            for i in nplist:
                newnum *= i
            for i in dplist:
                newdenom *= i

            return Fraction(newnum, newdenom)
    def __add__(self, other):
        """Adding two fraction objects together. """
        if simplificate == False:
            lcm = self.denominator * other.denominator // (math.gcd(self.denominator, other.denominator))
            numerator1 = self.numerator * (lcm // self.denominator)
            numerator2 = other.numerator * (lcm // other.denominator)
            numerator = int(numerator1 + numerator2)
            denominator = int(lcm)
            return Fraction(numerator, denominator)
        elif simplificate == True:
            lcm = self.denominator * other.denominator // (math.gcd(self.denominator, other.denominator))
            numerator1 = self.numerator * (lcm // self.denominator)
            numerator2 = other.numerator * (lcm // other.denominator)
            numerator = int(numerator1 + numerator2)
            denominator = int(lcm)
            nplist = []
            dplist = []
            if numerator < 0 and denominator < 0:
                numerator = abs(numerator)
                denominator = abs(denominator)
            elif numerator < 0 and denominator > 0:
                nplist.append(-1)
                numerator = abs(numerator)
            elif numerator >= 0 and denominator < 0:
                dplist.append(-1)
                denominator = abs(denominator)
            while numerator % 2 == 0:
                nplist.append(2)
                numerator //= 2
            for i in range(3, int(math.sqrt(numerator)) + 1, 2):
                while numerator % i == 0:
                    nplist.append(i)
                    numerator = numerator // i
            if numerator > 2:
                nplist.append(numerator)


            while denominator % 2 == 0:
                dplist.append(2)
                denominator //= 2
            for i in range(3, int(math.sqrt(denominator)) + 1, 2):
                while denominator % i == 0:
                    dplist.append(i)
                    denominator = denominator // i
            if denominator > 2:
                dplist.append(denominator)

            nplist.sort()
            dplist.sort()

            for i in nplist[:]:
                if i in dplist[:]:
                    nplist.remove(i)
                    dplist.remove(i)

            newnum = 1
            newdenom = 1
            for i in nplist:
                newnum *= i
            for i in dplist:
                newdenom *= i

            return Fraction(newnum, newdenom)
    def __sub__(self, other):
        """Subtracting one fraction object from another. """
        if simplificate == False:
            lcm = self.denominator * other.denominator // (math.gcd(self.denominator, other.denominator))
            numerator1 = self.numerator * (lcm // self.denominator)
            numerator2 = other.numerator * (lcm // other.denominator)
            numerator = int(numerator1 - numerator2)
            denominator = int(lcm)
            return Fraction(numerator, denominator)
        elif simplificate == True:
            lcm = self.denominator * other.denominator // (math.gcd(self.denominator, other.denominator))
            numerator1 = self.numerator * (lcm // self.denominator)
            numerator2 = other.numerator * (lcm // other.denominator)
            numerator = int(numerator1 - numerator2)
            denominator = int(lcm)
            nplist = []
            dplist = []
            if numerator < 0 and denominator < 0:
                numerator = abs(numerator)
                denominator = abs(denominator)
            elif numerator < 0 and denominator > 0:
                nplist.append(-1)
                numerator = abs(numerator)
            elif numerator >= 0 and denominator < 0:
                dplist.append(-1)
                denominator = abs(denominator)
            while numerator % 2 == 0:
                nplist.append(2)
                numerator //= 2
            for i in range(3, int(math.sqrt(numerator)) + 1, 2):
                while numerator % i == 0:
                    nplist.append(i)
                    numerator = numerator // i
            if numerator > 2:
                nplist.append(numerator)

            while denominator % 2 == 0:
                dplist.append(2)
                denominator //= 2
            for i in range(3, int(math.sqrt(denominator)) + 1, 2):
                while denominator % i == 0:
                    dplist.append(i)
                    denominator = denominator // i
            if denominator > 2:
                dplist.append(denominator)

            nplist.sort()
            dplist.sort()

            for i in nplist[:]:
                if i in dplist[:]:
                    nplist.remove(i)
                    dplist.remove(i)

            newnum = 1
            newdenom = 1
            for i in nplist:
                newnum *= i
            for i in dplist:
                newdenom *= i

            return Fraction(newnum, newdenom)
    def __truediv__(self, other):

        """Multiplying two fraction objects. """
        if simplificate == False:
            #Returning unsimplified multiplication
            if other.numerator != 0:
                return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
            else:
                raise Error('Division by Zero error. ')
        elif simplificate == True:
            #Prime factorizing the numerator and denominator, and then sorts them and removes anything within both lists
            if other.numerator != 0:
                numerator = self.numerator * other.denominator
                denominator = self.denominator * other.numerator
            else:
                raise Error('Division by Zero error. ')
            nplist = []
            dplist = []
            if numerator < 0 and denominator < 0:
                numerator = abs(numerator)
                denominator = abs(denominator)
            elif numerator < 0 and denominator > 0:
                nplist.append(-1)
                numerator = abs(numerator)
            elif numerator >= 0 and denominator < 0:
                dplist.append(-1)
                denominator = abs(denominator)
            while numerator % 2 == 0:
                nplist.append(2)
                numerator //= 2
            for i in range(3, int(math.sqrt(numerator)) + 1, 2):
                while numerator % i == 0:
                    nplist.append(i)
                    numerator = numerator // i
            if numerator > 2:
                nplist.append(numerator)


            while denominator % 2 == 0:
                dplist.append(2)
                denominator //= 2
            for i in range(3, int(math.sqrt(denominator)) + 1, 2):
                while denominator % i == 0:
                    dplist.append(i)
                    denominator = denominator // i
            if denominator > 2:
                dplist.append(denominator)

            nplist.sort()
            dplist.sort()

            for i in nplist[:]:
                if i in dplist[:]:
                    nplist.remove(i)
                    dplist.remove(i)

            newnum = 1
            newdenom = 1
            for i in nplist:
                newnum *= i
            for i in dplist:
                newdenom *= i

            return Fraction(newnum, newdenom)
    def __float__(self):
        return self.numerator/self.denominator
    def __eq__(self, other):
        """Checking whether fraction objects are equal to each other. """
        numerator = self.numerator
        denominator = self.denominator
        nplist = []
        dplist = []
        if numerator < 0 and denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
        elif numerator < 0 and denominator > 0:
            nplist.append(-1)
            numerator = abs(numerator)
            denominator = abs(denominator)
        elif numerator >= 0 and denominator < 0:
            nplist.append(-1)
            denominator = abs(denominator)
            numerator = abs(numerator)
        while numerator % 2 == 0:
            nplist.append(2)
            numerator //= 2
        for i in range(3, int(math.sqrt(numerator)) + 1, 2):
            while numerator % i == 0:
                nplist.append(i)
                numerator = numerator // i
        if numerator > 2:
            nplist.append(numerator)

        while denominator % 2 == 0:
            dplist.append(2)
            denominator //= 2
        for i in range(3, int(math.sqrt(denominator)) + 1, 2):
            while denominator % i == 0:
                dplist.append(i)
                denominator = denominator // i
        if denominator > 2:
            dplist.append(denominator)

        nplist.sort()
        dplist.sort()

        for i in nplist[:]:
            if i in dplist[:]:
                nplist.remove(i)
                dplist.remove(i)

        newnum = 1
        newdenom = 1
        for i in nplist:
            newnum *= i
        for i in dplist:
            newdenom *= i
        selfsimp = (newnum, newdenom)
        numerator = other.numerator
        denominator = other.denominator
        nplist = []
        dplist = []
        if numerator < 0 and denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
        elif numerator < 0 and denominator > 0:
            nplist.append(-1)
            numerator = abs(numerator)
            denominator = abs(denominator)
        elif numerator >= 0 and denominator < 0:
            nplist.append(-1)
            denominator = abs(denominator)
            numerator = abs(numerator)
        while numerator % 2 == 0:
            nplist.append(2)
            numerator //= 2
        for i in range(3, int(math.sqrt(numerator)) + 1, 2):
            while numerator % i == 0:
                nplist.append(i)
                numerator = numerator // i
        if numerator > 2:
            nplist.append(numerator)

        while denominator % 2 == 0:
            dplist.append(2)
            denominator //= 2
        for i in range(3, int(math.sqrt(denominator)) + 1, 2):
            while denominator % i == 0:
                dplist.append(i)
                denominator = denominator // i
        if denominator > 2:
            dplist.append(denominator)

        nplist.sort()
        dplist.sort()

        for i in nplist[:]:
            if i in dplist[:]:
                nplist.remove(i)
                dplist.remove(i)

        newnum = 1
        newdenom = 1
        for i in nplist:
            newnum *= i
        for i in dplist:
            newdenom *= i
        othersimp = (newnum, newdenom)

        if selfsimp == othersimp:
            return True
        else:
            return False
    def __ne__(self, other):
        """Checking whether fraction objects are not equal to each other. """
        return not Fraction(self.numerator, self.denominator) == Fraction(other.numerator, other.denominator)
    def __lt__(self, other):
        lcm = self.denominator * other.denominator // (math.gcd(self.denominator, other.denominator))
        numerator1 = self.numerator * (lcm // self.denominator)
        numerator2 = other.numerator * (lcm // other.denominator)
        if lcm > 0:
            return numerator1 < numerator2
        else:
            return numerator1 > numerator2
    def __le__(self, other):
        lcm = self.denominator * other.denominator // (math.gcd(self.denominator, other.denominator))
        numerator1 = self.numerator * (lcm // self.denominator)
        numerator2 = other.numerator * (lcm // other.denominator)
        if lcm > 0:
            return numerator1 <= numerator2
        else:
            return numerator1 >= numerator2
    def __gt__(self, other):
        lcm = self.denominator * other.denominator // (math.gcd(self.denominator, other.denominator))
        numerator1 = self.numerator * (lcm // self.denominator)
        numerator2 = other.numerator * (lcm // other.denominator)
        if lcm > 0:
            return numerator1 > numerator2
        else:
            return numerator1 < numerator2
    def __ge__(self, other):
        lcm = self.denominator * other.denominator // (math.gcd(self.denominator, other.denominator))
        numerator1 = self.numerator * (lcm // self.denominator)
        numerator2 = other.numerator * (lcm // other.denominator)
        if lcm > 0:
            return numerator1 >= numerator2
        else:
            return numerator1 <= numerator2


def simplification(bool):
    """Checking whether simplification is on or off."""
    global simplificate
    if type(bool) == type(True):
        simplificate = bool
    else:
        raise Error('Simplification has boolean argument. ')



if __name__ == '__main__':
    from sys import argv
    x = Fraction(-2, -3)
    y = Fraction(2, 3)
    z = Fraction(5, 7)
    try:
        if argv[1].lower() == 'true':
            simplification(True)
        else:
            simplification(False)
    except:
        simplification(False)
    print()
    print(x + y)
    print(x + y + z)
    print(Fraction(3, 4) *  y)
    print(y * z)
    print(y - z)
    print(x * y - z)
    print(x == y)
    print(x != y)
    print(x > z)
    print(y <= z)
