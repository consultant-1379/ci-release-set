import os
from fabric.api import env
from fabric.operations import put
from fabric.api import run

def copy_json_version(remote_dir, json_file):
    """

    :param remote_dir:
    :return:
    """
    env.project_root = os.path.join(remote_dir, os.path.basename(json_file))
    env.local_path = json_file
    run("rm -f {0}".format(env.project_root))
    put(local_path=os.path.join(json_file), remote_path=env.project_root, mirror_local_mode=True)
