def sequence(n):
    # Check user input
    if n < 0 or n > 1000000000:
        raise ValueError('Input must be between 0 and 1,000,000,000.')
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev_prev_member = 0  # The (n-2)th member
    prev_member = 1  # The (n-1)th member
    
    for _ in range(2, n+1):
        # Calculate the next element as the sum of the digits of the previous two elements
        next_element = sum(int(digit) for digit in str(prev_prev_member)) + sum(int(digit) for digit in str(prev_member))
        
        prev_prev_member = prev_member
        prev_member = next_element
    
    return prev_member

# Main 
if __name__ == '__main__':
    print(sequence(11))