# Low Frequency / Medium Frequency (LF/MF) Propagation Model, Python Wrapper #

<!-- LFMF-python: README BADGES

- The first badge links to the PropLib Wiki and does not need to be edited
- The second badge automatically displays and links to the most recent PyPI Release.
    - Make sure to update the [pypi-release-badge] and [pypi-release-link] URLs with
      your package name on PyPI (NOT the repository name on GitHub!)
    - This can only be added once there is a published version of the package on PyPI
- The third badge is the Tox GitHub actions status.
    - Update the repository name in [gh-actions-test-badge] and [gh-actions-test-link]
- The fourth badge displays open GitHub Issues
    - Update the repository name in [gh-issues-badge]
    - Update the repository name in [gh-issues-link]
- The fifth badge displays and links the Zenodo DOI
    - Get your repository ID from https://api.github.com/repos/NTIA/{repo}
    - Or, if private, follow: https://stackoverflow.com/a/47223479
    - Populate the repository ID in [doi-link] and [doi-badge]
-->
[![NTIA/ITS PropLib][proplib-badge]][proplib-link]
[![GitHub Issues][gh-issues-badge]][gh-issues-link]
<!--
[![GitHub Release][gh-releases-badge]][gh-releases-link]
[![PyPI Release][pypi-release-badge]][pypi-release-link]
[![GitHub Actions Unit Test Status][gh-actions-test-badge]][gh-actions-test-link]
[![DOI][doi-badge]][doi-link]
-->
[proplib-badge]: https://img.shields.io/badge/PropLib-badge?label=%F0%9F%87%BA%F0%9F%87%B8%20NTIA%2FITS&labelColor=162E51&color=D63E04
[proplib-link]: https://ntia.github.io/propagation-library-wiki
[gh-actions-test-badge]: https://img.shields.io/github/actions/workflow/status/NTIA/LFMF-python/tox.yml?branch=main&logo=pytest&logoColor=ffffff&label=Tests&labelColor=162E51
[gh-actions-test-link]: https://github.com/NTIA/LFMF-python/actions/workflows/tox.yml
[pypi-release-badge]: https://img.shields.io/pypi/v/LFMF-python?logo=pypi&logoColor=ffffff&label=Release&labelColor=162E51&color=D63E04
[pypi-release-link]: https://pypi.org/project/LFMF-python
[gh-issues-badge]: https://img.shields.io/github/issues/NTIA/LFMF-python?logo=github&label=Issues&labelColor=162E51
[gh-issues-link]: https://github.com/NTIA/LFMF-python/issues
[doi-badge]: https://zenodo.org/badge/LFMF-python.svg
[doi-link]: https://zenodo.org/badge/latestdoi/LFMF-python

This code repository contains the U.S. Reference Software Implementation of
Low Frequency / Medium Frequency (LF/MF) Propagation Model. This Python package wraps the
[base C++ implementation](https://github.com/NTIA/LFMF).

## Getting Started ##

> [!NOTE]
> The text below indicates this package is distributed on PyPi,
> however it is not yet uploaded. A link will be provided here when available.

This software is distributed on [PyPI](#) and is easily installable
using the following command.

```cmd
pip install LFMF
```

General information about using this model is available on
[its page on the **NTIA/ITS Propagation Library Wiki**](https://ntia.github.io/propagation-library-wiki/models/LFMF/).
Additionally, Python-specific instructions and code examples are available
[here](https://ntia.github.io/propagation-library-wiki/models/LFMF/python).

If you're a developer and would like to contribute to or extend this repository,
please review the guide for contributors [here](CONTRIBUTING.md) or open an
[issue](https://github.com/NTIA/LFMF-python/issues) to start a discussion.

## Development ##

This repository contains code which wraps [the C++ shared library](https://github.com/NTIA/LFMF)
as an importable Python module. If you wish to contribute to this repository,
testing your changes will require the inclusion of this shared library. You may retrieve
this either from the
[relevant GitHub Releases page](https://github.com/NTIA/LFMF/releases), or by
compiling it yourself from the C++ source code. Either way, ensure that the shared library
(`.dll`, `.dylib`, or `.so` file) is placed in `src/ITS/Propagation/LFMF/`, alongside `__init__.py`.

Below are the steps to build and install the Python package from the source code.
Working installations of Git and a [currently-supported version](https://devguide.python.org/versions/)
of Python are required. Additional requirements exist if you want to compile the shared
library from C++ source code; see relevant build instructions
[here](https://github.com/NTIA/LFMF?tab=readme-ov-file#configure-and-build).

1. Optionally, configure and activate a virtual environment using a tool such as
[`venv`](https://docs.python.org/3/library/venv.html) or 
[`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).


2. Clone the parent repository, then initialize the Git submodule containing the Python wrapper. This repository structure makes test data available to the Python wrapper.

    ```cmd
    # Clone the repository
    git clone https://github.com/NTIA/LFMF
    cd LFMF

    # Initialize Git submodule containing test data
    git submodule init

    # Clone the submodule
    git submodule update
    ```

3. Compile the C++ library for your platform, following instructions [here](https://github.com/NTIA/LFMF?tab=readme-ov-file#configure-and-build). Following these instructions should automatically copy the shared library into the location required by the Python wrapper.
    
    **OR**

    Download the shared library (`.dll`, `.so`, or `.dylib`) from a
[GitHub Release](https://github.com/NTIA/LFMF/releases). Then place the
downloaded file in `src/ITS/Propagation/LFMF/` (alongside `__init__.py`).


4. Install the local package and development dependencies into your current environment:

    ```cmd
    pip install .[dev]
    ```

5. To build the wheel for your platform:

    ```cmd
    hatchling build
    ```

### Running Tests ###

Python unit tests can be run to confirm successful installation. You will need to
clone this repository's test data submodule (as described above). Then, run the tests
with pytest using the following command.

```cmd
pytest
```

## References ##

LFMF-python: Update references

- [ITS Propagation Library Wiki](https://ntia.github.io/propagation-library-wiki)
- [LFMF Wiki Page](https://ntia.github.io/propagation-library-wiki/models/LFMF)
- [`ITS.Propagation.LFMF` C++ API Reference](https://ntia.github.io/LFMF)

## Contact ##

For technical questions, contact <code@ntia.gov>.