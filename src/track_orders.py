from collections import Counter


class TrackOrders:
    def __init__(self):
        self._orders = list()

    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        return self._orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        orders = Counter(
            order for name, order, _ in self._orders if name == customer
        )
        return orders.most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        all_orders = set(order for _, order, _ in self._orders)
        client_orders = set(
            order for name, order, _ in self._orders if name == customer
        )
        return all_orders - client_orders

    def get_days_never_visited_per_customer(self, customer):
        all_days = set(day for _, _, day in self._orders)
        client_attend = set(
            day for name, _, day in self._orders if name == customer
        )
        return all_days - client_attend

    def get_busiest_day(self):
        days = Counter(day for _, _, day in self._orders)
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = Counter(day for _, _, day in self._orders)
        return min(days, key=days.get)
