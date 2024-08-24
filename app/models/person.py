class Person:
    """
    A class to represent a person with a unique identifier and personal details. This class will be used as a base class for other classes in the application.
    
    Attributes:
    -----------
    last_id : int
        A class attribute to store the last unique identifier assigned to a person object.

    id: int
        A unique identifier for a person object.
    
    __first_name: str
        Instance variable that stores the first name of the person

    __surname: str
        Instance variable that stores the surname of the person

    Methods:
    --------
    ___init__(self, first_name: str, surname: str):
        Initializes a new instance of the Person class with the given first name and surname.
    
    get_unique_hospital_id(self) -> int:
        Returns the unique identifier of the person object.
    
    full_name(self) -> str:
        Returns the full name of the person object.
    
    get_first_name(self) -> str:
        Returns the first name of the person object.
    
    set_first_name(self, new_first_name: str):
        Sets the first name of the person object to the given value.

    get_surname(self) -> str:
        Returns the surname of the person object.

    set_surname(self, new_surname: str):
        Sets the surname of the person object to the given value. 
    """
    last_id = 0

    def __init__(self, first_name: str , surname: str) -> None:
        """
        Initializes a new instance of the Person class with the given first name and surname.

        Parameters:
        -----------
        first_name: str
            The first name of the person.
        
        surname: str
            The surname of the person.
        """
        self.id = Person.last_id + 1
        Person.last_id += 1
        self.__first_name = first_name
        self.__surname = surname

    def get_unique_hospital_id(self) -> int:
        """
        Returns the unique identifier of the person object.

        Returns:
        --------
        int 
            The unique identifier of the person object.
        """
        return self.id

    def full_name(self) -> str:
        """
        Returns the full name of the person object.

        Returns:
        --------
        str
            The full name of the person object.
        """
        return f'{self.__first_name} {self.__surname}'
    
    def get_first_name(self) -> str:
        """
        Returns the first name of the person.

        Returns:
        --------
        str
            The first name of the person.
        """
        return self.__first_name
    
    def set_first_name(self, new_first_name: str) -> None:
        """
        Updates the first name of the person 

        Parameters:
        -----------
        new_first_name: str
            The new first name of the person.
        """
        self.__first_name = new_first_name 

    def get_surname(self) -> str:
        """
        Returns the surname of the person.

        Returns:
        --------
        str
            The surname of the person.
        """
        return self.__surname
    
    def set_surname(self, new_surname: str) -> None:
        """
        Updates the surname of the person.

        Parameters:
        -----------
        new_surname: str
            The new surname of the person.
        """
        self.__surname = new_surname
