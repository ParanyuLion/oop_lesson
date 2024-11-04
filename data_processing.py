import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


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
        self.table_name = []
        with open(os.path.join(__location__, table_name)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.table_name.append(dict(r))
        self.table = table

    def filter(self, condition):
        filtered_list = []
        for item in self.table_name:
            if condition(item):
                filtered_list.append(item)
        return filtered_list

    def aggregate(self, aggregation_function, aggregation_key):
        temp = []
        for item in self.table_name:
            temp.append(float(item[aggregation_key]))
        return aggregation_function(temp)

    def __str__(self):
        return f"The {self.table_name}: {self.table}"



