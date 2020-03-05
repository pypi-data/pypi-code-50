class Offer:
    @property
    def id(self):
        """
        The character id this offer refers to.

        :getter: Returns this Offer's id
        :setter: Sets this Offer's id
        :type: int (conversion is applied)
        """
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = int(id)

    @property
    def level_price_dict(self):
        """
        The dictionary of level-to-price relationships for \
        this offer.

        :getter: Returns this Offer's level-price-dict
        :setter: Sets this Offer's level-price-dict
        :type: dict (sets to None if not type conformant)
        """
        return self.__level_price_dict

    @level_price_dict.setter
    def level_price_dict(self, lpd):
        self.__level_price_dict = lpd if isinstance(lpd, dict) else None
        if self.level_price_dict is not None and not self._is_level_price_dict_sorted():
            self._sort_level_price_dict()

    def __init__(self, id=0, level_price_dict=None):
        self.id = id
        self.level_price_dict = level_price_dict

    def _sort_level_price_dict(self):
        """Sorts dict with lowest price first"""
        if self.level_price_dict is not None:
            self.level_price_dict = {k: v for k, v in sorted(self.level_price_dict.items(),
                                                             key=lambda item: item[1])}

    def _is_level_price_dict_sorted(self):
        """Checks if dict is already sorted"""
        values = list(self.level_price_dict.values())
        return all(values[i] <= values[i + 1] for i in range(len(values) - 1))

    def get_min_price(self):
        """Return lowest price in dict"""
        return self.level_price_dict[self.get_min_level()]

    def get_min_level(self):
        """Return level for lowest price in dict"""
        return next(iter(self.level_price_dict))

    def get_rel_price(self, target_level):
        """Return price of target level, or min price if not available"""
        return self.level_price_dict.get(int(target_level), self.get_min_price())

    def get_rel_level(self, target_level):
        """Return target level, or min level if not available"""
        return target_level if int(target_level) in self.level_price_dict \
            else self.get_min_level()