


def test_many_versions(object_version_store):
    for x in range(200):
        object_version_store.write("symbol_{}".format(x), "thing")

    object_version_store.snapshot("test_snap")
