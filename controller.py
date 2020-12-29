import time


class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_menu(self):
        while 1:
            self.view.show_menu()
            option = int(input())
            if option == 1:
                self.view.display_input_code_dialog()
                code = input()
                if not self.model.insert_purchase(code):
                    self.view.display_error_dialog()
                else:
                    self.view.display_done()

            elif option == 2:
                self.view.display_input_code_dialog()
                code = input()
                self.view.display_new_price()
                new_price = input()

                if code.isnumeric():
                    isfloat = False
                    try:
                        float(new_price)
                        isfloat = True
                    except ValueError:
                        print("Not a float")
                    if isfloat:
                        self.model.update_price(code, new_price)
                        self.view.display_done()
                else:
                    self.view.display_error_dialog()

            elif option == 3:
                self.view.display_input_id()
                code = input()
                if code.isnumeric():
                    self.model.delete_purchase(code)
                else:
                    self.view.display_error_dialog()

            elif option == 4:
                self.view.display_input_n_dialog()
                n = input()
                if n.isnumeric():
                    self.model.insert_random_purchases(int(n))
                else:
                    self.view.display_error_dialog()

            elif option == 5:
                self.view.display_search_dialog()
                example = input()
                start_time = time.time()
                result = self.model.search_product(example)
                end_time = time.time()
                self.view.display_results(result, end_time - start_time)

            elif option == 6:
                break

            else:
                self.view.display_error_dialog()
