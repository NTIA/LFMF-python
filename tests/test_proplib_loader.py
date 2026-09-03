from ctypes import POINTER, c_char_p, cast

import pytest
from ITS.Propagation.LFMF.proplib_loader import PropLibCDLL


@pytest.mark.parametrize(
    ("system_name", "pointer_size", "suffix"),
    [
        ("Windows", 8, "-x64.dll"),
        ("Windows", 4, "-x86.dll"),
        ("Linux", 8, "-x86_64.so"),
        ("Darwin", 8, "-universal.dylib"),
    ],
)
def test_get_lib_name_uses_expected_platform_suffix(
    monkeypatch: pytest.MonkeyPatch,
    system_name: str,
    pointer_size: int,
    suffix: str,
) -> None:
    monkeypatch.setattr("ITS.Propagation.LFMF.proplib_loader.platform.system", lambda: system_name)
    monkeypatch.setattr("ITS.Propagation.LFMF.proplib_loader.struct.calcsize", lambda _: pointer_size)

    lib_path = PropLibCDLL.get_lib_name("Example-1.0")

    assert lib_path.endswith(suffix)
    assert "Example-1.0" in lib_path


def test_get_lib_name_rejects_unknown_platform(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("ITS.Propagation.LFMF.proplib_loader.platform.system", lambda: "Plan9")

    with pytest.raises(NotImplementedError, match="Unsupported operating system: Plan9"):
        PropLibCDLL.get_lib_name("Example-1.0")


def test_constructor_raises_clear_error_for_missing_library(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_path = r"C:\missing\Example-1.0-x64.dll"
    monkeypatch.setattr(PropLibCDLL, "get_lib_name", staticmethod(lambda _: fake_path))

    with pytest.raises(FileNotFoundError, match="Shared library 'Example-1.0' was not found"):
        PropLibCDLL("Example-1.0")


def test_err_check_returns_for_success() -> None:
    class FakeLibrary:
        pass

    PropLibCDLL.err_check(FakeLibrary(), 0)


def test_err_check_raises_library_message() -> None:
    error_message = b"example failure"
    freed_messages: list[object] = []

    class FakeLibrary:
        @staticmethod
        def GetReturnStatusCharArray(_code):
            return cast(c_char_p(error_message), POINTER(c_char_p))

        @staticmethod
        def FreeReturnStatusCharArray(message) -> None:
            freed_messages.append(message)

    with pytest.raises(RuntimeError, match="example failure"):
        PropLibCDLL.err_check(FakeLibrary(), 5)

    assert len(freed_messages) == 1


def test_err_check_handles_missing_error_text() -> None:
    freed_messages: list[object] = []

    class FakeLibrary:
        @staticmethod
        def GetReturnStatusCharArray(_code):
            return cast(c_char_p(None), POINTER(c_char_p))

        @staticmethod
        def FreeReturnStatusCharArray(message) -> None:
            freed_messages.append(message)

    with pytest.raises(RuntimeError, match="no error text was returned"):
        PropLibCDLL.err_check(FakeLibrary(), 9)

    assert len(freed_messages) == 1
