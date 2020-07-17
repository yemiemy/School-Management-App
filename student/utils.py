import string
import random

from .models import Student
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
	the_id =  "".join(random.choice(chars) for x in range(size))
	try:
		student = Student.objects.get(admission_id=the_id)
		id_generator()
	except Student.DoesNotExist:
		return the_id