from application import Application

class AddPerson(Application):
    def start_application(self, c):
        self.cursor = c
        
        self.fields = [ 'SIN',
                        'Name',
                        'Height',
                        'Weight',
                        'Eye Color',
                        'Hair Color',
                        'Address',
                        'Gender',
                        'Birthday' ]
