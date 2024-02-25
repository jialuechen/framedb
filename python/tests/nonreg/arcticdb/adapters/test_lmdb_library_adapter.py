
import tempfile

from framedb import Arctic


def test_creation_deletion_lmdb():
    # Non-regression test for #345

    with tempfile.TemporaryDirectory() as lmdb_temp_dirname:
        # The following instructions must complete without failure.
        store = Arctic(f"lmdb://{lmdb_temp_dirname}")
        assert store.list_libraries() == []
        store.create_library("option.1day")
        assert store.list_libraries() == ["option.1day"]
        store.delete_library("option.1day")
        assert store.list_libraries() == []
        del store
