# Roman-To-Integer
My solution from leetcode to convert any Roman Numeral to based 10
This Python class provides a method to convert a Roman numeral string into its corresponding integer value. The solution handles both standard and subtractive notation cases, ensuring accurate conversion.

## Class and Method

### `Solution`

The `Solution` class contains the following method:

- **`romanToInt(s: str) -> int`**: Converts a Roman numeral string `s` into its integer equivalent.

### Method Details

- **Input**: A string `s` representing a Roman numeral (e.g., "IX", "MCMXCIV").
- **Output**: An integer representing the equivalent value of the Roman numeral.

### Logic

- **Mapping**: A dictionary `roman_to_int` maps each Roman numeral character to its integer value.
- **Processing**:
  - The method iterates over each character in the string.
  - For each character, it compares the current numeral's value with the previous one.
  - If the current value is greater than the previous one, it subtracts twice the previous value from the total (to account for the subtractive notation).
  - Otherwise, it simply adds the current value to the total.
- **Result**: The method returns the computed integer value.

## Example

```python
sol = Solution()
result = sol.romanToInt("MCMXCIV")
print(result)  # Output: 1994

