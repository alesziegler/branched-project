from customer import Customer
from database import Database


class Interface:
    """
    Instance of this class handles all communication with users.
    It also shuffles newly created customers
    to a database (only backend inter-object operation in this app)
    """

    def __init__(self):
        """
        Initialization of an instance of this class is an equivalent of launch of the app.
        Empty instance of customer database is automatically initialized.
        Main menu is automatically opened.
        """
        self.database = Database()
        self.choosing_from_main_menu()

    def make_user_pick(self):
        """
        input function used for both main menu and search menu.
        """
        chosen_action = input("Vyberte si akci ze seznamu vyse: ")
        return chosen_action

    def choosing_from_main_menu(self):
        """
        this method:
        1) prints main menu,
        2) makes users pick one of its options,
        3) redirects users to relevant further processes according to their decisions,
        4) after that recursively begins itself again until user picks the exit option.
        """
        print("""
                Vase moznosti:\n
                1 - Pridat noveho pojisteneho\n
                2 - Vypsat vsechny pojistene\n
                3 - Vyhledat pojisteneho\n
                4 - Konec
                """)

        chosen_option = self.make_user_pick()

        match chosen_option:
                case "1":
                    self.add_new_customer()
                case "2":
                    self.print_all_customers()
                case "3":
                    self.find_customer()
                case "4":
                    return
                case _:
                    print("Tohle neni spravna volba. Vyberte si prosim lepe.")
        self.choosing_from_main_menu()

    def validate_input(self, boolean, property_of_object, prompt1, prompt2=None):
        """
         (Unfortunately this doesn't work;
         I am leaving it here in the hope that I'll be able to fix that later)
        """
        pass
        """
        This static method abstracts validation of user input, to avoid repeating code:
        :param boolean:
            while True, user is repeatedly asked for input.
            It becomes False when correct input is received from user.
        :param property_of_object:
        this is the property where we put validated input.
        :param prompt1:
        Variable input prompt.
        :param prompt2:
        optional second input prompt (here used for validating name(given_name,surname))
        """
        """
        while boolean:
            data_added_to_object = input(prompt1)
            if prompt2 is not None:
                additional_data = input(prompt2)
                data_added_to_object = (data_added_to_object, additional_data)
            try:
                property_of_object = data_added_to_object
            except ValueError as error_message:
                # this is a custom message, defined in property setter
                print(error_message)
            else:
                # when validation successful, boolean switches and process moves on:
                boolean = False
        """

    def add_new_customer(self):
        """
        Method to add new customers to a database (duh).
        Boolean variables are used in while cycles
        to force user to add valid input.
        New instance od Customer class is initialized;
        essentially its core is a dictionary whose values are to be filled
        by user input.
        After being filled with valid input, dictionary is then added
        to an instance of Database class, initialized in constructor of this class.
        """
        name_invalid = True
        contact_invalid = True
        age_invalid = True

        new_customer = Customer()

        """
        unfortunately this doesn't work
        (it asks for inputs,but it fails to pass input into setter,
        and continues with the next step):
        self.validate_input(
            name_invalid,
            new_customer.name,
            "Zadejte krestni jmeno pojistence (bez mezer): ",
            "Zadejte prijmeni pojistence (bez mezer): "
        )
        """
        while name_invalid:
            # this a stupidly repetitive way to do validation since clever method above doesn't work
            given_name = input("Zadejte krestni jmeno pojistence (bez mezer): ")
            surname = input("Zadejte prijmeni pojistence (bez mezer): ")
            # name is a tuple because Customer class requires it for validation purposes:
            full_name = (given_name, surname)

            try:
                # try/except statements used to avoid crashing the program if validation fails
                new_customer.name = full_name
            except ValueError as error_message:
                # this is a custom message, defined in setter:
                print(error_message)
            else:
                name_invalid = False

        while age_invalid:
            # this a stupidly repetitive way to do validation since clever method above doesn't work
            age = input("Zadejte vek pojistence: ")
            try:
                # try/except statements used to avoid crashing the program if validation fails
                new_customer.age = age
            except ValueError as error_message:
               # this is a custom message, defined in setter:
               print(error_message)
            else:
                age_invalid = False

        while contact_invalid:
            # this a stupidly repetitive way to do validation since clever method above doesn't work
            contact = input("Zadejte telefon pojistence: ")
            try:
                # try/except statements used to avoid crashing the program if validation fails
                new_customer.contact = contact
            except ValueError as error_message:
                # this is a custom message, defined in setter:
                print(error_message)
            else:
                contact_invalid = False
        try:
            self.database.add_new_customer(new_customer.identifiers)
            print("Novy pojistenec zadan do evidence.\n")
        except ValueError as error_message:
            print(error_message)
        #self.choosing_from_main_menu()

    def print_all_customers(self):
        """
        This method calls str method of
        Database object initialized in the constructor of this class.
        """
        print(self.database)

    def find_customer(self):
        print("""
        Chcete vyhledat pojisteneho:\n
        1) podle jmena a prijmeni?\n
        2) podle veku?\n
        3) podle telefoniho cisla?\n
        4) rozmyslel jsem si to. Nic hledat nechci.
        """)
        query = self.make_user_pick()

        match query:
            case "1":
                name_query = input("Zadejte prosim hledane jmeno a prijmeni, oddelene mezerou: ")
                print(self.database.find_customer_by_category("name",name_query))
            case "2":
                age_query = input("Zadejte prosim hledany vek: ")
                print(self.database.find_customer_by_category("age",age_query))
            case "3":
                contact_query = input("Zadejte prosim hledane telefonni cislo (9 cislic bez mezer): ")
                print(self.database.find_customer_by_category("contact",contact_query))
            case "4":
                print("Ok. Vitejte zpatky v hlavnim menu.")
                return
            case _:
                print("Tohle je spatna volba. Vyberte si prosim lepe.")

        self.find_customer()




