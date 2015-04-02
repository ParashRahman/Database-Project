from abc import ABCMeta, abstractmethod

# extend this class for your respective class
class Application(object):
    __metaclass__ = ABCMeta

    # List the TUI of the application
    @abstractmethod
    def start_application(self):
        pass
