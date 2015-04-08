import bsddb

# BTree (Subclass of DB)

class BTree(DB):
    def __init__(self, db_address):
        # Database="B_tree.db"
        # self.address=db.address #contains address to db file's location

        self.db = bsddb.btopenhashopen(self.address, 'c')           
        super(B_tree, self).__init__(self, self.db, db_address)

        return
