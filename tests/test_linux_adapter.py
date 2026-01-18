import pytest
import asyncio
from unittest.mock import AsyncMock, patch, MagicMock
from src.core.adapters.linux import LinuxClipboardAdapter
from src.core.domain.models import Content

@pytest.fixture
def mock_shutil_which():
    with patch("shutil.which") as mock:
        yield mock

@pytest.fixture
def mock_subprocess():
    with patch("asyncio.create_subprocess_exec") as mock:
        process_mock = AsyncMock()
        process_mock.communicate.return_value = (b"mock_output", b"")
        process_mock.returncode = 0
        mock.return_value = process_mock
        yield mock

@pytest.mark.asyncio
async def test_init_wl_clipboard(mock_shutil_which):
    # Simulate wl-clipboard existing
    def side_effect(cmd):
        return "/usr/bin/" + cmd if cmd in ["wl-copy", "wl-paste"] else None
    mock_shutil_which.side_effect = side_effect
    
    adapter = LinuxClipboardAdapter()
    # Check private attribute to verify tool detection
    assert adapter._tool == "wl-clipboard"

@pytest.mark.asyncio
async def test_init_no_tool(mock_shutil_which):
    mock_shutil_which.return_value = None
    with pytest.raises(ImportError):
        LinuxClipboardAdapter()

@pytest.mark.asyncio
async def test_read_success(mock_shutil_which, mock_subprocess):
    # Setup wl-clipboard
    mock_shutil_which.side_effect = lambda cmd: "/usr/bin/" + cmd if "wl" in cmd else None
    
    adapter = LinuxClipboardAdapter()
    
    # Configure subprocess mock for read
    process = mock_subprocess.return_value
    process.communicate.return_value = (b"Hello World", b"")
    
    result = await adapter.read()
    
    assert result is not None
    assert result.data == "Hello World"
    assert result.metadata.source_app == "wl-clipboard"
    mock_subprocess.assert_called()

@pytest.mark.asyncio
async def test_write_success(mock_shutil_which, mock_subprocess):
    mock_shutil_which.side_effect = lambda cmd: "/usr/bin/" + cmd if "wl" in cmd else None
    
    adapter = LinuxClipboardAdapter()
    content = Content.from_text("Test Write")
    
    await adapter.write(content)
    
    # Verify command called
    args, kwargs = mock_subprocess.call_args
    assert "wl-copy" in args
