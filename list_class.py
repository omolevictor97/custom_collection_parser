import logging

logging.basicConfig(filename="list_logger.log", level=logging.DEBUG,
                            format="%(asctime)s %(levelname)s %(message)s")

class ListParser:

    def __init__(self, lists):
        """List Parser initializer, the methods are list based methods"""
        logging.info("Initializer is starting")
        self.a = lists

    def not_list(self):
        """This checks if the passed argument is a list"""
        try:
            if type(self.a) == list:
                logging.info("This is a list collection")
                return 1
            else:
                logging.error("This is not a list collection")
                return 0
        except Exception as e:
            logging.exception(e)

    def reverser(self):
        """This method reverses the given list"""
        try:
            if self.not_list():
                logging.info(f"The list passed is {self.a} and the reversed is {self.a[::-1]} ")
                return self.a[::-1]
        except Exception as e:
            logging.exception("The program could not run because " + str(e))

    def clearer(self):
        """This method clears your list"""
        try:
            if self.not_list():
                x = self.a * 0
                logging.info("You had {} and now after being cleared you have {}".format(self.a, x))
                return x
        except Exception as e:
            logging.exception("The program could not run because " + str(e))

    def appender(self, b):
        """This method appends b to the passed list argument in List_Parser where
        b: is either a string, integer of float
        b cannot be a collection type like dictionary, another list, tuple or set"""
        try:
            if self.not_list():
                if type(b) == str or type(b) == int or type(b) == float:
                    self.a += [None]
                    self.a[len(self.a) - 1] = b
                    logging.info(f"You have appended {b} to the list to give {self.a}")
                    return self.a
                else:
                    logging.info("You can not append any other data type than str, int, or float")
        except Exception as e:
            logging.exception("The problem is " + str(e))

    def insertion(self, *args):
        """This method will accept an index and element add the element to the index"""
        try:
            logging.info("Your insertion method is starting")
            if type(args[0]) != int and len(args) > 1:
                logging.error("Index must be integer")
            elif type(args[0]) == int and len(args) == 2:
                self.a[args[0]] = args[1]
                logging.info(f"Your list has been updated with {args[1]}, so you have {self.a}")
                return self.a
            elif len(args) > 2:
                logging.info("Arguments passed can not be greater than 2")
                return False
            else:
                pass
        except TypeError as t:
            logging.exception(t)

    def counter(self, value):
        """This method takes exactly one parameter and counts the occurrences """
        try:
            total = 0
            for i in self.a:
                if value == i:
                    total += 1
            logging.info(f"Total number of occurrence of {value} is {total}")
        except Exception as e:
            logging.info(e)

    def indexer(self, value):
        """The method takes a value and returns the index of the first occurrence"""
        try:
            for i, item in enumerate(self.a):
                if item == value:
                    logging.info(f"{value} has index of {i} ")
            return -1
        except Exception as e:
            logging.info(e)

    def extend(self, c):
        try:
            if self.not_list():
                if isinstance(c, list):
                    x = self.a + c
                    logging.info(f"{x}")
                elif isinstance(c, tuple):
                    for i in c:
                        y = self.appender(i)
                    logging.info(f"{y}")
                elif isinstance(c, set):
                    for i in c:
                        z = self.appender(i)
                    logging.info(f"{z}")
                else:
                    pass
        except TypeError as t:
            logging.info(t)







