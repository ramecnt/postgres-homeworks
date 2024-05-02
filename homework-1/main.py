import psycopg2  # Импорт библиотеки для работы с PostgreSQL
import csv  # Импорт библиотеки для работы с CSV файлами


def import_data_to_database():
    """
    Импортирует данные из CSV файлов в таблицы базы данных PostgreSQL.

    Предполагается, что существуют следующие таблицы:
    - customers (customer_id, company_name, contact_name)
    - employee (employee_id, first_name, last_name, title, birth_date, notes)
    - orders (order_id, customer_id, employee_id, order_date, ship_city)

    CSV файлы ожидаются в директории 'north_data'.

    Возвращает:
        None
    """
    conn = psycopg2.connect(
        host="localhost",  # Хост базы данных
        database="postgres",  # Имя базы данных
    )
    try:
        with conn:
            with conn.cursor() as cur:
                with open('north_data/customers_data.csv') as file:
                    reader = csv.DictReader(file)  # Создание читателя CSV файла
                    for row in reader:
                        # Вставка данных из CSV файла в таблицу customers
                        cur.execute(
                            "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                            (row['customer_id'], row['company_name'], row['contact_name']))
                with open('north_data/employees_data.csv') as file:
                    reader = csv.DictReader(file)  # Создание читателя CSV файла
                    for row in reader:
                        # Вставка данных из CSV файла в таблицу employee
                        cur.execute(
                            "INSERT INTO employee (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s"
                            ", %s, %s, %s, %s, %s)",
                            (row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date'],
                             row['notes']))
                with open('north_data/orders_data.csv') as file:
                    reader = csv.DictReader(file)  # Создание читателя CSV файла
                    for row in reader:
                        # Вставка данных из CSV файла в таблицу orders
                        cur.execute(
                            "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s"
                            ", %s, %s, %s, %s)",
                            (row['order_id'], row['customer_id'], row['employee_id'], row['order_date'],
                             row['ship_city']))

    finally:
        conn.close()


# Вызов функции для импорта данных в базу данных
import_data_to_database()