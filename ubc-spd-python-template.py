# UBC Systematic Program Design - Python Template

# https://courses.edx.org/courses/course-v1:UBCx+SPD1x+2T2016/77860a93562d40bda45e452ea064998b/#Atomic
Please translate the following Racket code into Python Code with type annotations. No explanation is needed.

;; Time is Natural
;; interp. number of clock ticks since start of game

(define START-TIME 0)
(define OLD-TIME 1000)

#;
(define (fn-for-time t)
  (... t))

;; Template rules used:
;;  - atomic non-distinct: Natural

from typing import NewType

Time = NewType('Time', int)

START_TIME: Time = 0
OLD_TIME: Time = 1000

def fn_for_time(t: Time) -> ...:
    ...

# https://courses.edx.org/courses/course-v1:UBCx+SPD1x+2T2016/77860a93562d40bda45e452ea064998b/#Interval

Please translate the following Racket code into Python Code with type annotations. No explanation is needed.

;; Countdown is Integer[0, 10]
;; interp. the number of seconds remaining to liftoff
(define C1 10)  ; start
(define C2 5)   ; middle
(define C3 0)   ; end
 
#;
(define (fn-for-countdown cd)
  (... cd))

;; Template rules used:
;;  - atomic non-distinct: Integer[0, 10]

from typing import NewType
Countdown = NewType('Countdown', int)

C1: Countdown = 10
C2: Countdown = 5
C3: Countdown = 0

def fn_for_countdown(cd: Countdown) -> ...:
    ...

""" 
In Python, you can't directly specify a range for a type like you can in
some other languages. However, you can enforce this constraint with a function 
that creates a Countdown only if the input is within the desired range. 
Here's how you can do it:
"""

# method 1
class Countdown:
    def __init__(self, value: int):
        if value < 0 or value > 10:
            raise ValueError("Value must be between 0 and 10")
        self.value = value

# method 2
import dataclasses

@dataclasses.dataclass
class Example:
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise ValueError("Value must be non-negative")

# method 3
import dataclasses

@dataclasses.dataclass
class Countdown:
    _value: int

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0 or value > 10:
            raise ValueError("Value must be between 0 and 10")
        self._value = value

""" 
In this code, the value attribute is replaced with a _value attribute and a value
property. The value property has a getter that just returns _value,
and a setter that validates the value before setting _value. 
This way, the validation is performed not just when the instance is initialized,
but every time value is set.
"""

Please translate the following Racket code into Python Code with type annotations. No explanation is needed.











Please translate the following Racket code into Python Code with type annotations. No explanation is needed.





Please translate the following Racket code into Python Code with type annotations. No explanation is needed.







Please translate the following Racket code into Python Code with type annotations. No explanation is needed.








Please translate the following Racket code into Python Code with type annotations. No explanation is needed.








Please translate the following Racket code into Python Code with type annotations. No explanation is needed.







Please translate the following Racket code into Python Code with type annotations. No explanation is needed.



