import decimal
from decimal import Decimal
import random
import math

""" Qualean class based on Boolean+Quantum concepts """
class Qualean:
    """Qualean class based on Boolean and Quantan concepts"""
    def __init__(self, state): # 3 possible real states. True, False, and Maybe (1, 0, -1)
        """Initialize Qualean object"""
        self.state  = state

    @property
    def state(self):
        """Returns state"""
        return self._state

    @state.setter
    def state(self, state):
        """Set the state"""
        if state not in (0 , 1, -1):
            raise ValueError(f'Value of state must be among 0, 1 or -1')
        with decimal.localcontext() as ctx:
            ctx.prec = 10
            ctx.rounding = decimal.ROUND_HALF_EVEN
            state = Decimal(state)
            img = Decimal(random.uniform(-1,1))
            "Set state"
            self._state = state * img

    def __repr__(self):
        """ Return Qualean string for repr()."""
        return (f'Qualean(state={self.state})')

    def __str__(self):
        """ String representation for Qualean"""
        return((f'Qualean number - state is :{self.state}'))

    def __and__(self,other):
        """Return boolean and"""
        if isinstance(other, Qualean):
            raise NotImplementedError('Incorrect data type')
        return bool(self.state) and bool(other.state)

    def __or__(self,other):
        """Return boolean or"""
        if isinstance(other, Qualean):
            raise NotImplementedError('Incorrect data type')
        return bool(self.state) or bool(other.state)

    def __eq__(self, other):
        """ Check for the equality of qualeans"""
        if isinstance(other, Qualean):
            return(self.state==other.state)
        elif isinstance(other, bool):
            return(bool(self)==other)
        else:
            raise NotImplementedError('Incorrect data type')

    def __float__(self):
        """ Type cast to float """
        return float(self.state)

    def __ge__(self,other):
        """ Check for the greater than or equal to ineqaulity of qualeans"""
        if isinstance(other, Qualean):
            return(self.state >= other.state)
        else:
            raise NotImplementedError('Incorrect data type')

    def __gt__(self,other):
        """ Check for the greater than ineqaulity of qualeans"""
        if isinstance(other, Qualean):
            return(self.state > other.state)
        else:
            raise NotImplementedError('Incorrect data type')

    def __invertsign__(self):
        """ Invert the sign of qualean"""
        self = self * -1
        return self

    def __le__(self,other):
        """ Check for the lesser than or equal to ineqaulity of qualeans"""
        if isinstance(other, Qualean):
            return(self.state <= other.state)
        else:
            raise NotImplementedError('Incorrect data type')

    def __lt__(self,other):
        """ Check for the lesser than ineqaulity of qualeans"""
        if isinstance(other, Qualean):
            return(self.state < other.state)
        else:
            raise NotImplementedError('Incorrect data type')

    def __add__(self, other):
        "Add to qualean"
        with decimal.localcontext() as ctxa:
            ctxa.prec = 10
            ctxa.rounding = decimal.ROUND_HALF_EVEN
            if isinstance(other, (int,float,Decimal)):
                other = Decimal(other,ctxa)
                result = Qualean(0)
                result._state = Decimal(self.state + other, ctxa)
                return result
            elif isinstance(other,Qualean):
                result = Qualean(0)
                result._state = Decimal(self.state + other.state, ctxa)
                return result
            else:
                raise NotImplementedError('Incorrect data type')

    def __iadd__(self, other):
        "Add to qualean"
        with decimal.localcontext() as ctxa:
            ctxa.prec = 10
            ctxa.rounding = decimal.ROUND_HALF_EVEN
            if isinstance(other, (int,float,Decimal)):
                other = Decimal(other,ctxa)
                result = Qualean(0)
                result._state = Decimal(self.state + other, ctxa)
                return result
            elif isinstance(other,Qualean):
                result = Qualean(0)
                result._state = Decimal(self.state + other.state, ctxa)
                return result
            else:
                raise NotImplementedError('Incorrect data type')

    def __mul__(self, other):
        "Multiply to qualean"
        with decimal.localcontext() as ctxm:
            ctxm.prec = 10
            ctxm.rounding = decimal.ROUND_HALF_EVEN
            if isinstance(other, (int,float,Decimal)):
                other = Decimal(other,ctxm)
                result = Qualean(0)
                result._state = Decimal(self.state * other, ctxm)
                return result
            elif isinstance(other,Qualean):
                result = Qualean(0)
                result._state = Decimal(self.state * other.state, ctxm)
                return result
            else:
                raise NotImplementedError('Incorrect data type')

    def __sqrt__(self):
        "Square root of qualean"
        with decimal.localcontext() as ctxs:
            ctxs.prec = 10
            ctxs.rounding = decimal.ROUND_HALF_EVEN
            if self.state > 0:
                return self.state.sqrt()
            else:
                return complex(0,self.state.__abs__().sqrt())

    def __bool__(self):
        "Return False if state is 0 else True"
        return bool(self.state)

def check_qualean_addition(qual, n):
    """Test the qualean addition"""
    with decimal.localcontext() as ctx1:
        ctx1.prec = 10
        ctx1.rounding = decimal.ROUND_HALF_EVEN
        qsum = Qualean(0)
        for i in range(n):
            qsum = qsum + qual
        prod = qual * n
    return round(qsum.state,6) == round(prod.state,6)
