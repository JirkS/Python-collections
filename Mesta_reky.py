rivers = ["Labe", "Vltava", "Sazava"]
cities = ["Praha", "Vrchlabi", "Cesky Krumlov", "Melnik", "Tynec nad Sazavou", "Davle", "Zruc nad Sazavou"]
city_and_rivers = {
    cities[0]: [rivers[1]],
    cities[1]: [rivers[0]],
    cities[2]: [rivers[1]],
    cities[3]: [rivers[0], rivers[1]],
    cities[4]: [rivers[2]],
    cities[5]: [rivers[1], rivers[2]],
    cities[6]: [rivers[2]],
}
river_and_cities = {
    rivers[0]: [cities[1], cities[3]],
    rivers[1]: [cities[0], cities[2], cities[3], cities[5]],
    rivers[2]: [cities[4], cities[5], cities[6]],
}
river_from_place = {
    rivers[0]: "Kvilda-Vimperk",
    rivers[1]: "Spindleruv Mlyn",
    rivers[2]: "Zdar nad Sazavou",
}


def print_rivers():
    return ("Mestem '" + user_insert + "' protekaji reky: "
            +str(city_and_rivers.get(user_insert))[1:len(str(city_and_rivers.get(user_insert))) - 1])

def print_cities():
    return ("Reka '" + user_insert + "', prameni v '" +river_from_place.get(user_insert)+ "' a proteka mesty: "
            +str(river_and_cities.get(user_insert))[1:len(str(river_and_cities.get(user_insert))) - 1])

try:
    user_insert = input("Zadej reku, nebo mesto: ")

    if city_and_rivers.get(user_insert) is not None:
        print(print_rivers())
    elif river_and_cities.get(user_insert) is not None:
        print(print_cities())
    else:
        raise Exception("Zadano hodnota neni podporovana!")

except Exception as e:
    print(e)
