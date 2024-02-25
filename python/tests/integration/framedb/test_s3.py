

import pytest
import pandas as pd

from framedb import Arctic
from framedb_ext.exceptions import StorageException


def test_s3_storage_failures(mock_s3_store_with_error_simulation):
    lib = mock_s3_store_with_error_simulation
    symbol_fail_write = "symbol#Failure_Put_99_0"
    symbol_fail_read = "symbol#Failure_Get_17_0"
    df = pd.DataFrame({"a": list(range(100))}, index=list(range(100)))

    with pytest.raises(StorageException, match="Unexpected network error: S3Error#99"):
        lib.write(symbol_fail_write, df)

    lib.write(symbol_fail_read, df)
    with pytest.raises(StorageException, match="Unexpected error: S3Error#17"):
        lib.read(symbol_fail_read)
