import os
import sys


def main():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "frequently_asked_questions.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Not able to import Django "
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
