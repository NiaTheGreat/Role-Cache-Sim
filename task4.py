"""
The goal of this coding activity is to design a system that limits the number of active roles that any given person has. A role gives the user access to some thing, whether it be a piece of data or an internal system. The system achieves this requirement by keeping track of the last k roles that a person has used. If a new role is used, the oldest role is removed if there are already k active roles for that person. Each role has a name and a message which contains details about its use by the person. You only need to store the last message for a role invocation.

Implement the constructor, get, and set methods of RolesCache. Each instance of the RolesCache corresponds to a single person.

Finally, fill out the runtime complexity for get and set and the overall space used. Use Big O notation, i.e. O(1), O(N), etc. For a refresher on Big O notation, please review https://danielmiessler.com/study/big-o-notation/.

"""

class RolesCache:
    def __init__(self, capacity):
        self.capacity = capacity  # How many toys our box can hold
        self.cache = {}  # Our toy box
        self.order = []  # The order we played with our toys

    def get(self, role):
        if role in self.cache:
            # Move the toy to the top of our "recently played with" list
            self.order.remove(role)
            self.order.append(role)
            return self.cache[role]
        return None

    def set(self, role, message):
        if role in self.cache:
            # If we already have this toy, just update its note
            self.cache[role] = message
            # And move it to the top of our "recently played with" list
            self.order.remove(role)
            self.order.append(role)
        else:
            # If our toy box is full, remove the oldest toy
            if len(self.cache) >= self.capacity:
                oldest = self.order.pop(0)
                del self.cache[oldest]
            # Add the new toy
            self.cache[role] = message
            self.order.append(role)

    def _complexity(self):
        return {
            'get': 'O(1)',
            'set': 'O(1)',
            'space': 'O(k)'
        }