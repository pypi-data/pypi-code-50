from ungreat_matching import ungreat_match, num_match_max, num_match_min


test_data = [['python','Python'],
['python','python3.7'],
['PYTHON','python3.7'],
['PYTHON','python3.7.3']]
for data in test_data:
    print(ungreat_match(data[0],data[1], mismatching_chars=5, mkdefolt=0.7))
