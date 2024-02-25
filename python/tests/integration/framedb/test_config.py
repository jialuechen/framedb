import sys
import pytest
from subprocess import run, PIPE

from framedb_ext.log import LogLevel

_LEVELS = tuple(LogLevel.__entries)


@pytest.mark.parametrize("level", _LEVELS)
def test_set_log_level(level):
    code = f"""import framedb; import sys
print("Our printout starts", file=sys.stderr, flush=True)
framedb.config.set_log_level('{level}')
framedb.log.version.debug('test DEBUG')
framedb.log.version.info('test INFO')
framedb.log.version.warn('test WARN')
framedb.log.version.error('test ERROR')
"""
    p = run([sys.executable], universal_newlines=True, input=code, stderr=PIPE, timeout=10)
    lines = p.stderr.splitlines()
    idx = _LEVELS.index(level)
    while lines.pop(0) != "Our printout starts":
        pass
    for level in _LEVELS[idx:]:
        assert lines.pop(0).endswith(f"{level[0]} framedb.version | test {level}"), p.stderr
