from toolbox import strings


def test_strings():
    testcases = (2, 4, 8, 16, 32, 64)
    for n in testcases:
        assert len(strings.randstring(n)) == n
    # TODO(jdb) Measure the entropy of the randstring process
