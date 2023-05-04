import os
from pathlib import Path


class FileOperations:
    staticmethod

    def get_root_directory_path(self, file_in_root_dir_full_path) -> Path:
        file_path_parent = os.path.dirname(os.path.abspath(file_in_root_dir_full_path))
        tests_directory_path = Path(file_path_parent)
        project_root_path = tests_directory_path.parent.absolute()
        return project_root_path
