import csv, os


class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        self.table_database.append(table)

    def search(self, table_name):
        for table in self.table_database:
            if table == table_name:
                return table
        return None


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = []
        with open(os.path.join(__location__, table)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.table.append(dict(r))

    def filter(self, condition):
        filtered_list = []
        for item in self.table:
            if condition(item):
                filtered_list.append(item)
        return filtered_list

    def aggregate(self, aggregation_function, aggregation_key, filtered_data=None):
        temp = []
        if filtered_data is None:
            filtered_data = self.table
        for item in filtered_data:
            temp.append(float(item[aggregation_key]))
        return aggregation_function(temp)

    def __str__(self):
        return f"{self.table_name}: {self.table}"


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


table_db = TableDB()
cities_table = Table("Cities", "Cities.csv")
countries_table = Table("Countries", "Countries.csv")
print(cities_table)
print(countries_table)
table_db.insert(cities_table)
table_db.insert(countries_table)

country_in_EU = countries_table.filter(lambda x: (x['EU'] == 'yes' and x['coastline'] == 'no'))
# print(country_in_EU)
list_country_in_EU = []
for i in range(len(country_in_EU)):
    list_country_in_EU.append(country_in_EU[i]['country'])
# print(list_country_in_EU)
city_in_EU = cities_table.filter(lambda x: x['country'] in list_country_in_EU)
# print(type(city_in_EU))
# print(city_in_EU)

# Print the min temperatures for cities in EU that do not have coastlines
min_temp = (cities_table.aggregate(lambda x: min(x), 'temperature', city_in_EU))
print("min temperatures for cities in EU that do not have coastlines :")
print(min_temp)
print()
# Print the max temperatures for cities in EU that do not have coastlines
min_temp = (cities_table.aggregate(lambda x: max(x), 'temperature', city_in_EU))
print("max temperatures for cities in EU that do not have coastlines :")
print(min_temp)
print()

# Print the min latitude for cities in every country
min_temp = cities_table.aggregate(lambda x: min(x), 'latitude')
print("min latitude for cities in every country:")
print(min_temp)
print()
# Print the max latitude for cities in every country
max_temp = cities_table.aggregate(lambda x: max(x), 'latitude')
print("max latitude for cities in every country:")
print(max_temp)
print()
