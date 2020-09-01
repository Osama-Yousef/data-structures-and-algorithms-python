from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


def test_multi_bracket_validation():
    assert multi_bracket_validation('{}')
    assert multi_bracket_validation('{}(){}')
    assert multi_bracket_validation('{}()[[]]')
    assert multi_bracket_validation('()')
    assert multi_bracket_validation('(){}[]')
    assert multi_bracket_validation('{[]}')
    assert not multi_bracket_validation('(]')
    assert not multi_bracket_validation('((')
    assert not multi_bracket_validation('([)]')
    assert not multi_bracket_validation('[({}]')
    assert not multi_bracket_validation('{(})')
    assert not multi_bracket_validation('{')
    assert not multi_bracket_validation(')')
    assert not multi_bracket_validation('[}')
    

