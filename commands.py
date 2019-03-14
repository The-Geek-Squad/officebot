import database
import random

class Command(object):
    def __init__(self):
        self.commands = {
            "hi": self.hi,
            "quote": self.quote,
            "twss": self.twss
        }
        self._database = database.Database()

    @property
    def database(self):
        return self._database

    def handle_command(self, user, command):
        # response = "<@" + user + ">: "

        if command in self.commands:
            response = self.commands[command]()
        else:
            response = "Dwight you ignorant sl**."

        return response

    @staticmethod
    def hi():
        return "Hello"

    def quote(self):
        # TODO Handle Random quote better
        response = self.database.query("SELECT quote FROM quotes ORDER BY RAND()")
        val = random.randint(0, len(response)-1)
        return response[val]['quote']

    @staticmethod
    def twss():
        return "That's what she said!"
