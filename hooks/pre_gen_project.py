import re

MODULE_REGEX = r'^[a-z][a-z0-9\-]+[a-z0-9]$'
MODULE_NAME = '{{ cookiecutter.project_name }}'


def validate_project_name():
    """
    This validator is used to ensure that `project_name` is valid.
    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or underscores.
    Valid example: `school_project3`.
    """
    if not re.match(MODULE_REGEX, MODULE_NAME):
        # Validates project's module name:
        message = [
            'ERROR: The project slug {0} is not a valid name.',
            'Start with a lowercase letter.',
            'Followed by any lowercase letters, numbers, or dashes (-).',
        ]
        raise ValueError(' '.join(message).format(MODULE_NAME))
