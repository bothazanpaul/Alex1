# coding=utf-8
"""
Exceptions that the CNP class can raise.
"""


class CNPError(StandardError, object):
    """
    Standard Error for bad things that could happen in CNP class.
    """
    pass


class SexError(CNPError):
    """
    Error raised if 0 is set on the sex field.
    """
    pass


class DateError(CNPError):
    """
    Error raised when there is an error in the date of birth.
    """
    pass


class CountyError(CNPError):
    """
    Error raised when the county code is wrong.
    """
    pass