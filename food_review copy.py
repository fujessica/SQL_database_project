from food_review_utilities import show_menu, show_food_reviews, search_menu, search_food_review, insert_user_food_review, insert_review_food_review, delete_food_reviews, update_food_review
import sqlite3

database_file = 'food_review.db'

connection = sqlite3.connect(database_file)

while True:
    answer = input('what would you like to do with? 1. menu 2. reviews 3. exit?: ')
    if answer == '1':
        answer_1 = input('would you like to search?(yes or no): ').lower()
        if 'y' in answer_1:
            search_menu(connection)
        else:
            show_menu(connection)
    elif answer == '2':
        list_1 = {1: 'show', 2: 'edit'}
        answer_2 = int(input('would you like to 1. see or 2. edit?: '))
        if answer_2 == 1:
            while True:
                answer = input('wanna search?(yes or no): ').lower()
                if 'y' in answer:
                    search_food_review(connection)
                    break
                elif 'n' in answer:
                    show_food_reviews(connection)
                    break
                else:
                    print('be more blunt please :D')

        elif answer_2 == 2:
            while True:
                answer = input('do you have a user?: ')
                if 'y' in answer:
                    answer = input('what would you like to do? 1: create a review, 2: delete a review, 3: update a review?: ')
                    if answer == '1':
                        insert_review_food_review(connection)
                        break
                    elif answer == '2':
                        delete_food_reviews(connection)
                        break
                    elif answer == '3':
                        update_food_review(connection)
                        break
                    else:
                        print("kys")
                        break
                elif 'n' in answer:
                    insert_user_food_review(connection)
                else:
                    print('be more blunt please')
        else: 
            print('fadijfasdfds')
    else:
        break

            


