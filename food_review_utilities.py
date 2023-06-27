import sqlite3
from getpass import getpass

database_file = 'food_review.db'

connection = sqlite3.connect(database_file)

cursor = connection.cursor()


def show_menu(connection):
    '''shows items in the menu'''

    sql = "select * from dishes"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f"{'Dish name':<25}{'Desc.':<60}{'Price':<20}{'Dietary Info'}")
    for item in result:
        print(f"{item[1]:<25}{item[2]:<60}{item[3]:<20}{item[4]}")     


def show_food_reviews(connection):
    '''shows food reviews'''

    sql = "select user_name, dish_name, date, review from reviews_vw"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f"{'username':<25}{'dish_name'<30}{'date.':<20}{'review'}")
    for item in result:
            print(f"{item[0]:<25}{item[1]:<20}{item[2]:<20}{item[3]}")     


def search_menu(connection):
    '''searches the menu'''

    try:
        prompt = {1: 'dish_name', 2: 'price', 3: 'dietary_info'}
        answer_1 = int(input("select out of 1. dish_name, 2. price budget, 3. dietary_info: "))
        answer_2 = input("please enter value for {}: ".format(prompt[answer_1])).lower() 
        #chooses what to search with 
        if answer_1 == 1:
            sql = 'select dish_name, price from dishes where lower(dish_name) = ?'
        elif answer_1 == 2:
            sql = 'select dish_name, price from dishes where price <= ?'
            answer_2 = int(answer_2)
        elif answer_1 == 3:
            answer_2 = '%' + answer_2 + '%'
            sql = 'select dish_name, price from dishes where lower(dietary_information) like ?'
        cursor.execute(sql, [answer_2])
        result = cursor.fetchall()
        print(f"{'dish_name':<40}{'price':<15}{'dietary_info':<30}")
        for item in result:
            print(f"{item[0]:<40}{item[1]:<15}{item[2]:<30}")
    except:
         print("sin city wasn't made for you:/ ")


def search_food_review(connection):
    '''searches in the food reviews'''

    try:
        prompt = {1: 'user_name', 2: 'date', 3: 'dish_name'}
        answer_1 = input("select out of 1. user_name, 2. date, 3. dish_name: ")
        answer_1 = int(answer_1)
        answer_2 = input("please enter value for {}: ".format(prompt[answer_1]))
        answer_2 = answer_2.lower()
        #category to search in 
        if answer_1 == 1:
            sql = 'select user_name, date, review, dish_name from reviews_vw where lower(user_name) = ?'
        elif answer_1 == 2:
            sql = 'select user_name, date, review, dish_name from reviews_vw where date = ?'
        elif answer_1 == 3:
            sql = 'select user_name, date, review, dish_name from reviews_vw where lower(dish_name) = ?'
        cursor.execute(sql, [answer_2])
        result = cursor.fetchall()
        print(f"{'dish_name ':20}{'user_name':<20}{'date':<30}{'review':<40}")
        for item in result:
            print(f"{item[3]:<20}{item[0]:<20}{item[1]:<30}{item[2]:<40}")
    except:
         print("sin sin vity wasn't made for you")


def insert_user_food_review(connection):
    '''creates new users'''

    user_name = input('enter a user_name: ')
    gmail = input('enter a gmail: ')
    phone_number = input('enter a phone_number: ')
    password = input('enter a password: ')
    #gets all information needed and then creates a new user
    list = [user_name, gmail, phone_number, password]
    sql = 'insert into users(user_name, gmail, phone_number, password) values (?,?,?,?)'
    cursor.execute(sql, list)
    connection.commit()


def insert_review_food_review(connection):
    '''creates new food reviews'''

    try:
        dish_name = input('what is the name of the dish?: ').lower()
        sql_1 = 'select dish_id from dishes where lower(dish_name) = ?'
        cursor.execute(sql_1, [dish_name])
        dish_id = cursor.fetchone()[0]
        user_name = input('whats your user_name?: ' )
        user_name = user_name.lower()
        password = input('whats your password')
        list = [user_name, password] 
        #verifies that the account is valid
        sql = 'select user_id from users where lower(user_name) = ? and password = ?'
        cursor.execute(sql, list)
        user_id = cursor.fetchone()[0]
        review = input('wts the actual review now?: ')
        date = input('wots the date: ')
        #gets date and review
        list_2 = [dish_id, user_id, date, review]
        sql_2 = 'insert into reviews(dish_id, user_id, date, review) values (?,?,?,?)'
        cursor.execute(sql_2, list_2)
        connection.commit()
    except:
         print("sin city wasnt made for you")


def delete_food_reviews(connection):
    '''deletes food reviews'''

    try: 
        dish_name = input('what is the name of the dish?: ')
        sql_1 = 'select dish_id from dishes where lower(dish_name) = ?'
        cursor.execute(sql_1, [dish_name])
        dish_id = cursor.fetchone()[0]
        #gets the dis id from the name
        user_name = input('whats your user_name?: ' )
        user_name.lower()
        password = input("what is your password?: ")
        list = [user_name, password] 
        #verifies password and username 
        sql = 'select user_id from users where lower(user_name) = ? and password = ?'
        cursor.execute(sql, list)
        user_id = cursor.fetchone()[0]
        list = (user_id, dish_id)
        sql = 'delete from reviews where user_id = ? and dish_id = ?'
        cursor.execute(sql, list)
        connection.commit()
    except:
         print("sin city wasn't made for you")


def update_food_review(connection):
    ''''updates food reviews'''

    try:
        user_name = input('whats your user_name?: ' )
        user_name = user_name.lower()
        password = input("what is your password?: ")
        list = [user_name, password] 
        sql = 'select user_id from users where lower(user_name) = ? and password = ?'
        cursor.execute(sql, list)
        #verifies that the user has a valid review 
        user_id = cursor.fetchone()[0]
        dish_name = input('what is the name of the dish?: ')
        dish_name = dish_name.lower()
        sql_1 = 'select dish_id from dishes where lower(dish_name) = ?'
        cursor.execute(sql_1, [dish_name])
        dish_id = cursor.fetchone()[0]
        review = input('whats the review now?: ')
        list_1 = [review, user_id, dish_id]
        sql = 'update reviews set review = ? where user_id = ? and dish_id = ?'
        cursor.execute(sql, list_1)
        connection.commit()
    except:
         print("sin city wasn't made for you")

