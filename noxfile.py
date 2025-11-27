import nox

nox.options.default_venv_backend = "uv"

PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12", "3.13", "3.14", "pypy3.9", "pypy3.10"]


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    session.install(".", "pytest")
    session.run("pytest")
