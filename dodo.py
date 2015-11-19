from py.path import local
from doit.action import CmdAction
from doit.tools import LongRunning

DOIT_CONFIG = {
    "default_tasks": [],
}

MKDOCS = local.sysfind("mkdocs")
assert MKDOCS.exists()


def task_build():
    return {
        "actions": [
            CmdAction(["mkdocs", "build", "-d", "../build"],
                      shell=False,
                      cwd="websrc")
        ],
        "verbosity": 2,
    }


def task_serve():
    return {
        "actions": [
            LongRunning(["mkdocs", "serve"], shell=False, cwd="websrc")
        ],
        "verbosity": 2,
    }
