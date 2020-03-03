from sciencebeam_alignment.levenshtein import get_levenshtein_distance, get_levenshtein_ratio


class TestGetLevenshteinDistance(object):
    def test_should_return_zero_for_two_equal_sequences(self):
        assert get_levenshtein_distance('abc', 'abc') == 0

    def test_should_return_one_for_one_substitution(self):
        assert get_levenshtein_distance('abc', 'axc') == 1

    def test_should_return_one_for_one_deletion(self):
        assert get_levenshtein_distance('abc', 'ac') == 1

    def test_should_return_one_for_one_insertion(self):
        assert get_levenshtein_distance('abc', 'abxc') == 1

    def test_should_return_three_for_kitten_vs_sitten(self):
        assert get_levenshtein_distance('kitten', 'sitting') == 3


class TestGetLevenshteinRatio(object):
    def test_should_return_zero_for_two_empty_sequences(self):
        assert get_levenshtein_ratio('', '') == 0.0

    def test_should_return_one_for_two_equal_sequences(self):
        assert get_levenshtein_ratio('abc', 'abc') == 1.0

    def test_should_return_point_five_for_half_substitution(self):
        assert get_levenshtein_ratio('abcd', 'axxd') == 0.5

    def test_should_return_point_five_for_half_deletion(self):
        assert get_levenshtein_ratio('abcd', 'ad') == 0.5
