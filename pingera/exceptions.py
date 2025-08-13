"""
Exception classes for the Pingera API client.
"""

from typing import Optional, Dict, Any


class PingeraError(Exception):
    """Base exception for all Pingera API errors."""
    
    def __init__(
        self, 
        message: str, 
        status_code: Optional[int] = None,
        response_data: Optional[Dict[str, Any]] = None
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_data = response_data


class PingeraAuthenticationError(PingeraError):
    """Raised when authentication fails."""
    pass


class PingeraNotFoundError(PingeraError):
    """Raised when a resource is not found (404)."""
    pass


class PingeraValidationError(PingeraError):
    """Raised when request validation fails (400)."""
    
    def __init__(
        self, 
        message: str, 
        errors: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        super().__init__(message, **kwargs)
        self.errors = errors or {}


class PingeraRateLimitError(PingeraError):
    """Raised when rate limit is exceeded (429)."""
    
    def __init__(
        self, 
        message: str, 
        retry_after: Optional[int] = None,
        **kwargs
    ):
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class PingeraNetworkError(PingeraError):
    """Raised when a network error occurs."""
    pass