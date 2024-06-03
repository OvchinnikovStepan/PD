import random
import numpy as np
import time

class TSP:
    def __init__(self, cities):
        self.cities = cities
        self.distance_matrix = self.calculate_distance_matrix()

    def calculate_distance_matrix(self):
        """Вычисляет матрицу расстояний между городами."""
        n_cities = len(self.cities)
        distance_matrix = np.zeros((n_cities, n_cities))
        for i in range(n_cities):
            for j in range(i, n_cities):
                distance_matrix[i, j] = distance_matrix[j, i] = self.distance(self.cities[i], self.cities[j])
        return distance_matrix

    def distance(self, city1, city2):
        """Вычисляет расстояние между двумя городами."""
        return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

    def generate_route(self):
        """Генерирует случайный маршрут."""
        return random.sample(range(len(self.cities)), len(self.cities))

    def route_length(self, route):
        """Вычисляет общую длину маршрута."""
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[route[i], route[i + 1]]
        total_distance += self.distance_matrix[route[-1], route[0]]
        return total_distance

    def mutate(self, route, mutation_rate):
        """Мутирует маршрут."""
        if random.random() < mutation_rate:
            i = random.randint(0, len(route) - 1)
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
        return route
    
    def newborn(self, route1,route2):
        child=[None]*len(route1)
        child[0]=route1[0]
        for i in range(1,len(route1)):
            if i%2==1:
                if route2.index(child[i-1])+1<len(route2) and not(route2[route2.index(child[i-1])+1] in child):
                    next_city=route2[route2.index(child[i-1])+1]
                elif route1.index(child[i-1])+1<len(route1) and not(route1[route1.index(child[i-1])+1] in child):
                    next_city=route1[route1.index(child[i-1])+1]
                else:
                    next_city=random.sample([city for city in route1 if city not in child], 1)[0]
            else:
                if route1.index(child[i-1])+1<len(route1) and not(route1[route1.index(child[i-1])+1] in child):
                    next_city=route1[route1.index(child[i-1])+1]
                elif route2.index(child[i-1])+1<len(route2) and not(route2[route2.index(child[i-1])+1] in child):
                    next_city=route2[route2.index(child[i-1])+1]
                else:
                    next_city=random.sample([city for city in route1 if city not in child], 1)[0]
            child[i]=next_city
        return child

    def genetic_algorithm(self, population_size, generations, mutation_rate):
        """Выполняет генетический алгоритм."""
        population = [self.generate_route() for _ in range(population_size)]
        best_route = None
        best_distance = float('inf')

        # Список для хранения лучших маршрутов для анимации
        best_routes = []

        start_time = time.time()  # Запись времени начала обучения
        for generation in range(generations):
            # Оценка маршрутов
            fitness = [1 / self.route_length(route) for route in population]

            # Отбор родительских маршрутов
            parents = random.choices(population, weights=fitness, k=population_size)

            # Скрещивание и мутация
            new_population = []
            for i in range(0, population_size, 2):
                child1 = self.newborn(parents[i], parents[i + 1])
                child2 = self.newborn(parents[i + 1], parents[i])
                child1 = self.mutate(child1, mutation_rate)
                child2 = self.mutate(child2, mutation_rate)
                new_population.extend([child1, child2])

            # Обновление популяции
            population = new_population

            # Нахождение лучшего маршрута
            for route in population:
                distance = self.route_length(route)
                if distance < best_distance:
                    best_route = route
                    best_distance = distance
                    best_routes.append(best_route)  # Добавление в список для анимации

            # Вывод прогресса
            # print(f"Поколение {generation + 1}, Лучшая дистанция: {best_distance}")

        end_time = time.time()  # Запись времени окончания обучения
        training_time = end_time - start_time
        degeneration_rate = best_routes.index(best_route)
        return best_route, best_distance, best_routes, training_time, degeneration_rate