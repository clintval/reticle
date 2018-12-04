from datetime import datetime

from hypothesis import example, given
from hypothesis.strategies import integers, datetimes

from pendant.util import ExitCode, format_ISO8601


@given(integers())
@example(0)
def test_exit_code(integer):
    exit_code = ExitCode(integer)

    if integer == 0:
        assert exit_code.is_ok()
    if integer != 0:
        assert not exit_code.is_ok()

    assert exit_code == ExitCode(integer)
    assert repr(exit_code) == f'ExitCode({integer})'

@given(datetimes())
def test_format_ISO8601(date):
    expected = date.replace(microsecond=0)
    actual = datetime.strptime(format_ISO8601(date), '%Y-%m-%dT%H-%M-%S')
    assert expected == actual