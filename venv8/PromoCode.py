from uuid import uuid4

import Reward as r

class PromoCode(r.Reward):

    def __init__(self,  name, value, promoCode, quantity, expiryDate, category):
        r.Reward.__init__(self, name, value, expiryDate, category)
        uuid = str(uuid4())[:8]
        self.__promo_id = uuid
        self.__promoCode = promoCode
        self.__quantity = quantity

    def set_promo_id(self, promo_id):
        self.__promo_id = promo_id

    def set_promoCode(self, promoCode):
        self.__promoCode = promoCode

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_promoCode(self):
        return self.__promoCode

    def get_promo_id(self):
        return self.__promo_id

    def get_quantity(self):
        return self.__quantity

    def __str__(self):
        p = super().__str__()
        s = p + "Promo Code: {}  Quantity:{}".format(self.__promoCode, self.__quantity)
        return s

