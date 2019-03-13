class Command(object):
    def __init__(self):
        self.commands = {
            "hi": self.hi,
            "quote": self.quote,
            "twss": self.twss
        }

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

    @staticmethod
    def quote():
        return "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me."

    @staticmethod
    def twss():
        return "That's what she said!"
