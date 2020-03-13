import random
from datetime import date, timedelta


class RandomPESEL(object):
    __MIN_AGE = 0
    __MAX_AGE = 99
    __CHECKSUM_WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    def generate(self, gender=None, min_age=__MIN_AGE, max_age=__MAX_AGE):
        """Generate random PESEL number
        :param gender: Gender
        :type gender: str
        :param min_age: Min age
        :type min_age: int
        :param max_age: Max age
        :type max_age: int
        :return: Valid PESEL number
        :rtype: str
        :raises ValueError: if gender is different then 'm' or 'f'
        :raises ValueError: if min_age is less then 0 or greater then max_age
        """
        gender = gender.upper() if gender is not None else random.choice(['M', 'F'])
        if gender not in ['M', 'F']:
            raise ValueError('gender should contain one of two values: M - male, F - female')
        if min_age < 0 or min_age > max_age:
            raise ValueError('min_age must be greater then or equal to 0 and less then or equal to max_age')

        age = random.randint(min_age, max_age)
        birth_date = self.__get_random_birth_date(age)
        month = birth_date.month
        if 1800 <= birth_date.year <= 1899:
            month += 80
        elif 2000 <= birth_date.year <= 2099:
            month += 20
        elif 2100 <= birth_date.year <= 2199:
            month += 40
        elif 2200 <= birth_date.year <= 2299:
            month += 60

        pesel = birth_date.strftime('%y{:02d}%d').format(month)
        pesel += str(random.randint(0, 999)).zfill(3)
        pesel += str(random.choice([1, 3, 5, 7, 9])) if gender == 'M' else str(random.choice([0, 2, 4, 6, 8]))
        pesel += str(self.__get_checksum(pesel))
        return pesel

    @classmethod
    def __get_checksum(cls, pesel):
        """Generate checksum for PESEL
        :param pesel: PESEL number
        :type pesel: str
        :return: Checksum for PESEL
        :rtype: int
        """
        checksum = 0
        for index, value in enumerate(pesel):
            checksum += cls.__CHECKSUM_WEIGHTS[index] * int(value)
        checksum = (10 - (checksum % 10)) % 10;
        return checksum

    @staticmethod
    def __get_random_birth_date(age):
        """Generate birth date for specified age
        :param age: Age for PESEL
        :type age: int
        :return: Birth date
        :rtype: date
        """
        current_date = date.today()
        try:
            return current_date.replace(year=current_date.year - age - 1) + timedelta(days=random.randint(1, 364))
        except ValueError:
            return current_date + (date(current_date.year - age - 1, 1, 1) - date(current_date.year, 1, 1)) + timedelta(
                days=random.randint(1, 364))
