import di

def test_div_5():
    num=5
    result=di.divisible_5(num)
    assert result == True

def test_div_7():
    num=3
    result=di.div_7(num)
    assert result == False

def test_div_9():
    num=9
    result=di.div_9(num)
    assert result == True

def test_div_10():
    num=8
    result=di.div_10(num)
    assert result == False