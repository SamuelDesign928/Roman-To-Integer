class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a mapping of Roman numerals to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in s:
            value = roman_to_int[char]
            if value > prev_value:
                # Handle subtraction case (e.g., IV or IX)
                total += value - 2 * prev_value
            else:
                # Handle addition case
                total += value
            prev_value = value
        
        return total
   
