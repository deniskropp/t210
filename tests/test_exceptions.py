import pytest
from src.klipper_sdk.exceptions.base import (
    KlipperSDKError,
    ConnectionError,
    DataFormatError,
    AuthorizationError,
    NotFoundError
)

def test_exception_hierarchy():
    assert issubclass(ConnectionError, KlipperSDKError)
    assert issubclass(DataFormatError, KlipperSDKError)
    assert issubclass(AuthorizationError, KlipperSDKError)
    assert issubclass(NotFoundError, KlipperSDKError)
    assert issubclass(KlipperSDKError, Exception)

def test_exception_usage():
    with pytest.raises(KlipperSDKError):
        raise ConnectionError("Connection failed")
    
    with pytest.raises(NotFoundError):
        raise NotFoundError("Item not found")

    try:
        raise DataFormatError("Invalid format")
    except KlipperSDKError as e:
        assert str(e) == "Invalid format"
