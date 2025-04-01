import mysql
import mysql.connector

class Connection():
    select : list = []
    update : list = []
    insert : dict = {}
    values : list = []
    uset : list = []
    join : list = []
    on : dict = {}
    where : list = []
    groupby : list = []
    orderby : list = []
    having : list = []

    last = ""

    def __init__(self, host : str, database : str, user : str, passwd : str):
        self.connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=passwd
        )

        self.connection.autocommit = True

        self.cursor = self.connection.cursor()

    def SELECT(self, variable : str):
        self.select.append(variable)

        return self

    def UPDATE(self, variable : str):
        self.update.append(variable)

        return self

    def INSERT(self, column, value):
        self.insert.update({ column : value })

        return self

    def SET(self, expression : str):
        self.uset.append(expression)

        return self

    def FROM(self, table):
        self.table = table

        return self

    def JOIN(self, database : str, name : str):
        self.join.append(f"{database} {name}")

        self.last = f"{database} {name}"

        return self

    def ON(self, condition : str):
        if self.last not in self.on.keys():
            self.on.update({ f"{self.last}" : [condition]})
        else:
            self.on[self.last].append(condition)

        return self

    def WHERE(self, condition):
        self.where.append(condition)

        return self

    def GROUPBY(self, condition):
        self.groupby.append(condition)

        return self

    def ORDERBY(self, condition):
        self.orderby.append(condition)

        return self

    def HAVING(self, condition):
        self.having.append(condition)

        return self

    def EXECUTE(self):
        final_join = ""

        for join in self.join:
            final_join += f"JOIN {join} ON {' AND '.join(self.on[join])}"

        querry = "".join([(f"SELECT {', '.join(self.select)} " if len(self.select) > 0 else ""),
        (f"UPDATE {', '.join(self.update)} " if len(self.update) > 0 else ""),
        (f"INSERT INTO {self.table} ({', '.join(self.insert.keys())}) " if len(self.insert) > 0 else ""),
        (f"VALUES ({', '.join(self.insert.values())}) " if len(self.insert) > 0 else ""),
        (f"SET {', '.join(self.uset)} " if len(self.uset) > 0 else ""),
        (f"{final_join} "),
        (f"FROM {self.table} " if len(self.select) > 0 else ""),
        (f"WHERE {' AND '.join(self.where)} " if len(self.where) > 0 else ""),
        (f"GROUPBY {' AND '.join(self.groupby)} " if len(self.groupby) > 0 else ""),
        (f"ORDERBY {' AND '.join(self.orderby)} " if len(self.orderby) > 0 else ""), 
        (f"HAVING {' AND '.join(self.having)} " if len(self.having) > 0 else "")])

        print(querry)
        self.cursor.execute(querry)

        self.select = []
        self.update = []
        self.insert = {}
        self.values = []
        self.uset = []
        self.join = []
        self.on = {}
        self.where = []
        self.groupby = []
        self.orderby = []
        self.having = []
        self.table = ""

        return self.cursor.fetchall() if len(self.select) > 0 else None