from django.db import models
from uuid import uuid4
from apps.users.models.users import User
from apps.core.models.core import Tags

class Report(models.Model):
	title = models.CharField(max_length=500, null=True)
	content = models.TextField(default=None, null=True)
	user = models.ForeignKey(User, to_field="id", on_delete=models.DO_NOTHING, null=True)
	description = models.TextField(default=None, null=True)
	report_datetime = models.DateTimeField(default=None, null=True, blank=True)
	create_datetime = models.DateTimeField(auto_now=True)
	delete_datetime = models.DateTimeField(null=True, blank=True)

	class Meta:
		db_table = 'report'
 
class ReportComments(models.Model):
	user = models.ForeignKey(User, to_field="id", on_delete=models.DO_NOTHING, null=True)
	report = models.ForeignKey(Report, to_field="id", on_delete=models.DO_NOTHING, null=True)
	parent = models.ForeignKey("self", to_field="id", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="replies")
	content = models.TextField(default=None, null=True)
	create_datetime = models.DateTimeField(auto_now=True)
	delete_datetime = models.DateTimeField(null=True, blank=True)

	class Meta:
		db_table = 'report_comments'

class ReportSigns(models.Model):
	user = models.ForeignKey(User, to_field="id", on_delete=models.DO_NOTHING, null=True, related_name="reports_users")
	report = models.ForeignKey(Report, to_field="id", on_delete=models.DO_NOTHING, null=True, related_name="reports_signs")
	is_sign	= models.BooleanField(default=False)
	is_reject = models.BooleanField(default=False)
	create_datetime = models.DateTimeField(auto_now=True)
	delete_datetime = models.DateTimeField(null=True, blank=True)

	class Meta:
		db_table = 'report_signs'

class ReportAttachments(models.Model):
	report = models.ForeignKey(Report, to_field="id", on_delete=models.DO_NOTHING, null=True, related_name="reports_attachs")
	uuid = models.UUIDField(default=uuid4, unique=True)
	origin_file_name = models.TextField(default=None, null=True)
	file_path = models.TextField(default=None, null=True)
	tag = models.ForeignKey(Tags, to_field="id", on_delete=models.DO_NOTHING, null=True, related_name="reports_tags")
	create_datetime = models.DateTimeField(auto_now=True)
	delete_datetime = models.DateTimeField(null=True, blank=True)

	class Meta:
		db_table = 'report_attachments'

