"""
Authentication providers for the Pingera API client.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class AuthProvider(ABC):
    """Abstract base class for authentication providers."""
    
    @abstractmethod
    def get_headers(self) -> Dict[str, str]:
        """Return authentication headers."""
        pass


class BearerTokenAuth(AuthProvider):
    """Authentication using Bearer token (JWT)."""
    
    def __init__(self, token: str):
        """
        Initialize Bearer token authentication.
        
        Args:
            token: JWT token for authentication
        """
        if not token:
            raise ValueError("Bearer token cannot be empty")
        self.token = token
    
    def get_headers(self) -> Dict[str, str]:
        """Return Bearer authentication headers."""
        return {"Authorization": f"Bearer {self.token}"}


class APIKeyAuth(AuthProvider):
    """Authentication using API key."""
    
    def __init__(self, api_key: str):
        """
        Initialize API key authentication.
        
        Args:
            api_key: API key for authentication
        """
        if not api_key:
            raise ValueError("API key cannot be empty")
        self.api_key = api_key
    
    def get_headers(self) -> Dict[str, str]:
        """Return API key authentication headers."""
        return {"Authorization": self.api_key}