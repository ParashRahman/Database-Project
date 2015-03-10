from abc import ABCMeta, abstractmethod

# extend this class for your respective class
class Application(object):
    __metaclass__ = ABCMeta

    # List the TUI of the application
    @abstractmethod
    def list_options(self):
        pass

    # Called within the list_options method 
    # May end up repetitive amongst classes
    # Must have error checking
    @abstractmethod
    def get_option(self):
        pass
        
