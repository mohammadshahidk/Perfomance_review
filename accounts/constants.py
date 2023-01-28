"""Constants Used in Accounts App."""

import enum


class ChoiceAdapter(enum.IntEnum):
    """Class for creating choices"""
    @classmethod
    def choice(cls):
        return ((item.value, item.name.replace("_", " ")) for item in cls)


class UserRole(ChoiceAdapter):
    """ User role"""
    Admin = 1
    Employee = 2
