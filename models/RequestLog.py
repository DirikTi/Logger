from models.ILogAsikus import ILogAsikus
import zope.interface
from db.MySQLAsikus import AsikusMysql

@zope.interface.implementer(ILogAsikus)
class RequestLog():

    WHICH_SYSTEM_ENUM = {
        1, 2, 3
    }
    METHODS_ENUM = {
        'GET', 'POST', 'PUT', 'DELETE', 'HEAD'
    }

    def __init__(self, request_token, request_body, request_query, which_system, base_url, 
        headers, method, response_body, sender_ip_address, user_id, is_error, status):
        self.request_token = request_token
        self.request_body = request_body
        self.request_query = request_query
        self.which_system = which_system
        self.base_url = base_url
        self.headers = headers
        self.method = method
        self.response_body = response_body
        self.sender_ip_address = sender_ip_address
        self.user_id = user_id
        self.is_error = is_error
        self.status = status



    def insert_data(self):
        query = """
        INSERT INTO request_logs
        (request_token, request_body, request_query, which_system, base_url, headers, method, response_body, sender_ip_address, user_id, is_error, status)
        VALUES
        (%s, %s, %s, %d, %s, %s, %s, %s, %s, %s, %s, %d, %d, %d)
        """

        values = (self.request_token, self.request_body, self.request_query, self.which_system, self.base_url, 
            self.headers, self.method, self.response_body, self.sender_ip_address, self.user_id, self.is_error, self.status
        )
        print(values)
        AsikusMysql.insert(query, values)


    def getWhichSystem(self, which_system) -> int:
        if(which_system in self.WHICH_SYSTEM_ENUM):
            return which_system

        raise TypeError("ERROR: WHICH_SYSTEM MODEL IS NOT FIT %d ", which_system)


    def getMethod(self, method) -> str:
        if(method in self.METHODS_ENUM):
            return method

        raise TypeError("ERROR: WHICH_SYSTEM MODEL IS NOT FIT %d ", method)