

def get_cities_and_iata() -> dict:
    cities = {}
    with open("Data/iata_and_cities.txt", "r", encoding='utf-8') as file:
        for line in file:
            # Split the line based on the delimiter
            parts = line.strip().split(' — ')
            iata_code = parts[0]
            city = parts[-1]
            cities[city.split(", ")[-1]] = iata_code

    return cities