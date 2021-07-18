import sqlite3


conn = sqlite3.connect('storage/myInfo2.db')


class creaDB:

    def __init__(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = gender

    def get_createTable():
        sql = '''Create table students2(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            gender TEXT)'''

        return sql


def main():
    new_table = creaDB.get_createTable()
    conn.execute(new_table)


if __name__ == "__main__":
    main()

conn.close()
