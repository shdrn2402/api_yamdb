import csv
import sqlite3
import os


from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        path_to_folder = "D://Dev//api_yamdb//api_yamdb//static//data//"
        path_to_db = "D://Dev//api_yamdb//api_yamdb//db.sqlite3"
        folder_content = os.listdir(path_to_folder)
        with open(
            path_to_folder + "category.csv", newline="", encoding='utf-8'
        ) as csvfile:
            reader = csv.reader(csvfile)
            headers = tuple(next(reader, None))
            print(headers)
            for row in reader:
                print(", ".join(row))

        try:
            sqlite_connection = sqlite3.connect(path_to_db)
            cursor = sqlite_connection.cursor()
            print("Успешное подключение к базе данных")

            sqlite_insert_query = f"""INSERT INTO reviews_category
            {headers}
            VALUES
            (2,'Книга','book')"""

            cursor.execute(sqlite_insert_query)
            sqlite_connection.commit()
            print(
                "Данные успешно внесены в таблицу.",
                cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("Не удалось внести данные а таблицу!", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение закрыто.")
