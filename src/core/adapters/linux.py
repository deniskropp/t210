import asyncio
import shutil
from typing import List, Optional, Tuple
from src.core.domain.ports import ClipboardPort
from src.core.domain.models import Content, Metadata

class LinuxClipboardAdapter(ClipboardPort):
    """
    Linux implementation using wl-clipboard (Wayland) or xclip/xsel (X11).
    """
    
    def __init__(self) -> None:
        self._tool, self._cmds = self._detect_tool()
        
    def _detect_tool(self) -> Tuple[str, dict]:
        """
        Detects available clipboard tools.
        Returns tuple of (tool_name, command_map).
        """
        if shutil.which("wl-copy") and shutil.which("wl-paste"):
            return "wl-clipboard", {
                "read": ["wl-paste"],
                "write": ["wl-copy"],
                "clear": ["wl-copy", "--clear"]
            }
        elif shutil.which("xclip"):
            return "xclip", {
                "read": ["xclip", "-o", "-selection", "clipboard"],
                "write": ["xclip", "-selection", "clipboard"],
                "clear": ["xclip", "-selection", "clipboard", "/dev/null"] # Not quite right for clear, but effectively writes empty
            }
        elif shutil.which("xsel"):
            return "xsel", {
                "read": ["xsel", "-ob"],
                "write": ["xsel", "-ib"],
                "clear": ["xsel", "-cb"]
            }
        else:
            raise ImportError("No supported clipboard tool found (wl-clipboard, xclip, xsel).")

    async def _run_command(self, cmd_args: List[str], input_data: Optional[str] = None) -> str:
        """
        Runs a shell command asynchronously.
        """
        process = await asyncio.create_subprocess_exec(
            *cmd_args,
            stdin=asyncio.subprocess.PIPE if input_data is not None else None,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await process.communicate(
            input=input_data.encode() if input_data is not None else None
        )
        
        if process.returncode != 0:
            # For xclip/xsel, reading empty clipboard might produce error or empty. 
            # We treat generic errors as just logging or re-raising if critical.
            # For now, simplistic handling.
            pass
            
        return stdout.decode().strip()

    async def read(self) -> Optional[Content]:
        try:
            output = await self._run_command(self._cmds["read"])
            if not output:
                return None
            return Content.from_text(output, source_app=self._tool)
        except Exception:
            return None

    async def write(self, content: Content) -> None:
        await self._run_command(self._cmds["write"], input_data=content.data)

    async def clear(self) -> None:
        # For xclip clear, we might just write empty string if the command mapping is tricky
        if self._tool == "xclip" and "/dev/null" in self._cmds["clear"]:
             # xclip specific hack if needed, or just write empty
             await self._run_command(["xclip", "-selection", "clipboard"], input_data="")
        else:
             await self._run_command(self._cmds["clear"])