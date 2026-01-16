class KlipperSDKError(Exception):
    """Base exception for all Klipper SDK errors."""
    pass

class ConnectionError(KlipperSDKError):
    """Raised when connection to the Klipper daemon fails."""
    pass

class DataFormatError(KlipperSDKError):
    """Raised when data format is invalid or unsupported."""
    pass

class AuthorizationError(KlipperSDKError):
    """Raised when the client is not authorized to perform an action."""
    pass

class NotFoundError(KlipperSDKError):
    """Raised when a requested resource (e.g. history item) is not found."""
    pass
