from moonshot.app import clean_text


"""
pytest tests\test_app.py::
"""

def test_remove_stop_words():
    text1 = "This is a sample test sentence with numbers one, 2, 3.00 and four and an emoji 🏆!"
    assert clean_text(text1) == 'sample test sentence numbers one four emoji'

    text2 = "I owe party X 3K Euros"    
    assert clean_text(text2)=='owe party x euros'
    
