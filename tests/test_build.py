from click.testing import CliRunner
from starter_template.cli import main

def test_build_command():
    runner = CliRunner()
    result = runner.invoke(main, ["build"])
    assert result.exit_code == 0
    assert "Building the application..." in result.output
    assert "Build complete!" in result.output 