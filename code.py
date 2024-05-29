
try:
    from sympy import *

    def sum_of_sequence():
        """There exists a unique increasing geometric sequence of five 2-digit positive integers. What is their sum?"""
        sum_of_sequence = 0
        for a in range(10, 100):
            for r in range(2, 10):
                sequence = [a * r**i for i in range(5)]
                if all(10 <= n < 100 for n in sequence) and sorted(sequence) == sequence:
                    sum_of_sequence = sum(sequence)
                    return sum_of_sequence
    
    result = sum_of_sequence()
    print(result)
    
    def sum_of_sequence():
        """There exists a unique increasing geometric sequence of five 2-digit positive integers. What is their sum?"""
        sum_of_sequence = 0
        for a in range(10, 100):
            for r in range(2, 10):
                sequence = [a * r**i for i in range(5)]
                if all(10 <= n < 100 for n in sequence) and sorted(sequence) == sequence:
                    sum_of_sequence = sum(sequence)
                    return sum_of_sequence
                    break  # found the sequence, no need to continue the loop
    
    result = sum_of_sequence()
    print(result)
    
    def sum_of_sequence():
        """There exists a unique increasing geometric sequence of five 2-digit positive integers. What is their sum?"""
        sum_of_sequence = 0
        for a in range(10, 100):
            for r in range(2, 10):
                sequence = [a * r**i for i in range(5)]
                if all(10 <= n < 100 for n in sequence) and sorted(sequence) == sequence:
                    sum_of_sequence = sum(sequence)
                    return sum_of_sequence
    
    result = sum_of_sequence()
    print(result)
    
    def sum_of_sequence():
        """There exists a unique increasing geometric sequence of five 2-digit positive integers. What is their sum?"""
        for a in range(10, 100):
            for r in range(2, 10):
                sequence = [a * r**i for i in range(5)]
                if all(10 <= n < 100 for n in sequence) and sorted(sequence) == sequence:
                    return sum(sequence)
    
    result = sum_of_sequence()
    print(result)
    
    def sum_of_sequence():
        """There exists a unique increasing geometric sequence of five 2-digit positive integers. What is their sum?"""
        for a in range(10, 100):
            for r in range(2, 10):
                sequence = [a * r**i for i in range(5)]
                if all(10 <= n < 100 for n in sequence) and sorted(sequence) == sequence:
                    sum_of_sequence = sum(sequence)
                    return sum_of_sequence
    
    result = sum_of_sequence()
    print(result)
    
    def sum_of_sequence():
        """There exists a unique increasing geometric sequence of five 2-digit positive integers. What is their sum?"""
        for a in range(10, 100):
            for r in range(2, 10):
                sequence = [a * r**i for i in range(5)]
                if all(10 <= n < 100 for n in sequence) and sorted(sequence) == sequence:
                    sum_of_sequence = sum(sequence)
                    return sum_of_sequence
    
    result = sum_of_sequence()
    print(result)
    
    def sum_of_sequence():
        """There exists a unique increasing geometric sequence of five 2-digit positive integers. What is their sum?"""
        for a in range(10, 100):
            for r in range(2, 10):
                sequence = [a * r**i for i in range(5)]
                if all(10 <= n < 100 for n in sequence) and sorted(sequence) == sequence:
                    sum_of_sequence = sum(sequence)
                    return sum_of_sequence
    
    result = sum_of_sequence()
    print(result)
    
    def sum_of_sequence():
        """There exists a unique increasing geometric sequence of five 2-digit positive integers. What is their sum?"""
        for a in range(10, 100):
            for r in range(2, 10):
                sequence = [a * r**i for i in range(5)]
                if all(10 <= n < 100 for n in sequence) and sorted(sequence) == sequence:
                    sum_of_sequence = sum(sequence)
                    return sum_of_sequence
    
    result = sum_of_sequence()
    print(result)
    
except Exception as e:
    print(e)
    print('FAIL')
