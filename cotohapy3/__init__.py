"""
Cotoha API library
"""
__version__ = '3.6.9'

from .capi import CotohaAPI
from .utils import CotohaError, Response
from .parse import Parse

__all__ = ("CotohaAPI", "CotohaError", "Response", "Parse")
