import pytest
from datetime import datetime, timezone
from rich.table import Table
from rich.panel import Panel

from src.core.domain.models import Content, Metadata
from src.cli.components import HistoryTable, ItemDetail, ErrorPanel

def test_history_table_render():
    item = Content(
        data="test",
        metadata=Metadata(content_type="text/plain")
    )
    table_gen = HistoryTable()
    renderable = table_gen.render([item])
    assert isinstance(renderable, Table)
    assert renderable.title == "Clipboard History"
    assert len(renderable.columns) == 4

def test_item_detail_render():
    item = Content(
        data="test",
        metadata=Metadata(content_type="text/plain")
    )
    detail = ItemDetail(item)
    renderable = detail.render()
    assert isinstance(renderable, Panel)
    # Check if ID is in title
    assert str(item.metadata.id) in str(detail.render().title)

def test_error_panel_render():
    panel = ErrorPanel(title="Test Error", reason="Something went wrong", suggestion="Fix it")
    renderable = panel.render()
    assert isinstance(renderable, Panel)
    assert "Test Error" in str(panel.render().title)
