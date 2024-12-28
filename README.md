# PyMake

PyMake is a Python-based command-line tool designed to simplify the process of generating and managing `CMakeLists.txt` files for small projects. It offers a modular and extensible interface for project creation and building.

## Features

- **Commands**:
  - `create`: Set up a new CMake project with configurable options.
  - `build`: Build the project with optional cleaning of the build directory.
- **Supported Languages**:
  - C++ (`CXX`)
  - C
  - C#
  - CUDA
  - Objective-C (`OBJC`)
  - Objective-C++ (`OBJCXX`)
- **C++ Standards**:
  - 98, 3, 11, 14, 17, 20, 23
- **Flexible Options**:
  - Specify compiler standards, require or skip version enforcement, enable/disable compiler extensions.
  - Automatically create default project directories (`src`, `include`, `build`).
  - Verbose output for detailed step tracking.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Ensure you have Python installed (Python 3.11+ recommended).
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script using the following structure:

```bash
pymake <command> [options]
```

### Commands

#### `create`
Create a new CMake project.

| Argument                     | Description                                                                 | Default       |
|------------------------------|-----------------------------------------------------------------------------|---------------|
| `project_name`               | The name of the project.                                                   | None          |
| `-v`, `--version`            | The version of the project.                                                | None          |
| `-l`, `--languages`          | List of languages required for the project.                                | `CXX`         |
| `--cxx-standard`             | Specify the C++ standard to use.                                           | `17`          |
| `--cxx-standard-not-required`| If specified, the C++ standard will not be enforced.                        | `False`       |
| `--cxx-extensions`           | Whether compiler-specific extensions should be enabled.                    | `True`        |
| `-C`, `--create-dirs`        | Create default directories (`src`, `include`, `build`).                    | `False`       |
| `--verbose`                  | Enable verbose output during project creation.                             | `False`       |

#### Example

```bash
pymake create MyProject -v 1.0.0 -l CXX CUDA --cxx-standard 20 -C --verbose
```

#### `build`
Build the existing project.

| Argument        | Description                                        | Default |
|------------------|----------------------------------------------------|---------|
| `--clean`        | Clean the build directory before building.         | `False` |
| `--verbose`      | Enable verbose output during the build process.    | `False` |

#### Example

```bash
pymake build --clean --verbose
```

---

Happy coding with PyMake!

