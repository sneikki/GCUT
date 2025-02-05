from typing import Literal
from pathlib import Path
import subprocess
import shutil
from lib.project import create_project_directory, copy_file

PRODUCTION_DEPENDENCIES = [
    "typescript",
    "@google-cloud/functions-framework"
]


def create_main_file(project_directory_path: Path) -> Path:
    src_path = Path(project_directory_path, "src")
    src_path.mkdir()

    main_file_path = Path(src_path, "index.ts")
    main_file_path.touch()

    return main_file_path


def create_package_json(function_name: str):
    package_json_path = Path(function_name, "package.json")
    with open(package_json_path, "w") as package_json_file:
        package_json_file.write(
            f"""{{
    "name": "{function_name}",
    "version": "0.0.1",
    "main": "index.js",
    "private": true,
    "scripts": {{
        "build": "tsc",
        "gcp-build": "npm run build"
    }}
}}""")


def install_packages(function_name: str, package_names: [str], dev=False):
    subprocess.run([
        "npm", "install",
        ("--save-dev" if dev else "--save"),
        *package_names],
        cwd=Path(function_name),
        capture_output=True)


def create_src(function_name: str, function_trigger: Literal["http"]):
    src_path = Path(function_name, "src")
    src_path.mkdir()

    file_path = Path(Path(__file__).parent,
                     "ts", f"index.{function_trigger}.ts")
    shutil.copy(file_path, Path(src_path, "index.ts"))


def create_ts_project(function_name: str, function_type: Literal["ts"],
                      function_trigger: Literal["http"]):
    create_project_directory(function_name)
    copy_file(function_name, function_type, "tsconfig.json")
    copy_file(function_name, function_type, ".gcloudignore")
    create_package_json(function_name)
    create_src(function_name, function_trigger)
    install_packages(function_name, PRODUCTION_DEPENDENCIES)
