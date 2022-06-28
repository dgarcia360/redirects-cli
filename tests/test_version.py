from typer.testing import CliRunner

from src.redirects_cli import cli

runner = CliRunner()


def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
