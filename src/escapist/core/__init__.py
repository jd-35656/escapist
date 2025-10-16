# SPDX-FileCopyrightText: 2025-present Jitesh Sahani (JD) <jitesh.sahani@outlook.com>
#
# SPDX-License-Identifier: MIT


class Escapist:
    """
    Core class for the Escapist application.
    Handles core logic and serves as the main interface for higher-level features.
    """

    def __init__(self, name: str = "Escapist") -> None:
        self.name = name

    def run(self) -> str:
        """Run the main process."""
        return f"{self.name} is running!"

    def info(self) -> str:
        """Return basic information about the application."""
        return f"{self.name} — a lightweight CLI scaffolding tool."
