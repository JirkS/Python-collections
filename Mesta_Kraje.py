regions = ["Stredocesky", "Jihomoravsky", "Pardubicky"]
cities = ["Kladno", "Brno", "Prelouc", "Kurim", "Praha"]
pairs = {
    0: 0,
    1: 1,
    2: 2,
    3: 1,
    4: 0,
}


def check_cities():
    for key in pairs.keys():
        if cities[key] == user_insert:
            return key


def check_regions(user_pair_t):
    for value in pairs.values():
        if regions[value] == user_insert:
            return value
    if user_pair_t is None:
        raise Exception("Zadano hodnota neni podporovana!")


def print_city(user_pair_t):
    current_city_index, current_region_index = list(pairs.items())[user_pair_t]
    return ("Mesto " + cities[current_city_index] + " lezi uvnitr "
            + regions[current_region_index][0:len(regions[current_region_index]) - 1] + "eho kraje.")


def summarize_cities(current_city_indexes_t):
    for key, value in pairs.items():
        if value == user_pair:
            current_city_indexes_t.append(key)


def print_region(current_city_indexes_t, user_pair_t):
    end_result = "Uvnitr " + regions[user_pair_t][0:len(regions[user_pair_t]) - 1] + "eho kraje lezi mesta: "
    for i in current_city_indexes_t:
        end_result += cities[i] + ", "
    return end_result[0:len(end_result) - 2]


try:
    user_insert = input("Zadej mesto, nebo kraj: ")
    user_pair = check_cities()
    if user_pair is None:
        user_pair = check_regions(user_pair)
        current_city_indexes = []
        summarize_cities(current_city_indexes)
        print(print_region(current_city_indexes, user_pair))
    else:
        print(print_city(user_pair))


except Exception as e:
    print(e)
