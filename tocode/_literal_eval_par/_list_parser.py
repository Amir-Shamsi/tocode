import sys
import traceback
from importlib import reload
import pathlib
from tocode.__inner_files__._built_in._built_in_file_manager import __reset_files
from tocode._literal_eval_par._str_parser import __Str

_current_abso_path = pathlib.Path(__file__).parent.parent.absolute()

def listParser(str_list: str, no_string_quotation: bool = False):
    """
    the list parser will convert list in string to the list and there is
    an option available `no_string_quotation` if you string contains the
    needed quotations like bellow:
        Example = "['hello', 5, 7, ('damage', 5)]"
    make it 'False' or leave it because default is False.

    and when ever your strings don't contain any quotation make this 'True'
    it will add quotation for you like bellow:
        Example = [This is example, 9, [[[hello, 4]]]]
    :param str_list: the list in string which must convert to actual python list
    :param no_string_quotation: does the strings contain quotation?
    :return: actual python list converted from str_list
    """
    __reset_files()
    _lcd = ''
    if no_string_quotation:
        str_list = __Str.space_encoder(str_list)
        str_list_final = str_list
        _addi_index = 0
        while True:
            try:
                exec(str_list)
            except SyntaxError as err:
                error_class = err.__class__.__name__
                detail = err.args[0]
                line_number = err.lineno
            except Exception as err:
                error_class = err.__class__.__name__
                detail = err.args[0]
                cl, exc, tb = sys.exc_info()
                line_number = traceback.extract_tb(tb)[-1][1]
            else:
                break

            try:
                if detail.split('\'')[0] == 'name ' and detail.split('\'')[2] == ' is not defined':
                    _f_index = str_list.find(detail.split('\'')[1])
                    str_list = str_list.replace(detail.split('\'')[1], "'" + 'त'*(len(detail.split('\'')[1])) + "'", 1)
                    str_list_final = str_list_final[:_f_index] + "'" + str_list_final[_f_index: (_f_index + len(detail.split('\'')[1]))] + "'" + str_list_final[(_f_index + len(detail.split('\'')[1])):]
                else:
                    return detail + ' at line ' + str(line_number)
            except Exception as ignored:
                return detail + ' at line ' + str(line_number)
        str_list = __Str.space_decoder(str_list_final)

    with open(_current_abso_path.joinpath('__inner_files__/_gen/__code_gen_list__.py'), 'r') as _inner_lcode_gen:
        _inner_lcode_gen = open(_current_abso_path.joinpath('__inner_files__/_gen/__code_gen_list__.py'), 'r')
        _lcd = _inner_lcode_gen.read()

    with open(_current_abso_path.joinpath('__inner_files__/_gen/__code_gen_list__.py'), 'w') as _inner_lcode_gen:
        _lcd = _lcd.replace('return', 'return ' + str_list)
        _inner_lcode_gen.write(_lcd)

    from tocode.__inner_files__._gen import __code_gen_list__
    __code_gen_list__ = reload(__code_gen_list__)

    _generated_arr = __code_gen_list__._list_code__gen()
    return _generated_arr
