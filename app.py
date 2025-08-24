
import psycopg
# print(psycopg.__version__)
# exit()


# Подключение к базе данных
conn = psycopg.connect(dbname="Export",
                        host="localhost",
                        user="postgres",
                        password="***",                                                                                                                        
                        port="5432")
cur = conn.cursor()

# Инициализация ID и структур данных
market_id = 0
city_id = 0
product_id = 0
markets = {}
cities = {}
products = {}

# Блок для обработки исключений
try:

    # Запрос данных из таблицы export
    table_export = """
    SELECT fmid, marketname, website, facebook, twitter, youtube, othermedia, street, city, county, state, zip, review
    FROM public.export
    """
    cur.execute(table_export)

    # Обработка данных из базы
    for record in cur.fetchall():
        # Обработка рынков
        market_name = record[1] if record[1] is not None else 'Unknown'

        if market_name not in markets:
            markets[market_name] = {
                "id": market_id,
                "name": market_name,
                "city": record[8] if record[8] is not None else 'Unknown',
                "address": [{
                    "street": record[7] if record[7] is not None else 'Unknown',
                    "city": record[8] if record[8] is not None else 'Unknown',
                    "county": record[9] if record[9] is not None else 'Unknown',
                    "state": record[10] if record[10] is not None else 'Unknown',
                    "zip": record[11] if record[11] is not None else 'Unknown'
                }],
                "information": [{
                    "website": record[2] if record[2] is not None else 'Unknown',
                    "facebook": record[3] if record[3] is not None else 'Unknown',
                    "twitter": record[4] if record[4] is not None else 'Unknown', 
                    "youtube": record[5] if record[5] is not None else 'Unknown', 
                    "othermedia": record[6] if record[6] is not None else 'Unknown'
                }],
                "review": record[12] if record[12] is not None else 'Unknown'
            }
            market_id += 1
        else:
            markets[market_name]["address"].append({
                "street": record[7] if record[7] is not None else 'Unknown',
                    "city": record[8] if record[8] is not None else 'Unknown',
                    "county": record[9] if record[9] is not None else 'Unknown',
                    "state": record[10] if record[10] is not None else 'Unknown',
                    "zip": record[11] if record[11] is not None else 'Unknown'
            })

except Exception as e:
    print(f"Ошибка при работе с базой данных: {e}")
finally:
    if 'conn' in locals():
        cur.close()
        conn.close()


# Основной цикл меню
def menu():
    print("\nДобро пожаловать в приложение! Выберите пункт меню:")
    print("1 - Просмотр всех рынков")
    print("2 - Поиск рынков по городу")
    print("3 - Просмотр адреса рынка")
    print("4 - Просмотр информации о рынке")
    print("5 - Оставить рецензию о рынке")
    print("0 - Выход")


# 1
def display_markets(markets_to_display):
    for market in markets_to_display:
        print(f"{market['id']}.{market['name']}")
   
# 2
def find_markets_by_city(city):
    return [market for market in markets.values() if city.lower() in market['city'].lower()]
 
# 3
def find_market(name):
    return [market for market in markets.values() if name.lower() in market['name'].lower()]

def display_address(address_to_display):
    for market in address_to_display:
        print(f"{market['address']}")

#4
def display_information(information_to_display):
    for market in information_to_display:
        print(f"{market['information']}")

# Основной цикл с приложением
while True:
    menu()
    choice = input("")
    
    if choice == '1':
        display_markets(markets.values())
        input("Для продолжения нажмите клавишу Enter...")

    elif choice == '2':
        city = input("Введите город: ")
        markets_in_city = find_markets_by_city(city)
        if markets_in_city:
            print(f"\nСписок рынков в {city}:")
            display_markets(markets_in_city)
        else:
            print(f"Нет рынков в {city}.")
        input("Для продолжения нажмите клавишу Enter...")

    elif choice == '3':
        name = input("Введите название рынка: ")
        address_by_market = find_market(name)
        if address_by_market:
            print(f"\n{name} расположен по адресу:")
            display_address(address_by_market)
        else:
            print(f"Нет такого рынка")
        input("Для продолжения нажмите клавишу Enter...")

    elif choice == '4':
        name = input("Введите название рынка: ")
        information_by_market = find_market(name)
        if information_by_market:
            print(f"\n Подробная информация о рынке {name}:")
            display_information(information_by_market)
        else:
            print(f"Нет такого рынка")
        input("Для продолжения нажмите клавишу Enter...")

    elif choice == '5':
        name = input("Введите название рынка для рецензии: ")
        review = input("Напишите рецензию: ")
        try:
            psycopg.connect(dbname="Export",
                        host="localhost",
                        user="postgres",
                        password="***",                                                                                                                        
                        port="5432")
            cur = conn.cursor()
          
            insert_review = """
            INSERT INTO export (marketname, review)
            VALUES (%s, %s)
            """
            cur.execute(insert_review, (
                name, review
            ))
            conn.commit()
            print(f"Рецензия на рынок '{name}' успешно добавлена в базу данных.")
            
        except Exception as e:
            print(f"Ошибка при добавлении рецензии в базу данных: {e}")
        finally:
            if 'conn' in locals():
                cur.close()
                conn.close()

        input("Для продолжения нажмите клавишу Enter...")

    elif choice == '0':
        print("Выход...")
        break

    else:
        print("Некорректный выбор, попробуйте снова.")