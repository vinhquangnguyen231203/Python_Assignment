class Customer:
    # Constructor
    def __init__(self, id_customer, name, address, gender):
        self.id_customer = id_customer
        self.name = name
        self.address = address
        self.gender = gender

    # Methods:
    # Getter và Setter
    def get_id_customer(self):
        return self.id_customer
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def set_id_customer(self, id_customer):
        self.id_customer = id_customer
    
    def set_name(self, name):
        self.name = name
    
    def set_address(self, address):
        self.address = address

    def set_gender(self,gender):
        self.gender = gender
    
    def get_gender(self):
        return self.gender

    # to String
    def toString(self):
        return f"{self.id_customer}, {self.name}, {self.address}, {self.gender}"