class PhoneNumber:
    def __init__(self, provider=None, customer=None, number=None):
        self.provider = provider
        self.customer = customer
        self.number = number

    def get_provider(self):
        return self.provider

    def set_provider(self, provider):
        self.provider = provider

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def toString(self):
        return f"{self.number}, {self.provider}, [{self.customer.toString()}]"

