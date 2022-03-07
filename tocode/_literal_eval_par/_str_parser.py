
__inner_signs__ = ['{', '}', '[', ']', '(', ')', ',', '', ':']
class __Str:
    """
    the class contain string methods
    """
    @staticmethod
    def space_encoder(_str: str):
        """
        will encode spaces inside list in string.
        :param _str: list in string
        :return: return encoded string
        """
        _numeric_flag = False
        _str = list(_str)
        _space_index_st = 0
        for _index in range(len(_str)):
            if _str[_index] == ' ':
                if _str[_index - 1] not in __inner_signs__ and _str[_index + 1] not in __inner_signs__ and not _numeric_flag:
                    _str[_index] = 'र'
                    if _space_index_st == 0:
                        _space_index_st = _index
                else:
                    _str[_index] = ''
            else:
                if _str[_index] in __inner_signs__:
                    _numeric_flag = True
                if (not _str[_index].isnumeric()) and _str[_index] != ' ' and _str[_index] != '' and (_str[_index] not in __inner_signs__):
                    _numeric_flag = False

                if _space_index_st > 0 and _str[_index] == ',':
                    for _ind in range(_space_index_st, _index):
                        _str[_ind] = ''

                _space_index_st = 0
        return ''.join(_str)

    @staticmethod
    def space_decoder(_str: str):
        """
        will decode spaces inside list in string.
        :param _str: list in string
        :return: return encoded string
        """
        _str = list(_str)
        for _index in range(len(_str)):
            if _str[_index] == 'र':
                _str[_index] = ' '
        return ''.join(_str)
