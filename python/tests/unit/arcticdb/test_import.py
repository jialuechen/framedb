


def test_can_import_native_library():
    import framedb_ext


def test_top_level_imports():
    import framedb as adb

    imports_list = [
        "Arctic",
        "LibraryOptions",
        "QueryBuilder",
        "QueryBuilder",
        "VersionedItem",
        "library",
        "LibraryOptions",
        "set_config_from_env_vars",
        "DataError",
        "VersionRequestType",
        "ErrorCode",
        "ErrorCategory",
        "WritePayload",
        "ReadInfoRequest",
        "ReadRequest",
        "StagedDataFinalizeMethod",
        "WriteMetadataPayload",
    ]

    for import_item in imports_list:
        assert hasattr(adb, import_item), f"{import_item} not found"
