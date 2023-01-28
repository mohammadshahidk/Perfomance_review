from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts import constants as user_constants


class ProjectUser(AbstractUser):
    """
    Base User model to store user details.

    """
    email = models.CharField(default='', max_length=200, blank=True, null=True)
    phone = models.CharField(default='', max_length=200, blank=True, null=True)
    address = models.CharField(
        default='', max_length=2000, blank=True, null=True)
    role = models.IntegerField(
        default=user_constants.UserRole.Admin,
        choices=user_constants.UserRole.choice())

    class Meta:
        """Meta class for above model"""

        verbose_name = ("BaseUser")

    @property
    def name(self):
        """Get user full name"""
        return f'{self.first_name} {self.last_name}'


class Admin(ProjectUser):
    """
    Model to store admin details
    """
    designation = models.CharField(
        default='', max_length=200, blank=True, null=True)

    def __str__(self):
        """Object name in Django Admin"""
        return f'{self.id} {self.name}'

    class Meta:
        """Meta class for above model"""

        verbose_name = ("Admin")

    def save(self, *args, **kwargs):
        """Assign role as admin"""
        self.role = user_constants.UserRole.Admin
        return super(Admin, self).save(*args, **kwargs)


class Employee(ProjectUser):
    """
    Model to store Employee details
    """
    emp_id = models.CharField(
        "employee's id", default='', max_length=200, null=True, blank=True)
    designation = models.CharField(
        default='', max_length=200, null=True, blank=True)
    date_of_join = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        """Meta class for above model"""

        verbose_name = ("Employee")

    def __str__(self):
        """
        Object name in Django Admin.
        """
        return f'{self.id} {self.name}'

    def save(self, *args, **kwargs):
        """Assign role as employee."""
        self.role = user_constants.UserRole.Employee
        return super(Employee, self).save(*args, **kwargs)
