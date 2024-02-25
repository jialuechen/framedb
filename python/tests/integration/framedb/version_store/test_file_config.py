
from framedb.config import Defaults
from framedb.version_store.helper import add_lmdb_library_to_env, save_envs_config, get_frame_native_lib
from framecc.pb2.storage_pb2 import EnvironmentConfigsMap


def _make_temp_lmdb_lib(tmp_path, library_name):
    cfg_filename = "{}/{}".format(tmp_path, "test_cfg")
    cfg = EnvironmentConfigsMap()
    add_lmdb_library_to_env(
        cfg, lib_name=library_name, env_name=Defaults.ENV, description="a test library", db_dir=str(tmp_path)
    )
    save_envs_config(cfg, conf_path=cfg_filename)
    return "{}@{}".format(library_name, cfg_filename)


def test_native_lmdb_library(tmp_path):
    lib = get_frame_native_lib(_make_temp_lmdb_lib(tmp_path, "test.file_config"))
    lib.write("symbol", "thing")
    assert lib.read("symbol").data == "thing"
