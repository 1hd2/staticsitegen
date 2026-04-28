import os
import shutil        

def clear_dir(dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

def copy_dir(src, dst):
    src_subdirs = os.listdir(src)
    for subdir in src_subdirs:
        src_subdir_path = os.path.join(src, subdir)
        dst_subdir_path = os.path.join(dst, subdir)
        if os.path.isfile(src_subdir_path):
            shutil.copy(src_subdir_path, dst_subdir_path)
        else:            
            os.mkdir(dst_subdir_path)
            copy_dir(src_subdir_path, dst_subdir_path)

def src_to_public(src, dst):
    if not os.path.exists(src):
        return f'source directory "{src}" does not exist'

    clear_dir(dst)
    copy_dir(src, dst)