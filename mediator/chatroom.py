class User:

    def __init__(self, name):
        self.name = name
        self.room = None
        self.chat_log = []

    def receive(self, sender, message):
        envelope = f'{sender.name} to {self.name}: {message}'
        self.chat_log.append(envelope)
        print(envelope)
        return True

    def say(self, message):
        if self.room:
            return self.room.broadcast(self, message)
        return False

    def private_message(self, receiver, message):
        """This method utilises the `direct_message` method of the `ChatRoom` class.

        :param receiver: receiver user obj
        :type receiver: User
        :param message: message text body
        :type message: str
        :return: success or fail
        :rtype: bool
        """
        if self.room:
            return self.room.direct_message(self, receiver, message)
        return False

    def __repr__(self):
        return f'User(name={self.name})'


class ChatRoom:
    """
    A mediator class that handles interactions amongst User instances.
    """

    def __init__(self):
        self.users = []

    def join(self, user):
        join_msg = f'{user.name} joins the chat.'
        self.broadcast(type('RoomUser', (), {'name': 'room'})(), join_msg)
        user.room = self
        self.users.append(user)

    def broadcast(self, sender, message):
        for i in self.users:
            # assuming usernames are unique
            if i.name != sender.name:
                i.receive(sender, message)

    def direct_message(self, sender, receiver, message):
        """A mediator that handles direct messages b/w any two users in the chat room.

        :param sender: sender user obj
        :type sender: User
        :param receiver: receiver user obj
        :type receiver: User
        :param message: message text body
        :type message: str
        :return: success or fail
        :rtype: bool
        """
        for i in self.users:
            if i.name == receiver.name:
                return i.receive(sender, message)
        return False


if __name__ == "__main__":
    room = ChatRoom()

    abe = User('Abe')
    alice = User('Alice')
    alex = User('Alex')
    aaron = User('Aaron')

    room.join(abe)
    room.join(alice)
    room.join(alex)

    abe.private_message(alice, 'Hello Alice.')
    alex.say('Hi everyone!')
    alice.say('Hi Abe and Alex.')

    room.join(aaron)
