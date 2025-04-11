from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
	def create_user(self, username, password=None):
		if not username: 
			raise ValueError('Users must have an username')

		user = self.model(username = username)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password=None):
		"""
		Creates and saves a superuser with the given username, date of
		birth and password.
		"""
		user = self.create_user(username, password=password)
		user.is_admin = 1
		user.save(using=self._db)
		return user

class Auth(models.Model):
	name = models.CharField(max_length=500, null=True)
	type = models.IntegerField(default=0)
	rank = models.IntegerField(default=None, null=True)
	description = models.TextField(default=None, null=True)
	create_datetime = models.DateTimeField(auto_now=True)
	delete_datetime = models.DateTimeField(default=None, null=True)
 
	class Meta:
		db_table = 'auth'

class User(AbstractBaseUser):
	username = models.CharField(max_length=500, unique=True) #아이디
	name = models.CharField(max_length=500, null=False, blank=False)  # 사용자 이름
	phone = models.CharField(max_length=25, null=True, blank=True)  # 전화번호
	email = models.EmailField(unique=True, null=False, blank=False)  # 이메일
	create_datetime = models.DateTimeField(auto_now=True)
	update_datetime = models.DateTimeField(auto_now = True)
	delete_datetime = models.DateTimeField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False) #관리자 권한
	last_login = models.DateTimeField(null=True, blank=True)  # 마지막 로그인 시간

	auth = models.ForeignKey(Auth, to_field="id", on_delete=models.DO_NOTHING, null=True) # web 기능적으로는 반드시 들어감.
 
	objects = MyUserManager()
	USERNAME_FIELD = 'username'

	class Meta:
		db_table = 'user'

