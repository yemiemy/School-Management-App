import string
import random

from .models import Course
def id_generator(size=5, chars=string.digits):
	the_id =  "".join(random.choice(chars) for x in range(size))
	try:
		course = Course.objects.get(course_code=the_id)
		id_generator()
	except Course.DoesNotExist:
		return the_id