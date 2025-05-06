from pathlib import Path
import os
import subprocess
 

def create_pyproject_toml_file(library_name):
    library_dir = Path.cwd() / library_name
    toml_file = library_dir / "pyproject.toml"

    project_toml = '''[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
'''

    try:
        with open(toml_file, 'w', encoding='utf-8') as f:  # 'w' overwrites; use 'a' to append
            f.write(project_toml)
        print(f"✅ pyproject.toml created at: {toml_file}")
        return toml_file
    except Exception as e:
        print(f"❌ Failed to create pyproject.toml: {e}")
        return None

def create_project_directory(library_name):
    """
    Creates a project directory and returns status.
    Returns:
        True if created or already exists, False if failed.
    """
    try:
        library_dir = Path.cwd() / library_name
        library_dir.mkdir(exist_ok=True)
        print(f"✅ Successfully created or found existing directory: {library_dir}")
        return True
    except Exception as e:
        print(f"❌ Failed to create directory '{library_name}': {e}")
        return False

def copy_library_to_project_directory(library_name):
    """
    Moves the <library_name>.py file into the corresponding project directory.
    Returns:
        True if moved successfully, False otherwise.
    """
    try:
        current_dir = Path.cwd()
        source_module_path = current_dir / f"{library_name}.py"
        project_dir = current_dir / library_name
        target_module_path = project_dir / f"{library_name}.py"

        if not source_module_path.exists():
            print(f"⚠️ WARNING: {source_module_path} not found.")
            return False

        project_dir.mkdir(exist_ok=True)
        shutil.move(str(source_module_path), str(target_module_path))
        print(f"✅ Moved {library_name}.py to {project_dir}")
        return True

    except Exception as e:
        print(f"❌ Failed to move {library_name}.py: {e}")
        return False


from pathlib import Path

def create_setup_py_file(
    library_name,
    modules,
    library_description,
    version_number='0.1.0',
    author_name='Joe Eberle',
    author_email='josepheberle@outlook.com'
):
    """
    Generates a setup.py file for packaging a single-file Python module.
    """
    try:
        library_dir = Path.cwd() / library_name
        setup_path = library_dir / "setup.py"

        setup_contents = f"""from setuptools import setup

setup(
    name="{library_name}",
    version="{version_number}",
    py_modules={modules},
    author="{author_name}",
    author_email="{author_email}",
    description="{library_description}",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JoeEberle/{library_name}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
"""

        with open(setup_path, 'w', encoding='utf-8') as f:
            f.write(setup_contents)

        print(f"✅ setup.py created at: {setup_path}")
        return setup_path

    except Exception as e:
        print(f"❌ Failed to create setup.py: {e}")
        return None

def publish_to_pypi_generic(
    library_name,
    library_description,
    library_version,
    library_dependencies=None,
    author_name='Your Name',
    author_email='you@example.com',
    github_url='https://github.com/your_username/your_repo'
):
    """
    Package and publish a single-file Python library to PyPI.
    Assumes the file library_name.py exists in the current directory.
    """
    print(f"📦 Packaging library: {library_name}")

    # Install build tools
    subprocess.run(["pip", "install", "--upgrade", "build"], check=True)
    subprocess.run(["python", "-m", "build"], cwd=library_dir, check=True)

    # Upload to PyPI
    subprocess.run(["pip", "install", "--upgrade", "twine"], check=True)
    print("📤 Uploading to PyPI — you will be prompted for credentials.")
    subprocess.run(["twine", "upload", "dist/*"], cwd=library_dir, check=True)

    print(f"✅ Library '{library_name}' version {library_version} published to PyPI.")

