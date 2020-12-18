import os
import pytest

try:
    from src.data_prep import preprocessing_helpers
except ModuleNotFoundError:
    os.chdir(os.path.join(os.getcwd(), '../../'))
    print(f'Warning: Changing directory to run test files from {os.getcwd()} directory.')
    
from src.data_prep.preprocessing_helpers import convert_os_filepath

class TestProperInput(object):
    
    def test_convert_os_filepath_with_proper_string_input(self):
        assert convert_os_filepath('.\\Users\Documents') == './Users/Documents' 
        assert convert_os_filepath('.\\') == './'

    def test_convert_os_filepath_with_empty_string_input(self):
        assert convert_os_filepath('') == '' 
        
    def test_convert_os_filepath_with_empty_input(self):
        with pytest.raises(TypeError) as exception_info:
            convert_os_filepath()
        assert exception_info.match("missing 1 required positional argument")
