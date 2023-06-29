from food_review_utilities import show_menu, show_food_reviews, search_menu, search_food_review, insert_user_food_review, insert_review_food_review, delete_food_reviews, update_food_review
import sqlite3

database_file = 'food_review.db'

connection = sqlite3.connect(database_file)

'''final code'''

while True:
    choice_1 = input('what would you like to do with? 1. menu 2. reviews 3. exit?: ')
    if choice_1 == '1':
        while True:
            menu_search = input('would you like to search? (y/n): ').lower()
            if 'y' in menu_search:
                search_menu(connection)
                break
            elif 'n' in menu_search:
                show_menu(connection)
                break
            else:
                print("try again")
    elif choice_1 == '2':
        while True:
            choice_2 = input('would you like to 1. see or 2. edit?: ')
            confirmation = input('are you sure? (y/n): ')
            if 'y' in confirmation:
                if choice_2 == '1':
                    while True:
                        review_search = input('wanna search? (y/n): ').lower()
                        if 'y' in review_search:
                            search_food_review(connection)
                            break
                        elif 'n' in review_search:
                            show_food_reviews(connection)
                            break
                        else:
                            print('be more blunt please :D')
                elif choice_2 == '2':
                    while True:
                        users = input('do you have a user? (y/n): ')
                        if 'y' in users:
                            while True:
                                choice_3 = input('what would you like to do? 1: create a review, 2: delete a review, 3: update a review, 4: back?: ')
                                if choice_3 == '1':
                                    insert_review_food_review(connection)
                                    break
                                elif choice_3 == '2':
                                    delete_food_reviews(connection)
                                    break
                                elif choice_3 == '3':
                                    update_food_review(connection)
                                    break
                                elif choice_3 == '4':
                                    break
                                else:
                                    print("no")
                                break
                        elif 'n' in users:
                            insert_user_food_review(connection)
                        else:
                            print('be more blunt please')
                        break
                else: 
                    print('sorry, dont understand your answer.')
                break
    elif choice_1 == '3':
        break
    else:
        print("try again :C")
