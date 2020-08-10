import pytest
import random
import string
import session4
import os
import inspect
import re
import math
import decimal
from decimal import Decimal

decimal.getcontext().prec = 10
decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN


README_CONTENT_CHECK_FOR = [
    'and',
    'or',
    'repr',
    'str',
    'add',
    'eq',
    'float',
    'ge',
    'gt',
    'invertsign',
    'le',
    'lt',
    'mul',
    'sqrt',
    'bool',
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_innacurate_addition():
    """q + q + q ... 100 times = 100 * q"""
    state = random.choice([-1,0,1])
    qualean = session4.Qualean(state)
    assert session4.check_qualean_addition(qualean, 100)== True, "Rounding error for qualean states"

def test_qualean_square_root():
    """q.__sqrt__() = Decimal(q).sqrt"""
    for _ in range(100):
        state = random.choice([-1,0,1])
        q = session4.Qualean(state)
        if q.state >= 0:
            assert(q.__sqrt__() == Decimal(q.state).sqrt()), " Square root not calculated properly"

def test_qualean_negative_square_root():
    """q.__sqrt__() = Decimal(q).sqrt"""
    for _ in range(100):
        state = random.choice([-1,0,1])
        q = session4.Qualean(state)
        if q.state < 0:
            assert(isinstance(q.__sqrt__(),complex)), " Square root not calculated properly for negative state of qualean"

def test_normal_dist_state():
    """sum of 1 million different qs is very close to zero (use isclose)"""
    pass

def test_boolean_and():
    """# q1 and q2 returns False when q1 or q2 is False"""
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    q3 = session4.Qualean(-1)
    assert q1 and q3 == True , "And is not working properly while state of both qualean is not 0"
    assert q1 and q2 == False , "And is not working properly while state of both qualean is not same"

def test_boolean_or():
    """# q1 or q2 returns False when q1 and q2 are False"""
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    q3 = session4.Qualean(-1)
    q4 = session4.Qualean(0)
    assert q1 or q3 == True , "Or is not working properly while state of both qualean is not 0"
    assert q1 or q2 == True , "Or is not working properly while state of both qualean is not same"
    assert q3 or q2 == True , "Or is not working properly while state of both qualean is not 0"
    assert q2 or q4 == False , "Or is not working properly while state of both qualean is 0"

def test_string_repr():
    """test string representation"""
    q = session4.Qualean(1)
    assert q.__repr__() == f'Qualean(state={q.state})', 'The representation of the Qualean object does not meet expectations'

def test_string_representation():
    """test string representation in readable form"""
    q = session4.Qualean(1)
    assert q.__str__() == f'Qualean number - state is :{q.state}', 'The print of the Qualean object does not meet expectations'

def test_qualean_float():
    """test conversion to float"""
    for _ in range(100):
        state = random.choice([-1,0,1])
        q = session4.Qualean(state)
        assert q.__float__() == float(q.state), f'Qualean number to float conversion does not meet expectations'

def test_qualean_ge_inequality():
    """ Check for the greater than or equal to ineqaulity of qualeans"""
    for _ in range(100):
        state = random.choice([-1,0,1])
        q1 = session4.Qualean(state)
        state = random.choice([-1,0,1])
        q2 = session4.Qualean(state)
        if q1.state >= q2.state:
            assert (q1 >= q2) == True, f'{q1}, {q2}, Greater than or equal to ineqaulity of qualeans is not implemented correctly'
        else:
            assert (q1 >= q2) == False, f'Greater than or equal to ineqaulity of qualeans is not implemented correctly'

def test_qualean_gt_inequality():
    """ Check for the greater than ineqaulity of qualeans"""
    for _ in range(100):
        state = random.choice([-1,0,1])
        q1 = session4.Qualean(state)
        state = random.choice([-1,0,1])
        q2 = session4.Qualean(state)
        if q1.state > q2.state:
            assert (q1 > q2) == True, f'{q1}, {q2}, Greater than ineqaulity of qualeans is not implemented correctly'
        elif  q1.state == q2.state == 0:
            assert (q1 > q2) == False, f'Greater than ineqaulity of qualeans is not implemented correctly'

def test_qualean_le_inequality():
    """ Check for the lesser than or equal to ineqaulity of qualeans"""
    for _ in range(100):
        state = random.choice([-1,0,1])
        q1 = session4.Qualean(state)
        state = random.choice([-1,0,1])
        q2 = session4.Qualean(state)
        if q1.state <= q2.state:
            assert (q1 <= q2) == True, f'{q1}, {q2}, Lesser than or equal to ineqaulity of qualeans is not implemented correctly'
        else:
            assert (q1 <= q2) == False, f'Lesser than or equal to ineqaulity of qualeans is not implemented correctly'

def test_qualean_lt_inequality():
    """ Check for the lesser than or equal to ineqaulity of qualeans"""
    for _ in range(100):
        state = random.choice([-1,0,1])
        q1 = session4.Qualean(state)
        state = random.choice([-1,0,1])
        q2 = session4.Qualean(state)
        if q1.state < q2.state:
            assert (q1 < q2) == True, f'{q1}, {q2}, Lesser than ineqaulity of qualeans is not implemented correctly'
        elif  q1.state == q2.state == 0:
            assert (q1 < q2) == False, f'Greater than ineqaulity of qualeans is not implemented correctly'

def test_sign_inversion():
    """Check sign inversion"""
    for _ in range(100):
        state = random.choice([-1,0,1])
        q = session4.Qualean(state)
        assert q + q.__invertsign__() == session4.Qualean(0) , f'Qualean number to sign inversion is not implemented correctly'

def test_qual_to_bool():
    """Check qual to bool conversion"""
    for _ in range(100):
        state = random.choice([-1,0,1])
        q = session4.Qualean(state)
        assert isinstance(q.__bool__(),bool), f'Qualean number to boolean conversion does not meet expectations'
