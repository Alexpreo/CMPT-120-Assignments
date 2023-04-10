f = open('cities.txt', 'r', encoding='utf-8')

cities = {}
for line in f:
    name, population = line.strip().split('\t')
    cities[name] = int(population)

city_names = list(cities.keys())
for i in range(len(city_names)):
    for j in range(len(city_names) - 1 - i):
        if cities[city_names[j]] > cities[city_names[j+1]]:
            city_names[j], city_names[j+1] = city_names[j+1], city_names[j]

while True:
    city = input()
    if city == 'quit':
        break
    if city in cities:
        rank = city_names.index(city) + 1
        print(rank)
