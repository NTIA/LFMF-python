# Low Frequency / Medium Frequency (LF/MF) Propagation Model, Python® Wrapper #

[![NTIA/ITS PropLib][proplib-badge]][proplib-link]
[![PyPI Release][pypi-release-badge]][pypi-release-link]
[![GitHub Actions Unit Test Status][gh-actions-test-badge]][gh-actions-test-link]
[![GitHub Issues][gh-issues-badge]][gh-issues-link]
[![DOI][doi-badge]][doi-link]

[proplib-badge]: https://img.shields.io/badge/PropLib-badge?label=%F0%9F%87%BA%F0%9F%87%B8%20NTIA%2FITS&labelColor=162E51&color=D63E04
[proplib-link]: https://ntia.github.io/propagation-library-wiki
[gh-actions-test-badge]: https://img.shields.io/github/actions/workflow/status/NTIA/LFMF-python/pytest.yml?branch=main&logo=pytest&logoColor=ffffff&label=Tests&labelColor=162E51
[gh-actions-test-link]: https://github.com/NTIA/LFMF-python/actions/workflows/pytest.yml
[pypi-release-badge]: https://img.shields.io/pypi/v/proplib-lfmf?logo=pypi&logoColor=ffffff&label=Release&labelColor=162E51&color=D63E04
[pypi-release-link]: https://pypi.org/project/proplib-lfmf
[gh-issues-badge]: https://img.shields.io/github/issues/NTIA/LFMF-python?logo=github&label=Issues&labelColor=162E51
[gh-issues-link]: https://github.com/NTIA/LFMF-python/issues
[doi-badge]: https://zenodo.org/badge/896234119.svg
[doi-link]: https://zenodo.org/badge/latestdoi/896234119

This code repository contains a Python wrapper for the NTIA/ITS implementation of the
Low Frequency / Medium Frequency (LF/MF) Propagation Model. LF/MF predicts basic transmission
loss in the frequency range 0.01 - 30 MHz for propagation paths over a smooth Earth and antenna
heights less than 50 meters. This Python package wraps the [NTIA/ITS C++ implementation](https://github.com/NTIA/LFMF).

## Getting Started ##

This software is distributed on [PyPI](https://pypi.org/project/proplib-lfmf) and is easily installable
using the following command.

```cmd
pip install proplib-lfmf
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

1. Clone this repository, then initialize the Git submodule containing the test data.

    ```cmd
    # Clone the repository
    git clone https://github.com/NTIA/LFMF-python
    cd LFMF-python

    # Initialize Git submodule containing test data
    git submodule init

    # Clone the submodule
    git submodule update
    ```

1. Download the shared library (`.dll`, `.so`, or `.dylib`) from a
[GitHub Release](https://github.com/NTIA/LFMF/releases). Then place the
downloaded file in `src/ITS/Propagation/LFMF/` (alongside `__init__.py`).

1. Install the local package and development dependencies into your current environment:

    ```cmd
    pip install .[dev]
    ```

1. To build the wheel for your platform:

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

- [ITS Propagation Library Wiki](https://ntia.github.io/propagation-library-wiki)
- [LFMF Wiki Page](https://ntia.github.io/propagation-library-wiki/models/LFMF)
- [`ITS.Propagation.LFMF` C++ API Reference](https://ntia.github.io/LFMF)
- Bremmer, H. "Terrestrial Radio Waves" _Elsevier_, 1949.
- DeMinco, N. "Medium Frequency Propagation Prediction Techniques and Antenna Modeling for Intelligent Transportation Systems (ITS) Broadcast Applications", [_NTIA Report 99-368_](https://www.its.bldrdoc.gov/publications/2399.aspx), August 1999
- DeMinco, N. "Ground-wave Analysis Model For MF Broadcast System", [_NTIA Report 86-203_](https://www.its.bldrdoc.gov/publications/2226.aspx), September 1986
- Sommerfeld, A. "The propagation of waves in wireless telegraphy", _Ann. Phys._, 1909, 28, p.665
- Wait, J. "Radiation From a Vertical Antenna Over a Curved Stratified Ground", _Journal of Research of the National Bureau of Standards_.  Vol 56, No. 4, April 1956. Research Paper 2671

## License ##

See [LICENSE](./LICENSE.md).

"Python" and the Python logos are trademarks or registered trademarks of the Python Software Foundation, used by the National Telecommunications and Information Administration with permission from the Foundation.

## Contact ##

For technical questions, contact <code@ntia.gov>.

## Disclaimer ##

Certain commercial equipment, instruments, or materials are identified in this project were used for the convenience of the developers. In no case does such identification imply recommendation or endorsement by the National Telecommunications and Information Administration, nor does it imply that the material or equipment identified is necessarily the best available for the purpose.
