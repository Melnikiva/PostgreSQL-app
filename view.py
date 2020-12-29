class View(object):

    @staticmethod
    def show_menu():
        print()
        print("Select operation: ")
        print("1. Add new purchase")
        print("2. Update product price")
        print("3. Delete purchase")
        print("4. Generate N purchases")
        print("5. Search for product")
        print("6. Exit")
        print()

    @staticmethod
    def display_input_code_dialog():
        print("Input product code: ")

    @staticmethod
    def display_new_price():
        print("Input new price: ")

    @staticmethod
    def display_input_n_dialog():
        print("Input N: ")

    @staticmethod
    def display_input_id():
        print("Input purchase id: ")

    @staticmethod
    def display_error_dialog():
        print("Invalid input")

    @staticmethod
    def display_done():
        print("Command has been done")

    @staticmethod
    def display_search_dialog():
        print("Input string to search")

    @staticmethod
    def display_results(results, time):
        for single in results:
            print("Code: {} | Description: {} | Price: {} | Storage: {}"
                  .format(single[0], single[1], single[2], single[3]))
        print("Time: {} ms".format(time * 1000))
