"""Compatibility re-export for the canonical user model.

The application imports StudentUser from users.py; keep models.py as a simple
bridge so both module names resolve to the same implementation.
"""

from users import StudentUser, User

__all__ = ["User", "StudentUser"]