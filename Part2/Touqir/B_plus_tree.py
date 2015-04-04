

#For the sequential files, I am using a list of tuples
#I may also have to use a list of keys only for binary search

class B_plus_tree:


	def __init__(self,db_address,branching_factor):

		self.root=self.create()


	def create(self):

		return []



	def insert(self,records):

	current_bucket=[]

		if no_roots() :

			for record in records:
				
				if len(current_bucket) < (self.branching_factor-1)
					
					[position,found]=binary_search() #Add the parameters

					current_bucket = current_bucket[0:position] + [record] + current_bucket[position:]

				else :

					#Case when the bucket gets full and splitting needs to be done

		
		return

	

	def delete(self):

		return

	def search(self, keys):

		records=[]

		return records


	#Returns true if there is only one bucket(eg no roots)
	def no_roots(self):


	def binary_search(self,key_list,key,low=0,high=len(key_list)):

		found=False #Flag which tells if key is found or not
		position = bisect_left(key_list,key,low,high)
		
		if key_list[position]==key:
			found=True

		return [position,found]