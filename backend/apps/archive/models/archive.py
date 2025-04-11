from django.db import models
from uuid import uuid4
from apps.users.models.users import User
from apps.core.models.core import Tags

class Archive(models.Model):
	title = models.CharField(max_length=500, null=True)
	content = models.TextField(default=None, null=True)
	user = models.ForeignKey(User, to_field="id", on_delete=models.DO_NOTHING, null=True)
	description = models.TextField(default=None, null=True)
	create_datetime = models.DateTimeField(auto_now=True)
	delete_datetime = models.DateTimeField(null=True, blank=True)

	class Meta:
		db_table = 'archive'

class ArchiveAttachments(models.Model):
	archive = models.ForeignKey(Archive, to_field="id", on_delete=models.DO_NOTHING, null=True, related_name="archives_attachs")
	uuid = models.UUIDField(default=uuid4, unique=True)
	origin_file_name = models.TextField(default=None, null=True)
	file_path = models.TextField(default=None, null=True)
	tag = models.ForeignKey(Tags, to_field="id", on_delete=models.DO_NOTHING, null=True, related_name="archives_tags")
	create_datetime = models.DateTimeField(auto_now=True)
	delete_datetime = models.DateTimeField(null=True, blank=True)

	class Meta:
		db_table = 'archive_attachments'