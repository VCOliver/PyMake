# PyMake

PyMake is a Python script designed to streamline the generation of `CMakeLists.txt` files for small projects. It simplifies project setup by providing an easy-to-use command-line interface to configure CMake options for various programming languages and standards.

## Features

- Supports multiple programming languages:
  - C++ (`CXX`)
  - C
  - C#
  - CUDA
  - Objective-C (`OBJC`)
  - Objective-C++ (`OBJCXX`)
- Configurable C++ standards:
  - 98, 3, 11, 14, 17, 20, 23
- Flexible project versioning.
- Options to:
  - Require or not require a specific C++ standard.
  - Enable or disable compiler-specific extensions.
- Automatically sets up source (`src/`) and include (`include/`) directories based on the current working directory.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Ensure you have Python installed (Python 3.11+ recommended).
3. Install dependencies if required:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the desired arguments:

```bash
python pymake.py <project_name> [options]
```

### Arguments

| Argument                     | Description                                                  | Default      |
|------------------------------|--------------------------------------------------------------|--------------|
| `project_name`               | The name of the CMake project.                              | None         |
| `-v`, `--version`            | The version of the project.                                 | None         |
| `-l`, `--languages`          | Languages needed to build the project.                      | `CXX`        |
| `--cxx-standard`             | Specify the C++ standard to use.                            | `17`         |
| `--cxx-standard-not-required`| If specified, the C++ standard will not be required.         | `False`      |
| `--cxx-extensions`           | Whether to use compiler-specific extensions.                | `True`       |

### Example

```bash
python pymake.py MyProject -v 1.0.0 -l CXX CUDA --cxx-standard 20 --cxx-extensions False
```
This generates a `CMakeLists.txt` file for a project named `MyProject` with version `1.0.0`, using C++ and CUDA, targeting the C++20 standard without compiler-specific extensions.

Happy coding with PyMake!

