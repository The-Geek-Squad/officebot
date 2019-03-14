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
        self.value = 0

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
        response = self.database.query("SELECT quote FROM quotes")
        val = random.randint(0, len(response)-1)
        if val == self.value:
            if val == 0:
                self.value += 1
            elif val >= len(response) - 1:
                self.value -= 1
        else:
            self.value = val
        return response[self.value]['quote']

    @staticmethod
    def twss():
        return "That's what she said!"
