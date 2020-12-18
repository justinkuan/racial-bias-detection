'''TESTs for preprocessing_helper functions'''

class TestProperInput(object):
    
    '''Test convert_os_filepath'''
    from src.data_prep.preprocessing_helpers import convert_os_filepath

    def test_convert_os_filepath_with_proper_string_input(self):
        assert convert_os_filepath('.\\Users\Documents') == './Users/Documents' 
        assert convert_os_filepath('.\\') == './'

        assert not convert_os_filepath('./Users/Documents') == './/Users//Documents'
        assert not convert_os_filepath('./') == './/'

    def test_convert_os_filepath_with_empty_string_input(self):
        assert convert_os_filepath('') == '' 
        assert not convert_os_filepath('') == '/'

    def test_convert_os_filepath_with_empty_input(self):
        with pytest.raises(TypeError) as exception_info:
            convert_os_filepath()
        assert exception_info.match("missing 1 required positional argument")
    
    '''Test remove_empty_articles'''
    from src.data_prep.preprocessing_helpers import remove_empty_articles

    def test_remove_empty_articles_with_dataframe_input(self):
        pass

    def test_remove_empty_articles_with_non_dataframe_input(self):
        pass

    '''Test impute_nans'''
    from src.data_prep.preprocessing_helpers import impute_nans

    def test_impute_nans_with_dataframe_input(self):
        pass

    def test_impute_nans_with_non_dataframe_input(self):
        pass

    '''Test load_first_subset'''
    
    '''Test save_to_parquet'''
    
class TestProperOutput(object):
    
    '''Test convert_os_filepath'''
    from src.data_prep.preprocessing_helpers import convert_os_filepath

    def test_convert_os_filepath_with_proper_output(self):
        pass
