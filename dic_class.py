class DicParser:
    """This is a dictionary parser class"""

    def __init__(self, d):
        self.d = d

    def get_keys(self):
        if self.not_dic():
            return list(self.d.keys())

    def get_values(self):
        if self.not_dic():
            return list(self.d.values())

    def not_dic(self):
        if type(self.d) != dict:
            raise Exception(f'{self.d} is not a dictionary')
        return True

    def user_input(self):
        while True:
            keys = input("Enter a dictionary key: ")
            values = input("Enter a dictionary value: ")
            if keys == "-1" or values == "-1":
                break
            else:
                self.d[keys] = values
        return self.d

    def insertion(self, k, v):
        """This method takes a key and value pair and insert in the ready_made dictionary"""
        self.d[k] = v
        return self.d


class DicParser2:
    """This is a dictionary parser class"""

    def __init__(self, d):
        self.d = d

    def get_keys(self):
        if self.not_dic():
            return list(self.d.keys())

    def get_values(self):
        if self.not_dic():
            return list(self.d.values())

    def not_dic(self):
        if type(self.d) != dict:
            raise Exception(f'{self.d} is not a dictionary')
        return True

    def user_input(self):
        while True:
            keys = input("Enter a dictionary key: ")
            value = input("Enter a dictionary value: ")
            self.d[keys] = value
            if keys == "-1" or value == "-1":
                break
        return self.d

    def insertion(self, k, v):
        """This method takes a key and value pair and insert in the ready_made dictionary"""
        self.d[k] = v
        return self.d


class DicParser3:
    """This is a dictionary parser class"""

    def __init__(self, d):
        self.d = d

    def get_keys(self):
        if self.not_dic():
            return list(self.d.keys())

    def get_values(self):
        if self.not_dic():
            return list(self.d.values())

    def not_dic(self):
        if type(self.d) != dict:
            raise Exception(f'{self.d} is not a dictionary')
        return True

    def user_input(self):
        while True:
            keys = input("Enter a dictionary key: ")
            value = input("Enter a dictionary value: ")
            self.d[keys] = value
            if keys == "-1" or value == "-1":
                break
        return self.d

    def insertion(self, k, v):
        """This method takes a key and value pair and insert in the ready_made dictionary"""
        self.d[k] = v
        return self.d



