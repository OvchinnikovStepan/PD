import random

def generate_random_cities(num_cities, max_coord=100):
    """Генерирует случайный набор городов для задачи коммивояжера."""
    cities = []
    for _ in range(num_cities):
        x = random.randint(0, max_coord)
        y = random.randint(0, max_coord)
        cities.append([x, y])
    return cities