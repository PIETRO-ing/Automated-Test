import add_number

def test_conv_ls():
    assert add_number.conv_ls(987) == [9,8,7]
    assert add_number.conv_ls(0), [0]

def test_conv_nmbr():    
    assert add_number.conv_nmbr([9,8,7]) == 987
    
def test_delete_neg():
    assert add_number.delete_neg(-987,5) == [5,9,8,7]
    assert add_number.delete_neg(-12354,5) == [5,1,2,3,5,4]

def test_add_integer():
    assert add_number.add_integer([9,7,8,9],5) == [9,7,8,9,5]
    assert add_number.add_integer([1,2,3],5) == [5,1,2,3]
    assert add_number.add_integer([0],5) ==[5,0]
    assert add_number.add_integer([9,1,7,8],5) == [9,5,1,7,8]
    
def test_solution():
    assert add_number.solution(0) == 50
    assert add_number.solution(123) == 5123
    assert add_number.solution(9157) == 95157
    assert add_number.solution(98789) == 987895
    assert add_number.solution(0) == 50
    assert add_number.solution(-123) == -5123
    assert add_number.solution(-9898989) == -59898989
    assert add_number.solution(-91789) == -591789



