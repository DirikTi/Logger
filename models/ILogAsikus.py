import zope.interface

class ILogAsikus(zope.interface.Interface):
    def insert_data(self, value) -> bool:
        pass
