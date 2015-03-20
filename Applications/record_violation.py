from application import Application

class RecordViolation(Application):
    def start_application(self, c):
        self.cursor = c
        
