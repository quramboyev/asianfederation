import os

import environ
from django.core.exceptions import ImproperlyConfigured

env = environ.Env(DEBUG=(bool, False))

current_path = environ.Path(__file__) - 1
site_root = current_path - 2
env_file = site_root(".env")

print(env_file)

if os.path.exists(env_file):  # pragma: no cover
    environ.Env.read_env(env_file=env_file)


def env_to_enum(enum_cls, value):
    for x in enum_cls:
        if x.value == value:
            return x

    raise ImproperlyConfigured(
        f"Env value {repr(value)} could not be found in {repr(enum_cls)}"
    )