"""
Pingera Python SDK

A comprehensive Python SDK for the Pingera monitoring platform API.
Built on top of the OpenAPI-generated client with enhanced Pythonic interfaces.
"""

from .client import PingeraClient
from .auth import AuthProvider, BearerTokenAuth, APIKeyAuth

__version__ = "1.0.0"
__all__ = [
    "PingeraClient",
    "AuthProvider", 
    "BearerTokenAuth",
    "APIKeyAuth"
]