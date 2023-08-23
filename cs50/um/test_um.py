from um import count
def main():
    test_surrounded_by_space()
    test_upper_lower_case()
    test_word_with_um()
def test_upper_lower_case():
    assert count('Um, thanks for the album.')==1
    assert('Um, thanks, um...')==2
def test_word_with_um():
    assert count('yummi')==0
def test_surrounded_by_space():
    assert count('hello um world')==1
    assert count('um?')==1
if __name____=="__main__":
    main()