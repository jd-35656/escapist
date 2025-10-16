import pytest
from click.testing import CliRunner

from escapist.cli import escapist


@pytest.fixture
def runner():
    """Fixture for Click CLI runner."""
    return CliRunner()


def test_cli_invokes_main(runner):
    """Test that running the CLI prints the expected message."""
    result = runner.invoke(escapist)
    assert result.exit_code == 0
    assert "running" in result.output.lower()


def test_cli_help_option(runner):
    """Test that --help shows usage."""
    result = runner.invoke(escapist, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.output


def test_cli_version_option(runner):
    """Test that --version shows the version."""
    result = runner.invoke(escapist, ["--version"])
    assert result.exit_code == 0
    assert "escapist" in result.output.lower()
