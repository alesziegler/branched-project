class Customer:
    """
    This class defines an object whose attributes
    are passed from outside through validating setters.
    The core property of this object is a dictionary, whose keys are
    immutable from outside, and whose values are validated inputs.
    """
    
    def __init__(self):
        """
        name:passed on from outside through a setter
        age: dtto
        contact: dtto
        identifiers: core attribute of this class.
        After name, age and contact inputs are validated,
        their values are in their setters automatically entered into this dictionary.
        age_count: for purposes of age validation:
        if users try to enter age over 100, they are asked once whether they really mean it,
        but if they do, on the next attempt it's allowed.
        """
        self.__name = None
        self.__age = None
        self.__contact = None
        self.__identifiers = {
            "name": self.__name,
            "age": self.__age,
            "contact": self.__contact,
        }
        self.__age_count = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if len(n) != 2:
            """
            Name has to be two objects in an iterable (given name and surname). 
            This validation step is superflous in this app because of the way input is entered, 
            but if Customer class would be repurposed for something else, it would be essential.
            """
            raise ValueError("Je nutno zadat jmeno a prijmeni (dve slova)")

        given_name = n[0]
        surname = n[1]

        try:
            """
            Validation is performed separately for name and surname,
            in a method that is identical for both. 
            """
            self.name_validation(given_name, "krestnim jmenu")
            self.name_validation(surname, "prijmeni")
        except ValueError as error_message:
            raise ValueError(error_message)
        else:
            self.__name = given_name + " " + surname
            self.__identifiers["name"] = self.__name

    def name_validation(self, name, locator):
        """
        Method for validating name
        (defined solely for purposes of avoiding repeated code for given name and surname)
        """
        if not name:
            raise ValueError("Je nutno zadat jmeno i prijmeni")

        czech_alphabet = "abcdefghijklmnopqrstuvwxyzáčďéěíňóřšťúůýž"
        for letter in name:
            if letter.lower() not in czech_alphabet:
                raise ValueError(
                    f"Vsechny znaky v {locator} musi byt soucasti ceske abecedy. "
                    f"V {locator} nesmi byt mezery. Zadejte prosim krestni jmeno i prijmeni znovu."
                )

        if not name[0].isupper():
            raise ValueError(
                f"Prvni pismeno v {locator} musi byt velke. "
                f"Zadejte prosim krestni jmeno i prijmeni znovu."
            )
        if not name[1::].islower():
            raise ValueError(
                f"Velke pismeno muze byt v {locator} jen na zacatku. "
                f"Zaroven krestni jmeno i prijmeni nesmi byt jen jedno pismeno."
                f"Zadejte prosim krestni jmeno i prijmeni znovu."
            )

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, a):
        try:
            int(a)
        except ValueError:
            raise ValueError("Vek musi byt cislo (bez mezer mezi cislicemi)")
        else:
            if int(a) < 18:
                raise ValueError("Vek musi byt nejmene 18")
                """
            elif int(a) > 100:
                if self.__age_count == 0:
                    self.__age_count += 1
                    #print(count)
                    raise ValueError("Jste si jisti, ze pojistenci je vic jak 100 let?"
                                     "Zadejte prosim vek znovu.")
                                     """
            else:
                self.__age = a
                self.__identifiers["age"] = self.__age

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, t):
        try:
            int(t)
        except ValueError:
            raise ValueError("telefonni cislo musi obsahovat pouze cislice bez mezer")
        else:
            if len(t) != 9:
                raise ValueError("telefonni cislo musi obsahovat presne 9 cislic bez mezer")
            else:
                self.__contact = t
                self.__identifiers["contact"] = self.__contact

    @property
    def identifiers(self):
        """
        dictionary of identifiers doesn't have a setter,
        since it is not supposed to be changed from the outside of this class.
        """
        return self.__identifiers

    def __str__(self):
        """
        this method is superfluous in this app, since
        customers are delivered to the database in the form of dictionaries, not strings.
        It would of course be possible to make them into strings and then split them and
        create a dictionary in the Database class, but that would be more complicated and I am not aware of any advantages.
        """
        return f"{self.name}, {self.contact}, {self.age}"
