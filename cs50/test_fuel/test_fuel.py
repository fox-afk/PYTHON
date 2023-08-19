from fuel import converted, gauge
def main():
    test_corrected_input()
    test_zero_division()
    test_value()

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        converted('1/0')

def test_value():
    with pytest.raises(ValueError):
            converted('cat/dog')

def test_corrected_input():
    assert converted('1/4')==25 and gauge(25)=='25%'
    assert converted('1/100')==1 and gauge(1)=='E'
    assert converted('99/100')==99 and gauge(99)=='F'


if __name__=="__main__":
    main()