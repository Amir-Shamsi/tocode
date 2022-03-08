import pathlib
import os
def __reset_files():
    """
     file rester
    """
    _current_abso_path = pathlib.Path(__file__).parent.parent.absolute()
    _inner_lcode_src = open(_current_abso_path.joinpath('_src/__code_sr_list__.py'), 'r')
    _raw = _inner_lcode_src.read()
    _inner_lcode_src.close()
    os.remove(_current_abso_path.joinpath('_gen/__code_gen_list__.py'))
    _inner_lcode_gen = open(_current_abso_path.joinpath('_gen/__code_gen_list__.py'), 'w')
    _inner_lcode_gen.write(_raw)
    _inner_lcode_gen.close()