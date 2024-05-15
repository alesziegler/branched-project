class Database:
    """
    This class will have methods which
    will be called directly from controller.
    Probably it will essentially be a list of Persons,
    i.e. essentially list of dictionaries.
    It should def have add method, print all method, and find method
    add method should have an equal thing used for validation
    (so it would be impossible to have two identical customers)
    Maybe we should not store here person objects, but
    dictionaries roughly equivalent to them?

    """

    def __init__(self):
        self.__core_database = []

    def add_new_customer(self, new_customer):
        for customer in self.__core_database:
            if customer == new_customer:
                raise ValueError("Tento pojistenec uz je v evidenci.")


        self.__core_database.append(new_customer)
        #print("test append")
        #print(new_customer.values())

    def find_customer_by_category(self,category, query):

        count = 0

        result = "Vysledky hledani: \n"
        for customer in self.__core_database:
            if str(customer[category].lower()) == query.lower():
                #result += "jmeno, vek, telefon\n"
                #print(customer)
                """
                customer should be printed in the same format is in str method.
                
                """
                result += f"jmeno: {customer['name']},vek: {customer['age']},telefon: {customer['contact']}\n"
                count += 1
        result += f"Nalezeno {count} vysledku."
        #print(result)
        return result

    def __str__(self):
        """
        This is used for fetching the whole database
        """
        printable_table = "jmeno,vek,telefon:\n"
        count = 0
        for customer in self.__core_database:
            printable_customer = (
                f"{customer['name']},{customer['age']},{customer['contact']}\n")
            printable_table += printable_customer
            count += 1
            """
             so, we need to do what?
             ideally, a matrix, somehow.
             First line would be: jmeno, vek, telefon
             """
        printable_table += f"Celkem {count} pojistencu."
        return printable_table
