class KlipperError(Exception):
    """Base exception for all Klipper SDK errors."""
    def __init__(self, message: str, code: str = "KLIPPER_ERROR"):
        self.message = message
        self.code = code
        super().__init__(self.message)

class ConfigurationError(KlipperError):
    """Raised when there is a configuration issue."""
    def __init__(self, message: str):
        super().__init__(message, code="CONFIG_ERROR")

class InfrastructureError(KlipperError):
    """Base for errors related to external infrastructure (Network, FS, etc.)."""
    pass

class NetworkError(InfrastructureError):
    """Raised when network operations fail."""
    def __init__(self, message: str, original_error: Exception | None = None):
        super().__init__(message, code="NETWORK_ERROR")
        self.original_error = original_error

class DomainError(KlipperError):
    """Base for domain capability errors."""
    pass

class ResourceNotFoundError(DomainError):
    """Raised when a requested resource is not found."""
    def __init__(self, resource_type: str, resource_id: str):
        super().__init__(
            f"{resource_type} with ID '{resource_id}' not found.", 
            code="RESOURCE_NOT_FOUND"
        )
