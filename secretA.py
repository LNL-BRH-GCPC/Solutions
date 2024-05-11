def generate_code_variations(code):
  """
  Generates all possible variations of a secret agent code based on neighbor connections.

  Args:
      code: A string representing the code with possible digit variations.

  Returns:
      A list of strings containing all valid code variations.
  """
  variations = []
  for i, digit in enumerate(code):
    neighbor_values = get_neighbor_values(digit)
    # Special case: Handle leading zeros with neighbor values
    if digit == '0' and i == 0:
      neighbor_values = [''] + neighbor_values  # Add empty string for leading zero
    
    # Base case: No variations for single-digit code
    if len(code) == 1:
      variations.extend(neighbor_values)
      return variations
    
    # Recursive case: Generate variations for each digit and its neighbors
    next_digits = code[i+1:]
    next_variations = generate_code_variations(next_digits)
    for neighbor in neighbor_values:
      for variation in next_variations:
        variations.append(neighbor + variation)
  return variations

def get_neighbor_values(digit):
  """
  Returns a list of possible values for a digit based on neighbor connections.

  Args:
      digit: A character representing the digit in the code.

  Returns:
      A list of strings containing possible neighbor values.
  """
  neighbors = {
      '0': ['8'],
      '1': ['0', '2', '4'],
      '2': ['1', '3', '5'],
      '3': ['2', '4', '6'],
      '4': ['1', '3', '5', '7'],
      '5': ['2', '4', '6', '8'],
      '6': ['3', '5', '7', '9'],
      '7': ['4', '6', '8'],
      '8': ['0', '5', '9'],
      '9': ['6', '8']
  }
  return neighbors.get(digit, [])

code = str(input())
variations = generate_code_variations(code)
print(variations)
