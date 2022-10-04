class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self._orders = list()
        self._buy_list = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }
        self._out_of_stock = set()

    def add_new_order(self, customer, order, day):
        self._orders.append((customer, order, day))
        ingredient_out_of_stock = set(self.INGREDIENTS).intersection(self._out_of_stock)
        if len(ingredient_out_of_stock) == 0:
            for ingridient in self.INGREDIENTS[order]:
                self._buy_list[ingridient] += 1
                current_stock = self.MINIMUM_INVENTORY[ingridient] - self._buy_list[ingridient]
                if current_stock <= 0:
                    self._out_of_stock.add(ingridient)
            return False


    def get_quantities_to_buy(self):
        return self._buy_list
