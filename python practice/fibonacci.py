"""
Fibonacci Sequence Calculator Function

Objective:
Write a function named 'fibonacci_sequence' to generate the Fibonacci sequence up to a given number using a while loop.

Function Parameter:
1. max_value (integer): Maximum value for the Fibonacci sequence.

Instructions:
- Use a while loop to generate the Fibonacci sequence up to 'max_value'.
- Return the sequence as a list.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. fibonacci_sequence(10) should return the Fibonacci sequence up to 10.
2. fibonacci_sequence(1) should return the Fibonacci sequence up to 1.
3. fibonacci_sequence(0) should return a sequence with 0.
4. fibonacci_sequence(-5) should handle negative input.
"""


def fibonacci_sequence(max_value):
    if max_value >=0:
        fib_sequence=[0,1]
        while fib_sequence[-1]+fib_sequence[-2] <= max_value:
            next_fib=fib_sequence[-1]+fib_sequence[-2]
        #fib_sequence[-1] means the last number of the sequence, -2 means the second-to-last number.
            fib_sequence.append(next_fib)
        return fib_sequence
        
        #append() 是 Python 列表对象的一个方法，用于在列表末尾添加新的元素。
        #next_fib 是在循环中计算得到的下一个斐波那契数值。
        #fib_sequence.append(next_fib) 将 next_fib 添加到 fib_sequence 列表的末尾。
    else:
        print("Error, please input 0 or postive number")

    # Implement the Fibonacci sequence calculation using a while loop
   


# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))  # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))  # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Empty list or error message
