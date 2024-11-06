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


