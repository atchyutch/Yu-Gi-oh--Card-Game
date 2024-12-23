###########################################################
#  Yu-Gi-Oh! Trading Card Game
#
#  Project Algorithm
#    -prompt the user to enter the  file name to open using the open_file function
#    -open file and read teh data using read_card_data function
#    -loop for user options until exit is chosen
#       if option is to check all cards:
#           - sort the cards and display the first 50 cards
#           - compute the stats and display the stats
#       if option is to search cards:
#           -prompt for search query and category until a correct category is entered
#           -search and display results with stats
#       if option is to view decklist:
#           prompt for decklist file name
#           read decklist and display card details with stats
#       if option is to exit:
#           break the loop and display a Thank you message
###########################################################

import csv
from operator import itemgetter

CATEGORIES = ["id", "name", "type", "desc", "race", "archetype", "card price"]


def open_file(prompt_str):
    """
    The function opens a file in th read mode and returns the file pointer, everything is in the while loop to user
    to enter the file name until a correct file is entered.
    """
    while True:
        try:  # try to open the file and if the file is not found, prompt the user to enter the file name again
            fp = open(prompt_str, "r", encoding="utf-8")
            return fp
        except FileNotFoundError:
            print("\nFile not Found. Please try again!")
            prompt_str = input("\nEnter cards file name: ")


def read_card_data(fp):
    """
    The function reads the csv files and takes each line of the file as a tuple and stores inside a list through
    a for loop. Then it sorts the list by the price of the cards and the name of the cards. It returns the list of cards
    """
    card_data = []
    card_csv_reader = csv.reader(fp)
    next(card_csv_reader, None)
    for row in card_csv_reader:  # loop through the csv file and append the cards to the list in the form of a tuple
        card_data.append(
            (row[0].strip(), row[1].strip()[:45], row[2].strip(), row[3].strip(), row[4].strip(), row[5].strip(),
             float(row[6].strip())))
    card_data.sort(key=itemgetter(6, 1))  # sort the card data based on the price and name of the cards
    return card_data


def read_decklist(fp, card_data):
    """
    The function reads the decklist file and takes each line of the file as a tuple and stores inside a list through
    a for loop. Then it sorts based on price and name of cards, finally returns a list of cards
    """
    decklist_data = []
    decklist_csv_reader = csv.reader(fp)
    for row in decklist_csv_reader:
        for card in card_data:  # loop through the card data and append the cards that are in the decklist
            if row[0] in card:
                decklist_data.append(card)
        decklist_data.sort(key=itemgetter(6, 1))  # sort the decklist data based on the price and name of the cards
    return decklist_data


def search_cards(card_data, query, category_index):
    """
    The function searched through the card data that is provided and returns the cards that match the query and category
    inputted by the user.
    """
    result = []
    for card in card_data:
        if query in card[category_index]:
            result.append(card)
    result.sort(key=itemgetter(6, 1))
    return result


def compute_stats(card_data):
    """
    The function computes the minimum, maximum and median price of the cards and returns the cards that have minimum,
    maximum and median price using a for loop and list method called append. Then it sorts the cards based on price and
    returns them.
    """
    card_data.sort(key=itemgetter(6, 1))
    # since we have sorted the card data, the minimum price is the first card and the maximum price is the last card
    min_price_card = card_data[0][6]
    max_price_card = card_data[-1][6]
    med_price_card = card_data[len(card_data) // 2][6]  # median price is the middle value of the list of cards
    min_cards = []
    max_cards = []
    med_cards = []
    for card in card_data:  # loop through the card data and append the cards with minimum, maximum and median price
        if card[6] == min_price_card:
            min_cards.append(card)
        if card[6] == max_price_card:
            max_cards.append(card)
        if card[6] == med_price_card:
            med_cards.append(card)
    # sort the cards based on the name of the cards
    min_cards.sort(key=itemgetter(1))
    max_cards.sort(key=itemgetter(1))
    med_cards.sort(key=itemgetter(1))
    return min_cards, min_price_card, max_cards, max_price_card, med_cards, med_price_card


def display_data(card_data):
    """
    The function displays the card data in a formatted way using the format() method and a for loop to iterate through
    the list of cards.
    """
    print(f"{'Name'.ljust(50)}{'Type'.ljust(30)}{'Race'.ljust(20)}{'Archetype'.ljust(40)}{'TCGPlayer'.ljust(12)}")
    total_price = 0
    for card in card_data:  # loop through the card data and display the cards with left justification
        price_formatted = f"{card[6]:,.2f}".center(12)
        print(f"{card[1].ljust(50)}{card[2].ljust(30)}{card[4].ljust(20)}{card[5].ljust(40)}{price_formatted}")
        total_price += card[6]
    print()
    total_price = f"{total_price:,.2f}".center(12)
    # display the total price of the cards but formatted in a way where only two columns are printed
    print(f"{'Totals'.ljust(50)}{''.ljust(30)}{''.ljust(20)}{''.ljust(40)}{total_price}")


def display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price):
    """
    The function displays the minimum, maximum and median price of the cards in a formatted way using the f-strings and
    a for loop to iterate through the list of cards.
    """
    print(f"\nThe price of the least expensive card(s) is {min_price:,.2f}")
    for i in min_cards:
        print(f"\t{i[1]}")
    print(f"\nThe price of the most expensive card(s) is {max_price:,.2f}")
    for j in max_cards:
        print(f"\t{j[1]}")
    print(f"\nThe price of the median card(s) is {med_price:,.2f}")
    for k in med_cards:
        print(f"\t{k[1]}")


def main():
    prompt = input("\nEnter cards file name: ")
    card_fp = open_file(prompt)
    card_data = read_card_data(card_fp)
    while True:  # loop to prompt the user to enter the option until exit is chosen
        # prompt the user to enter the option using an input function and display the options
        print("\nYu-Gi-Oh! Card Data Analysis")  # instead of using a MENU I printed each statement
        print("1) Check All Cards")
        print("2) Search Cards")
        print("3) View Decklist")
        print("4) Exit")
        option_choice = input("\nEnter option: ")
        if option_choice == "1":  # if the user enters 1, the cards are sorted and displayed with stats
            card_data.sort(key=itemgetter(6))
            print(f"\nThere are {len(card_data)} cards in the dataset.")
            cheap_cards = card_data[:50]  # list formatted to display the first 50 cards as they are sorted by price
            display_data(cheap_cards)
            min_cards, min_price, max_cards, max_price, med_cards, med_price = compute_stats(card_data)
            display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price)
        elif option_choice == "2":  # the cards are searched based on query in that category and displayed with stats
            prompt_for_query = input("\nEnter query: ")
            while True: # Loop is used to prompt the user to enter the category until a correct category is entered
                prompt_for_category = input("\nEnter category to search: ").lower()  # prompt is converted to lower case
                if prompt_for_category not in CATEGORIES:
                    print("\nIncorrect category was selected!")
                else:
                    # if the category is correct, the index of the category in the list is stored in a variable
                    if prompt_for_category == "id":
                        prompt_index = 0
                    elif prompt_for_category == "name":
                        prompt_index = 1
                    elif prompt_for_category == "type":
                        prompt_index = 2
                    elif prompt_for_category == "desc":
                        prompt_index = 3
                    elif prompt_for_category == "race":
                        prompt_index = 4
                    elif prompt_for_category == "archetype":
                        prompt_index = 5
                    elif prompt_for_category == "card price":
                        prompt_index = 6
                    break
            searched_cards = search_cards(card_data, prompt_for_query, prompt_index) # search the cards based on query
            print("\nSearch results")
            if len(searched_cards) == 0:  # if there are no cards with the query in the category
                print(f"\nThere are no cards with '{prompt_for_query}' in the '{prompt_for_category}' category.")
            else:
                print(f"\nThere are {len(searched_cards)} cards with '{prompt_for_query}' in the '{prompt_for_category}' category.")
                display_data(searched_cards) # display the cards that match the query and category
                min_cards, min_price, max_cards, max_price, med_cards, med_price = compute_stats(searched_cards)
                display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price)
        elif option_choice == "3": # the decklist is read and displayed with stats
            prompt_for_decklist = input("\nEnter decklist filename: ")
            decklist_file = open_file(prompt_for_decklist)  # open the decklist file
            decklist_information = read_decklist(decklist_file, card_data)  # read the decklist file
            print("\nSearch results")
            display_data(decklist_information)  # display the decklist information
            min_cards, min_price, max_cards, max_price, med_cards, med_price = compute_stats(decklist_information)
            display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price)
        elif option_choice == "4":  # if the user enters 4, the loop is broken and a thankyou message is displayed
            print("\nThanks for your support in Yu-Gi-Oh! TCG")
            break
        else:
            print("\nInvalid option. Please try again!")


if __name__ == "__main__":
    main()
