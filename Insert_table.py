
import sqlite3


conn = sqlite3.connect("storage/myInfo2.db")  # 資料庫連線
print('請輸入myInfo資料庫student2表單資料')


class dbDate:

    def __init__(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = gender

    def get_student2():

        while True:
            new_name = input('請輸入您的名字:')
            new_gender = input('請輸入您的性別:')
            comb = (new_name, new_gender)

            return comb


def main():
    while True:
        tables = dbDate.get_student2()
        sql = '''insert into students2(name,gender) values(?,?)'''

        conn.execute(sql, tables)
        conn.commit()
        again = input('繼續(y/n)?')
        if again.lower() == 'n':
            break


if __name__ == "__main__":
    main()

conn.close()
