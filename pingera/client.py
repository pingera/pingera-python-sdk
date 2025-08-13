"""
Pingera API Client

Main client class for interacting with the Pingera monitoring platform API.
Provides a high-level interface with authentication, error handling, and 
convenient methods for common operations. Built on top of the OpenAPI-generated client.
"""

import os
import sys
from typing import Optional, Dict, Any, Union

# Add client directory to path to import generated client
client_path = os.path.join(os.path.dirname(__file__), '..', 'client')
if client_path not in sys.path:
    sys.path.insert(0, client_path)

from pingera_generated import ApiClient, Configuration
from pingera_generated.api import (
    AlertsApi,
    ChecksApi,
    ChecksUnifiedResultsApi,
    HeartbeatsApi,
    OnDemandChecksApi,
    StatusPagesComponentsApi,
    StatusPagesIncidentsApi
)

from .auth import AuthProvider, BearerTokenAuth, APIKeyAuth
from .exceptions import (
    PingeraError, 
    PingeraAuthenticationError,
    PingeraNotFoundError, 
    PingeraValidationError,
    PingeraRateLimitError,
    PingeraNetworkError
)


class PingeraClient:
    """
    Main client for the Pingera API.
    
    Provides high-level access to all Pingera API endpoints with authentication,
    error handling, and convenient Python interfaces.
    """
    
    def __init__(
        self,
        auth: Optional[AuthProvider] = None,
        base_url: str = "https://api.pingera.ru",
        timeout: float = 30.0,
        **kwargs
    ):
        """
        Initialize the Pingera client.
        
        Args:
            auth: Authentication provider. If None, will try to auto-configure from environment.
            base_url: Base URL for the Pingera API
            timeout: Request timeout in seconds
            **kwargs: Additional configuration options
        """
        # Auto-configure authentication if not provided
        if auth is None:
            auth = self._auto_configure_auth()
        
        self.auth = auth
        
        # Configure the generated client
        self.configuration = Configuration(host=base_url)
        
        # Set authentication based on auth provider type
        if isinstance(auth, BearerTokenAuth):
            self.configuration.access_token = auth.token
        elif isinstance(auth, APIKeyAuth):
            self.configuration.api_key['Authorization'] = auth.api_key
        
        # Create API client
        self.api_client = ApiClient(self.configuration)
        
        # Initialize API instances
        self.alerts = AlertsApi(self.api_client)
        self.checks = ChecksApi(self.api_client)
        self.checks_unified_results = ChecksUnifiedResultsApi(self.api_client)
        self.heartbeats = HeartbeatsApi(self.api_client)
        self.on_demand_checks = OnDemandChecksApi(self.api_client)
        self.components = StatusPagesComponentsApi(self.api_client)
        self.incidents = StatusPagesIncidentsApi(self.api_client)
    
    def _auto_configure_auth(self) -> AuthProvider:
        """Auto-configure authentication from environment variables."""
        bearer_token = os.environ.get('PINGERA_BEARER_TOKEN')
        if bearer_token:
            return BearerTokenAuth(bearer_token)
        
        api_key = os.environ.get('PINGERA_API_KEY')
        if api_key:
            return APIKeyAuth(api_key)
        
        raise PingeraAuthenticationError(
            "No authentication credentials found. Set either PINGERA_BEARER_TOKEN "
            "or PINGERA_API_KEY environment variable, or provide credentials directly to the client."
        )
    
    @classmethod
    def from_env(cls) -> 'PingeraClient':
        """Create a client using environment variables for authentication."""
        return cls()
    
    @classmethod
    def from_bearer_token(cls, token: str, **kwargs) -> 'PingeraClient':
        """Create a client using Bearer token authentication."""
        return cls(auth=BearerTokenAuth(token), **kwargs)
    
    @classmethod
    def from_api_key(cls, api_key: str, **kwargs) -> 'PingeraClient':
        """Create a client using API key authentication."""
        return cls(auth=APIKeyAuth(api_key), **kwargs)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self.api_client, 'close'):
            self.api_client.close()