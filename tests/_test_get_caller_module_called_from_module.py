from pydantic.generics import get_caller_module_name

try:
    get_caller_module_name()
except RuntimeError as e:
    assert isinstance(e, RuntimeError), e
    assert e.args == ('This function must be used inside another function',), e.args
    assert isinstance(e.__cause__, IndexError), e.__cause__
    assert isinstance(e.__context__, IndexError), e.__context__
else:
    raise AssertionError('RuntimeError was not raised')
