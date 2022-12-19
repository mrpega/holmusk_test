from importlib.metadata import PackageNotFoundError, version
from .reader import Reader

try:
    __version__ = version('EHRReader')
except PackageNotFoundError:
    __version__ = '(local)'

del PackageNotFoundError
del version

