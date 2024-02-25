
from framedb.exceptions import ArcticNativeException


def check(cond, msg, *args, **kwargs):
    if not cond:
        raise ArcticNativeException(msg.format(*args, **kwargs))
