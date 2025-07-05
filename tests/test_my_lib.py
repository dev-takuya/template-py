from unittest.mock import patch

from src.my_pkg.my_lib import hello_world


def test_hello_world() -> None:
    """Test hello_world function prints Hello World."""
    with patch("builtins.print") as mock_print:
        hello_world()
        mock_print.assert_called_once_with("Hello World")
