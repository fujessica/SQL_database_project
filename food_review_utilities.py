
'''utilities'''


def show_menu(connection):
    '''shows items in the menu'''
    cursor = connection.cursor()
    sql = "SELECT * FROM dishes"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f"{'Dish name':<45}{'Desc.':<80}{'Price':<20}{'Dietary Info'}")
    for item in result:
        print(f"{item[1]:<45}{item[2]:<80}{item[3]:<20}{item[4]}")     


def show_food_reviews(connection):
    '''shows food reviews'''
    cursor = connection.cursor()
    sql = "SELECT user_name, dish_name, date, review FROM reviews_vw"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f"{'username':<25}{'dish_name':<45}{'date':<20}{'review'}")
    #displays headings
    for item in result:
        print(f"{item[0]:<25}{item[1]:<45}{item[2]:<20}{item[3]}")
        #prints items 


def search_menu(connection):
    '''searches the menu'''
    cursor = connection.cursor()
    try:
        prompt = {1: 'dish_name', 2: 'price', 3: 'dietary_info'}
        answer_1 = int(input("select out of 1. dish_name, 2. price budget, 3. dietary_info: "))
        answer_2 = input("please enter value for {}: ".format(prompt[answer_1])).lower() 
        #chooses what to enter into the search
        if answer_1 == 1:
            sql = 'SELECT dish_name, price, dietary_information FROM dishes WHERE lower(dish_name) = ?'
        elif answer_1 == 2:
            sql = 'SELECT dish_name, price, dietary_information  FROM dishes WHERE price <= ?'
        elif  answer_1 == 3:
            answer_2 = '%' + answer_2 + '%'
            #enables the 'like' function in sql 
            sql = 'SELECT dish_name, price, dietary_information FROM dishes WHERE lower(dietary_information) LIKE ?'
        cursor.execute(sql, [answer_2])
        result = cursor.fetchall()
        if result == []:
            print('sorry no such dish!')
        else:
            print(f"{'dish_name':<40}{'price':<15}{'dietary_info':<30}")
            for item in result:
                print(f"{item[0]:<40}{item[1]:<15}{item[2]:<30}")
    except:
        print("sin city wasn't made for you:/ ")


def search_food_review(connection):
    '''searches in the food reviews'''
    cursor = connection.cursor()
    try:
        prompt = {1: 'user_name', 2: 'date', 3: 'dish_name'}
        answer_1 = input("select out of 1. user_name, 2. date, 3. dish_name: ")
        answer_1 = int(answer_1)
        answer_2 = input("please enter value for {}: ".format(prompt[answer_1]))
        answer_2 = answer_2.lower()
        #category to search in 
        if answer_1 == 1:
            sql = 'SELECT user_name, date, review, dish_name FROM reviews_vw WHERE lower(user_name) = ?'
        elif answer_1 == 2:
            sql = 'SELECT user_name, date, review, dish_name FROM reviews_vw WHERE date = ?'
        elif answer_1 == 3:
            sql = 'SELECT user_name, date, review, dish_name FROM reviews_vw WHERE lower(dish_name) = ?'
        cursor.execute(sql, [answer_2])
        result = cursor.fetchall()
        if result == []:
            print('sorry no results!')
        else:
            print(f"{'dish_name ':<30}{'user_name':<20}{'date':<15}{'review':<40}")
            for item in result:
                print(f"{item[3]:<30}{item[0]:<20}{item[1]:<15}{item[2]:<40}")
    except:
        print("sin sin vity wasn't made for you")


def insert_user_food_review(connection):
    '''creates new users'''
    while True:
        try:
            cursor = connection.cursor()
            user_name = input('enter a user_name: ')
            gmail = input('enter a gmail: ')
            phone_number = input('enter a phone_number: ')
            password = input('enter a password: ')
            #gets all information needed AND then creates a new user
            list = [user_name, gmail, phone_number, password]
            sql = 'INSERT INTO users(user_name, gmail, phone_number, password) VALUES (?,?,?,?)'
            #creates new user
            cursor.execute(sql, list)
            connection.commit()
            break
        except:
            print('username taken, probably try again')


def insert_review_food_review(connection):
    '''creates new food reviews'''
    cursor = connection.cursor()
    try:
        dish_name = input('what is the name of the dish?: ').lower()
        sql_1 = 'SELECT dish_id FROM dishes WHERE lower(dish_name) = ?'
        cursor.execute(sql_1, [dish_name])
        dish_id = cursor.fetchone()[0]
        user_name = input('whats your user_name?: ' )
        user_name = user_name.lower()
        password = input('whats your password?: ')
        list = [user_name, password] 
        #verifies that the account is valid
        sql = 'SELECT user_id FROM users WHERE lower(user_name) = ? AND password = ?'
        cursor.execute(sql, list)
        user_id = cursor.fetchone()[0]
        review = input('wts the actual review now?: ')
        date = input('wots the date: ')
        #gets date and review
        list_2 = [dish_id, user_id, date, review]
        sql_2 = 'INSERT INTO reviews(dish_id, user_id, date, review) VALUES (?,?,?,?)'
        cursor.execute(sql_2, list_2)
        connection.commit()
    except:
        print("sin city wasnt made for you")



def delete_food_reviews(connection):
    '''deletes food reviews'''
    cursor = connection.cursor()
    try: 
        dish_name = input('what is the name of the dish?: ')
        dish_name = dish_name.lower()
        sql_1 = 'SELECT dish_id FROM dishes WHERE lower(dish_name) = ?'
        cursor.execute(sql_1, [dish_name])
        dish_id = cursor.fetchone()[0]
        #gets the dis id from the name
        user_name = input('whats your user_name?: ' )
        user_name.lower()
        password = input("what is your password?: ")
        list = [user_name, password] 
        #verifies password and username 
        sql = 'SELECT user_id FROM users WHERE lower(user_name) = ? AND password = ?'
        cursor.execute(sql, list)
        user_id = cursor.fetchone()[0]
        list = (user_id, dish_id)
        sql = 'DELETE FROM reviews WHERE user_id = ? AND dish_id = ?'
        cursor.execute(sql, list)
        connection.commit()
    except:
        print("sin city wasn't made for you")


def update_food_review(connection):
    ''''updates food reviews'''
    cursor = connection.cursor()
    try:
        user_name = input('whats your user_name?: ' )
        user_name = user_name.lower()
        password = input("what is your password?: ")
        list = [user_name, password] 
        sql = 'SELECT user_id FROM users WHERE lower(user_name) = ? AND password = ?'
        cursor.execute(sql, list)
        #verifies that the user has a valid review 
        user_id = cursor.fetchone()[0]
        dish_name = input('what is the name of the dish?: ')
        dish_name = dish_name.lower()
        sql_1 = 'SELECT dish_id FROM dishes WHERE lower(dish_name) = ?'
        cursor.execute(sql_1, [dish_name])
        #gets dish id AND user id
        dish_id = cursor.fetchone()[0]
        review = input('whats the review now?: ')
        list_1 = [review, user_id, dish_id]
        sql = 'UPDATE reviews SET review = ? WHERE user_id = ? AND dish_id = ?'
        cursor.execute(sql, list_1)
        connection.commit()
    except:
        print("sin city wasn't made for you")

#atethat
