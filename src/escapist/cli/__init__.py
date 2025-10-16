# SPDX-FileCopyrightText: 2025-present Jitesh Sahani (JD) <jitesh.sahani@outlook.com>
#
# SPDX-License-Identifier: MIT

import click

from escapist.__version__ import __version__
from escapist.core import Escapist


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="escapist")
def escapist() -> None:
    """Entry point for the Escapist CLI."""
    core = Escapist()
    click.echo(core.run())
