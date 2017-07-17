class Parent():
	def __init__(self, last_name, eye_color):
		print "Parent Constructor Called..."
		self.last_name = last_name
		self.eye_color = eye_color
	
	def show_info(self):
		print "Your last name is {} with eye color {}.".format(self.last_name, self.eye_color)


class Child(Parent):
	def __init__(self, last_name, eye_color, num_of_toys):
		print "Child Constructor Called..."
		Parent.__init__(self, last_name, eye_color)
		self.num_of_toys = num_of_toys

emily = Parent("Chang", "black")
#emily.show_info()

#print emily.last_name

nate = Child("Sun", "black", 3)
# print nate.last_name
# print nate.num_of_toys
nate.show_info()