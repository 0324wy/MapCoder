import re

def ensure_xml_structure(response: str) -> str:
    # Define the required structure in the correct order
    expected_structure = [
        "<root>",
        "<problem>",
        "<description>",
        "</description>",
        "<code>",
        "</code>",
        "<planning>",
        "</planning>",
        "</problem>",
        "<algorithm>",
        "</algorithm>",
        "</root>"
    ]

    # # Ensure response starts with <root> and ends with </root>
    # if not response.strip().startswith("<root>"):
    #     response = "<root>\n" + response
    # if not response.strip().endswith("</root>"):
    #     response += "\n</root>"

    # Add missing tags in the correct order
    for i, tag in enumerate(expected_structure):
        # Check if tag is missing by searching for each tag in sequence
        if not re.search(re.escape(tag), response):
            # Insert missing opening tags at the beginning and closing tags at the end in correct order
            if tag.startswith("</"):
                response += f"\n{tag}"
            else:
                response = f"{tag}\n" + response

    # Ensure the order of closing tags at the end
    # response = re.sub(r"</algorithm>\s*</root>$", "", response)  # Remove misplaced endings if any
    # response += "\n</algorithm>\n</root>"

    return response
  


text = """<root>
<problem>
<description>
# Problem 1: Find the maximum sum of a subarray within an array.
Given an array of integers, find the maximum sum of a subarray within that array.
</description>
<code>
# Step 1: Initialize variables to store the maximum sum and the current sum.
max_sum = float('-inf')
current_sum = 0

# Step 2: Iterate over the array to calculate the maximum sum.
for num in array:
    # Step 3: Update the current sum by adding the current number.
    current_sum = max(num, current_sum + num)
    
    # Step 4: Update the maximum sum if the current sum is greater.
    max_sum = max(max_sum, current_sum)

# Step 5: Return the maximum sum.
return max_sum

# Python3 code to solve the problem
def max_subarray_sum(array):
    max_sum = float('-inf')
    current_sum = 0
    for num in array:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Test the function
array = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray_sum(array))  # Output: 7
</code>
<planning>
# Planning to solve the problem:
1. Initialize variables to store the maximum sum and the current sum.
2. Iterate over the array to calculate the maximum sum.
3. Update the current sum by adding the current number.
4. Update the maximum sum if the current sum is greater.
5. Return the maximum sum.
</planning>
</problem>

<problem>
<description>
# Problem 2: Find the first duplicate in an array.
Given an array of integers, find the first duplicate in the array.
</description>
<code>
# Step 1: Initialize an empty set to store unique elements.
unique_elements = set()

# Step 2: Iterate over the array to find the first duplicate.
for num in array:
    # Step 3: If the number is already in the set, it's a duplicate.
    if num in unique_elements:
        return num
    # Step 4: Add the number to the set.
    unique_elements.add(num)

# Step 5: If no duplicates are found, return None.
return None

# Python3 code to solve the problem
def first_duplicate(array):
    unique_elements = set()
    for num in array:
        if num in unique_elements:
            return num
        unique_elements.add(num)
    return None

# Test the function
array = [2, 1, 3, 5, 3, 2]
print(first_duplicate(array))  # Output: 3
</code>
<planning>
# Planning to solve the problem:
1. Initialize an empty set to store unique elements.
2. Iterate over the array to find the first duplicate.
3. If the number is already in the set, it's a duplicate.
4. Add the number to the set.
5. If no duplicates are found, return None.
</planning>
</problem>

<problem>
<description>
# Problem 3: Find the longest common prefix among strings in an array.
Given an array of strings, find the longest common prefix among all strings.
</description>
<code>
# Step 1: Sort the array of strings.
array.sort()

# Step 2: Compare the first and last strings to find the common prefix.
common_prefix = ''
for chars in zip(array[0], array[-1]):
    # Step 3: If the characters match, add them to the common prefix.
    if chars[0] == chars[1]:
        common_prefix += chars[0]
    # Step 4: If the characters don't match, break the loop.
    else:
        break

# Step 5: Return the common prefix.
return common_prefix

# Python3 code to solve the problem
def longest_common_prefix(array):
    array.sort()
    common_prefix = ''
    for chars in zip(array[0], array[-1]):
        if chars[0] == chars[1]:
            common_prefix += chars[0]
        else:
            break
    return common_prefix

# Test the function
array = ['flower', 'flow', 'flight']
print(longest_common_prefix(array))  # Output: 'fl'
</code>
<planning>
# Planning to solve the problem:
1. Sort the array of strings.
2. Compare the first and last strings to find the common prefix.
3. If the characters match, add them to the common prefix.
4. If the characters don't match, break the loop.
5. Return the common prefix.
</planning>
</problem>

<algorithm>
# Algorithm: Kadane's Algorithm
Kadane's Algorithm is a dynamic programming algorithm used to find the maximum sum of a subarray within an array. It works by iterating over the array and at each step, it decides whether to include the current number in the subarray or start a new subarray.

# Tutorial:
## Step 1: Initialize variables
Initialize variables to store the maximum sum and the current sum.

## Step 2: Iterate over the array
Iterate over the array to calculate the maximum sum.

## Step 3: Update the current sum
Update the current sum by adding the current number.

## Step 4: Update the maximum sum
Update the maximum sum if the current sum is greater.

## Step 5: Return the maximum sum
Return the maximum sum.

## Time complexity:
The time complexity of Kadane's Algorithm is O(n), where n is the number of elements in the array.

## Space complexity:
The space complexity of Kadane's Algorithm is O(1), as it only uses a constant amount of space to store the maximum sum and the current sum.

## Example use cases:
Kadane's Algorithm can be used to find the maximum sum of a subarray within an array, which has many practical applications in finance, data analysis, and machine learning.

## Variations:
There are several variations of Kadane's Algorithm, including the "Maximum Subarray Problem" and the "Maximum Subsequence Problem".

## Advantages:
Kadane's Algorithm has several advantages, including its simplicity, efficiency, and ability to handle large datasets.

## Disadvantages:
Kadane's Algorithm has several disadvantages, including its sensitivity to outliers and its inability to handle non-numeric data.

## Real-world applications:
Kadane's Algorithm has many real-world applications, including:

* Financial analysis: to find the maximum sum of a subarray within a stock price array.
* Data analysis: to find the maximum sum of a subarray within a dataset.
* Machine learning: to find the maximum sum of a subarray within a feature array.

## Conclusion:
Kadane's Algorithm is a powerful dynamic programming algorithm used to find the maximum sum of a subarray within an array. Its simplicity, efficiency, and ability to handle large datasets make it a popular choice in many fields. However, its sensitivity to outliers and inability to handle non-numeric data are its main disadvantages."""

print(ensure_xml_structure(text))