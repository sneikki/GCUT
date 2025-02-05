from typing import Literal
from pathlib import Path
import shutil


def create_project_directory(function_name: str) -> Path:
    project_directory_path = Path(function_name)
    project_directory_path.mkdir()
    return project_directory_path


def copy_file(function_name: str, function_type: Literal["ts"],
              file_name: str):
    file_path = Path(Path(__file__).parent, function_type, file_name)
    shutil.copy2(file_path, Path(function_name))
