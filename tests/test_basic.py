import pytest

def test_infrastructure():
    """Проверка, что среда тестирования настроена корректно."""
    assert True

def test_mcp_import():
    """Проверка наличия установленного SDK."""
    try:
        import mcp
        assert True
    except ImportError:
        pytest.fail("MCP SDK не установлен в окружении")
