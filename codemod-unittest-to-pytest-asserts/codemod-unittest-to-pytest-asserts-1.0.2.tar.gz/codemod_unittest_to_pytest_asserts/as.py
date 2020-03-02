class A:
    def one():
        def two():
            assert 1 != 2
        
    def three():
        assert 3 == 3
        def four():
            assert 4 == 4
