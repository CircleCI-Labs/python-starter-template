import pytest
from click.testing import CliRunner
from starter_template.cli import main

def test_hello_command():
    runner = CliRunner()
    result = runner.invoke(main, ["hello"])
    assert result.exit_code == 0
    assert "Hello from the starter template!" in result.output 