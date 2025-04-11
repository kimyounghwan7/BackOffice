from django.db import models

class Tags(models.Model):
	name = models.CharField(max_length=500, null=True)
	type = models.IntegerField(null=True, blank=True)
	create_datetime = models.DateTimeField(auto_now=True)
	delete_datetime = models.DateTimeField(default=None, null=True)

	class Meta:
		db_table = 'tags'