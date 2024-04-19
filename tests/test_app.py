from moonshot.app import process_text, remove_emoji, remove_punctuations, remove_numbers


"""
pytest tests\test_app.py::test_remove_stop_words
"""


def test_remove_stop_words():
    text1 = "This is a sample test sentence with numbers one, 2, 3.00 and four and an emoji 🏆!"
    assert process_text(text1) == "sample test sentence numbers one four emoji"

    text2 = "I owe party X 3K Euros"
    assert process_text(text2) == "owe party x euros"

    text3 = "123456789✍🌷📌"
    assert process_text(text3) == ""

    text5 = "&*@#🌷$*@#($*@✍📌(#%*($*%$*🌷#&%>)))"
    assert process_text(text5) == ""

    text6 = "🌷                     this is a sentence.............123 21312 ✍3 a"
    assert process_text(text6) == "sentence"


"""
pytest tests\test_app.py::test_remove_emoji
"""


def test_remove_emoji():
    text1 = "✍🌷📌👈🏻🖥"
    assert remove_emoji(text1) == ""

    text2 = "I am ✍writing test 🌷 cases to remove 👈🏻 emojis ✍ "
    assert remove_emoji(text2) == "I am writing test  cases to remove  emojis  "


"""
pytest tests\test_app.py::test_remove_punctuations
"""


def test_remove_punctuations():
    text1 = "(This test case is wonderful!)"
    assert remove_punctuations(text1) == "This test case is wonderful"

    text2 = "Adding more punctuations *&^^() to the sentence........!!!!"
    assert remove_punctuations(text2) == "Adding more punctuations  to the sentence"


"""
pytest tests\test_app.py::test_remove_numbers
"""


def test_remove_numbers():
    text1 = "He learnt to count numbers from 1, 2, three, 4.00 to 100K "
    assert remove_numbers(text1) == 'He learnt to count numbers from  ,  , three,  to   '

    text2 = "217823238, 33.555, 34.987"
    assert remove_numbers(text2) == ' ,  ,  '