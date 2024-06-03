import tsp
import generate_tsp
import numpy as np

def run_genetic_algorithm(cities, population_size, generations, mutation_rate):
    """Запускает генетический алгоритм и возвращает результаты."""
    tsp_problem = tsp.TSP(cities)
    best_route, best_distance, best_routes, training_time,degeneration_rate = tsp_problem.genetic_algorithm(
        population_size, generations, mutation_rate
    )
    return best_route, best_distance, best_routes, training_time,degeneration_rate

def main():
    # Параметры генетического алгоритма
    population_size_list = [10,20,50,100,200]
    generations_list = [5,10,30,50,100,200]
    mutation_rate_list = [0,0.1,0.3,0.5,0.7,1]

    # Генерация наборов данных
    num_cities_list = [[5]*20,[10]*20,[20]*10,[50]*10,[100]*5,[150]*5,[300]*3,[500]]
    results = []
    for population_size in population_size_list:
        for generation in generations_list:
            for mutation_rate in mutation_rate_list:
                for num_cities in num_cities_list:
                    temp_results=[]
                    deg_results=[]
                    for case in num_cities:
                        cities = generate_tsp.generate_random_cities(case)
                        best_route, best_distance, best_routes, training_time, degeneration_rate = run_genetic_algorithm(
                        cities, population_size, generation, mutation_rate
                        )
                        # result[num_cities] = {
                        # "best_route": best_route,
                        # "best_distance": best_distance,
                        # "training_time": training_time,
                        # "best_routes": best_routes
                        # }
                        temp_results.append(training_time)
                        deg_results.append(degeneration_rate)
                    print(f"Количество городов: {case}")
                    print(f"Размер популяции: {population_size}")
                    print(f"Чиcлo_пoкoлeний: {generation}")
                    print(f"Mutant_rate: {mutation_rate}")
                    print(f"Среднее время обучения: {np.mean(temp_results)} секунд")
                    print(f"Средняя поколение вырождения: {np.mean(deg_results)} поколение")

    # Вывод результатов
    # print("Результаты генетического алгоритма:")
    # for num_cities, result in results.items():
    #     print(f"Количество городов: {num_cities}")
    #     print(f"Лучший маршрут: {result['best_route']}")
    #     print(f"Лучшая дистанция: {result['best_distance']}")
    #     print(f"Время обучения: {result['training_time']:.2f} секунд")
    #     print()

if __name__ == "__main__":
    main()