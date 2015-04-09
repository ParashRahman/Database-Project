import bsddb
from DB import DB

# BTree (Subclass of DB)

class BTree(DB):

    def __init__(self, db_address):
        # Database="B_tree.db"
        # self.address=db.address #contains address to db file's location

        self.db = bsddb.btopen(db_address, 'c')           
        DB.__init__(self, self.db, db_address)

        return

	def __del__(self):

		self.close()

		return


