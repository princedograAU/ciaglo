from typing import Any

from django.core.management import BaseCommand
from django.core.management.base import CommandParser


class Command(BaseCommand):
    help = "Install all fixtures from the fixtureset directory"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--dry_run",
            default=False,
            type=bool,
            help="Rollback entire transaction without committing for testing fixtures",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        return super().handle(*args, **options)
