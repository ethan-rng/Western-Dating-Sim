# Exceptions

# User Issues Exceptions
class UserNotFound(Exception):
    """An Exception Class raised when a user tries to log in with a username that does not exist."""
    def __init__(self, username:str): 
         super().__init__(f"{username} is not an available user to log into")

class DuplicateUser(Exception):
    """An Exception Class raised when a user makes an account with an already existing username."""
    def __init__(self, username:str): 
        super().__init__(f"{username} is already taken")

class IncorrectPassword(Exception):
    """An Exception Class raised when incorrect password is used."""
    def __init__(self, username:str, password:str): 
        super().__init__(f"{username} with {password} password is incorrect")


# Admin Level Account Exceptions
class AdminLevelAccount(Exception):
    """An Exception Class raised when trying to make a user account with the username developer or instructor account."""
    def __init__(self): 
        super().__init__(f"Cannot make an admin level account")

class IncorrectPrivilege(Exception):
    """An Exception Class raised when trying to access methods without the right privilege level."""
    def __init__(self): 
        super().__init__(f"Cannot access method as a non-admin user (developer/instructor)")