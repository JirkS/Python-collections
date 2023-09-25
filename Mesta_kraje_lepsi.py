regions = ["Stredocesky", "Jihomoravsky", "Pardubicky"]
cities = ["Kladno", "Brno", "Prelouc", "Kurim", "Praha"]
city_and_regions = {
    cities[0]: regions[0],
    cities[1]: regions[1],
    cities[2]: regions[2],
    cities[3]: regions[1],
    cities[4]: regions[0],
}
region_and_cities = {
    regions[0]: [cities[0], cities[4]],
    regions[1]: [cities[1], cities[3]],
    regions[2]: [cities[2]],
}

'''
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
'''


def print_region():
    return ("Mesto '" + user_insert + "' lezi uvnitr "
            + str(city_and_regions.get(user_insert))[0:len(str(city_and_regions.get(user_insert))) - 1] + "eho kraje")


def print_city():
    return ("Uvnitr " + user_insert[0:len(user_insert) - 1] + "eho kraje lezi mesta: "
            + str(region_and_cities.get(user_insert))[1:len(str(region_and_cities.get(user_insert))) - 1])


try:
    user_insert = input("Zadej mesto, nebo kraj: ")

    if city_and_regions.get(user_insert) is not None:
        print(print_region())
    elif region_and_cities.get(user_insert) is not None:
        print(print_city())
    else:
        raise Exception("Zadano hodnota neni podporovana!")

except Exception as e:
    print(e)
