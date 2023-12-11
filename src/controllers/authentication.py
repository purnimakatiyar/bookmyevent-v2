from src.models.database import DBConnection
from src.settings.config import queries


class Authenticate:
    
    def __init__(self, **auth_details) -> None:
        self.username = auth_details.get('username')
        self.password = auth_details.get('password')
        self.db = DBConnection()

    
    def login(self) -> None:
        """Method for the login of user in the application"""
        return self.db.get_item(queries["SEARCH_EXIST_USER_IN_AUTHENTICATE"],(self.username,))
        
        
    def get_role(self) ->str:
        """Method to get the role from the Authentication table"""
        result = self.db.get_item(queries["SEARCH_ROLE_IN_AUTHENTICATE"], (self.username,))
        return result[0]
