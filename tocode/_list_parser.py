from importlib import reload
import pathlib
from tocode.__inner_files__._built_in._built_in_file_manager import _reset_files

_current_abso_path = pathlib.Path(__file__).parent.absolute()

def listParser(str_list: str, no_string_quotation: bool = False):
    _reset_files()
    _lcd = ''
    if no_string_quotation:
        pass
    with open(_current_abso_path.joinpath('__inner_files__/_gen/__code_gen_list__.py'), 'r') as _inner_lcode_gen:
        _inner_lcode_gen = open(_current_abso_path.joinpath('__inner_files__/_gen/__code_gen_list__.py'), 'r')
        _lcd = _inner_lcode_gen.read()

    with open(_current_abso_path.joinpath('__inner_files__/_gen/__code_gen_list__.py'), 'w') as _inner_lcode_gen:
        _lcd = _lcd.replace('return', 'return ' + str_list)
        _inner_lcode_gen.write(_lcd)

    from .__inner_files__._gen import __code_gen_list__
    __code_gen_list__ = reload(__code_gen_list__)

    _generated_arr = __code_gen_list__._list_code__gen()
    return _generated_arr
