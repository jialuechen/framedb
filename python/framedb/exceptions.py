
from framedb_ext.exceptions import *
from framedb_ext.exceptions import ArcticException as ArcticNativeException
from framedb_ext.storage import DuplicateKeyException, NoDataFoundException, PermissionException
from framedb_ext.version_store import NoSuchVersionException, StreamDescriptorMismatch


class ArcticDbNotYetImplemented(ArcticException):
    pass


# Backwards compat - this is the old name of ArcticDbNotYetImplemented
ArcticNativeNotYetImplemented = ArcticDbNotYetImplemented


class LibraryNotFound(ArcticException):
    pass


class MismatchingLibraryOptions(ArcticException):
    pass


class LmdbOptionsError(ArcticException):
    pass
