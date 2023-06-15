#!/usr/bin/env python3

def print_fibonacci(length):
    f_sequence = []
    
    if length > 0:
       ( f_sequence.append(0))
    if length > 1:
        ( f_sequence.append(1))
    if length >2:
        for i in range(2, length) :
            f_sequence.append(
                f_sequence[i-1] + f_sequence[i-2]
            )
    
    print(f_sequence)