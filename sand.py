import tsp
def main():
    cities=[]
    for i in range(45):
        cities.append([0,1.1**i])

    model=tsp.TSP(cities)
    population_size=1000
    generations=10
    mutation_rate=1
    best_route, best_distance, best_routes, training_time, degeneration_rate=model.genetic_algorithm(population_size, generations, mutation_rate)
    
    sum=(cities[len(cities)-1][1]-cities[0][1])*2
    
    print(sum)
    print(f"Лучший маршрут: {best_route}")
    print(f"Лучшее расстояние: {best_distance}")
    print(f"Время: {training_time}")
    print(f"Дегенерация: {degeneration_rate}")
    print(f"Количество городов: {len(cities)}")
    print(f"Размер популяции: {population_size}")
    print(f"Чиcлo_пoкoлeний: {generations}")
    print(f"Mutant_rate: {mutation_rate}")
if __name__ == "__main__":
    main()
