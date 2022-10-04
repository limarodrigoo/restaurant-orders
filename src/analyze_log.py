import csv
from collections import Counter


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, encoding="utf-8") as csvfile:
            restaurant_log = list(
                csv.reader(csvfile, delimiter=",", quotechar="\n")
            )

            result = [
                most_ordered_by_client(restaurant_log, "maria"),
                order_by_client_meal(restaurant_log, "hamburguer", "arnaldo"),
                orders_never_requested(restaurant_log, "joao"),
                off_days_by_client(restaurant_log, 'joao')
            ]

            with open("data/mkt_campaign.txt", "w") as file:
                for result_line in result:
                    file.write(f"{result_line}\n")

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def most_ordered_by_client(list, client):
    orders = Counter(order for name, order, _ in list if name == client)
    return orders.most_common(1)[0][0]


def order_by_client_meal(list, order, client):
    orders = Counter(order for name, order, _ in list if name == client)
    return orders[order]


def orders_never_requested(list, client):
    all_orders = set(order for _, order, _ in list)
    client_orders = set(order for name, order, _ in list if name == client)
    return all_orders - client_orders


def off_days_by_client(list, client):
    all_days = set(day for _, _, day in list)
    client_attend = set(day for name, _, day in list if name == client)
    return all_days - client_attend
