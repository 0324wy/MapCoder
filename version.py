import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))  # Check the name of the first GPU

from openai import OpenAI
import re

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
    timeout=60*5
)

text = '''## Modified Planning:

1. **Divide the problem**: Break down the problem into smaller subproblems.
   - The problem can be divided into two subproblems: encoding and decoding.
   - The encoding subproblem involves cycling groups of three characters in the input string.
   - The decoding subproblem involves reversing the groups of three characters in the encoded string.

2. **Overlapping subproblems**: Identify if the subproblems have overlapping solutions.
   - The subproblems have overlapping solutions because the encoded string can be decoded back to the original string.

3. **Memoization**: Store the solutions to subproblems in a memory-based data structure (e.g., array, hash table).
   - We can use a 2D array to store the lengths of common subsequences in the longest common subsequence function.

4. **Bottom-up approach**: Start with the smallest subproblems and build up to the original problem.
   - We can start by calculating the lengths of common subsequences for smaller substrings and then build up to the original strings.

5. **Optimization**: Use dynamic programming to avoid redundant computation and improve performance.
   - We can use dynamic programming to avoid redundant computation by storing the lengths of common subsequences in a 2D array.

6. **Correct the decode_cyclic function**: The decode_cyclic function is not correctly reversing the groups of three characters.
   - We can fix this by changing the line `groups = [group[2] + group[:2] for group in groups]` to `groups = [group[2] + group[:2] for group in groups if len(group) == 3 else group]`.

7. **Add test cases**: Add test cases to ensure that the functions are working correctly.

## Modified Code:

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group[2] + group[:2] for group in groups if len(group) == 3 else group]
    return "".join(groups)


def test_encode_cyclic():
    assert encode_cyclic('abc') == 'bca'
    assert encode_cyclic('abcabc') == 'bcaabc'


def test_decode_cyclic():
    assert decode_cyclic(encode_cyclic('abc')) == 'abc'
    assert decode_cyclic(encode_cyclic('abcabc')) == 'abcabc'


def test_encode_decode():
    for _ in range(100):
        s = ''.join(random.choice('abc') for _ in range(10))
        encoded = encode_cyclic(s)
        decoded = decode_cyclic(encoded)
        assert s == decoded


import random
test_encode_cyclic()
test_decode_cyclic()
test_encode_decode()
```

However, the above code still has issues with the decode_cyclic function. The issue is that the decode_cyclic function is not correctly reversing the groups of three characters.

## Modified Planning:

1. **Divide the problem**: Break down the problem into smaller subproblems.
   - The problem can be divided into two subproblems: encoding and decoding.
   - The encoding subproblem involves cycling groups of three characters in the input string.
   - The decoding subproblem involves reversing the groups of three characters in the encoded string.

2. **Overlapping subproblems**: Identify if the subproblems have overlapping solutions.
   - The subproblems have overlapping solutions because the encoded string can be decoded back to the original string.

3. **Memoization**: Store the solutions to subproblems in a memory-based data structure (e.g., array, hash table).
   - We can use a 2D array to store the lengths of common subsequences in the longest common subsequence function.

4. **Bottom-up approach**: Start with the smallest subproblems and build up to the original problem.
   - We can start by calculating the lengths of common subsequences for smaller substrings and then build up to the original strings.

5. **Optimization**: Use dynamic programming to avoid redundant computation and improve performance.
   - We can use dynamic programming to avoid redundant computation by storing the lengths of common subsequences in a 2D array.

6. **Correct the decode_cyclic function**: The decode_cyclic function is not correctly reversing the groups of three characters.
   - We can fix this by changing the line `groups = [group[2] + group[:2] for group in groups if len(group) == 3 else group]` to `groups = [group[2] + group[:2] for group in groups]`.

7. **Add test cases**: Add test cases to ensure that the functions are working correctly.

## Modified Code:

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group[2] + group[:2] for group in groups]
    return "".join(groups)


def test_encode_cyclic():
    assert encode_cyclic('abc') == 'bca'
    assert encode_cyclic('abcabc') == 'bcaabc'


def test_decode_cyclic():
    assert decode_cyclic(encode_cyclic('abc')) == 'abc'
    assert decode_cyclic(encode_cyclic('abcabc')) == 'abcabc'


def test_encode_decode():
    for _ in range(100):
        s = ''.join(random.choice('abc') for _ in range(10))
        encoded = encode_cyclic(s)
        decoded = decode_cyclic(encoded)
        assert s == decoded


import random
test_encode_cyclic()
test_decode_cyclic()
test_encode_decode()
```

However, the above code still has issues with the decode_cyclic function. The issue is that the decode_cyclic function is not correctly reversing the groups of three characters.

## Modified Planning:

1. **Divide the problem**: Break down the problem into smaller subproblems.
   - The problem can be divided into two subproblems: encoding and decoding.
   - The encoding subproblem involves cycling groups of three characters in the input string.
   - The decoding subproblem involves reversing the groups of three characters in the encoded string.

2. **Overlapping subproblems**: Identify if the subproblems have overlapping solutions.
   - The subproblems have overlapping solutions because the encoded string can be decoded back to the original string.

3. **Memoization**: Store the solutions to subproblems in a memory-based data structure (e.g., array, hash table).
   - We can use a 2D array to store the lengths of common subsequences in the longest common subsequence function.

4. **Bottom-up approach**: Start with the smallest subproblems and build up to the original problem.
   - We can start by calculating the lengths of common subsequences for smaller substrings and then build up to the original strings.

5. **Optimization**: Use dynamic programming to avoid redundant computation and improve performance.
   - We can use dynamic programming to avoid redundant computation by storing the lengths of common subsequences in a 2D array.

6. **Correct the decode_cyclic function**: The decode_cyclic function is not correctly reversing the groups of three characters.
   - We can fix this by changing the line `groups = [group[2] + group[:2] for group in groups]` to `groups = [group[2] + group[:2] for group in groups if len(group) == 3 else group]`.

7. **Add test cases**: Add test cases to ensure that the functions are working correctly.

## Modified Code:

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group[2] + group[:2] for group in groups if len(group) == 3 else group]
    return "".join(groups)


def test_encode_cyclic():
    assert encode_cyclic('abc') == 'bca'
    assert encode_cyclic('abcabc') == 'bcaabc'


def test_decode_cyclic():
    assert decode_cyclic(encode_cyclic('abc')) == 'abc'
    assert decode_cyclic(encode_cyclic('abcabc')) == 'abcabc'


def test_encode_decode():
    for _ in range(100):
        s = ''.join(random.choice('abc') for _ in range(10))
        encoded = encode_cyclic(s)
        decoded = decode_cyclic(encoded)
        assert s == decoded


import random
test_encode_cyclic()
test_decode_cyclic()
test_encode_decode()
```

However, the above code still has issues with the decode_cyclic function. The issue is that the decode_cyclic function is not correctly reversing the groups of three characters.

## Modified Planning:

1. **Divide the problem**: Break down the problem into smaller subproblems.
   - The problem can be divided into two subproblems: encoding and decoding.
   - The encoding subproblem involves cycling groups of three characters in the input string.
   - The decoding subproblem involves reversing the groups of three characters in the encoded string.

2. **Overlapping subproblems**: Identify if the subproblems have overlapping solutions.
   - The subproblems have overlapping solutions because the encoded string can be decoded back to the original string.

3. **Memoization**: Store the solutions to subproblems in a memory-based data structure (e.g., array, hash table).
   - We can use a 2D array to store the lengths of common subsequences in the longest common subsequence function.

4. **Bottom-up approach**: Start with the smallest subproblems and build up to the original problem.
   - We can start by calculating the lengths of common subsequences for smaller substrings and then build up to the original strings.

5. **Optimization**: Use dynamic programming to avoid redundant computation and improve performance.
   - We can use dynamic programming to avoid redundant computation by storing the lengths of common subsequences in a 2D array.

6. **Correct the decode_cyclic function**: The decode_cyclic function is not correctly reversing the groups of three characters.
   - We can fix this by changing the line `groups = [group[2] + group[:2] for group in groups if len(group) == 3 else group]` to `groups = [group[2] + group[:2] for group in groups]`.

7. **Add test cases**: Add test cases to ensure that the functions are working correctly.

## Modified Code:

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group[2] + group[:2] for group in groups]
    return "".join(groups)


def test_encode_cyclic():
    assert encode_cyclic('abc') == 'bca'
    assert encode_cyclic('abcabc') == 'bcaabc'


def test_decode_cyclic():
    assert decode_cyclic(encode_cyclic('abc')) == 'abc'
    assert decode_cyclic(encode_cyclic('abcabc')) == 'abcabc'


def test_encode_decode():
    for _ in range(100):
        s = ''.join(random.choice('abc') for _ in range(10))
        encoded = encode_cyclic(s)
        decoded = decode_cyclic(encoded)
        assert s == decoded


import random
test_encode_cyclic()
test_decode_cyclic()
test_encode_decode()
```

However, the above code still has issues with the decode_cyclic function. The issue is that the decode_cyclic function is not correctly reversing the groups of three characters.

## Modified Planning:

1. **Divide the problem**: Break down the problem into smaller subproblems.
   - The problem can be divided into two subproblems: encoding and decoding.
   - The encoding subproblem involves cycling groups of three characters in the input string.
   - The decoding subproblem involves reversing the groups of three characters in the encoded string.

2. **Overlapping subproblems**: Identify if the subproblems have overlapping solutions.
   - The subproblems have overlapping solutions because the encoded string can be decoded back to the original string.

3. **Memoization**: Store the solutions to subproblems in a memory-based data structure (e.g., array, hash table).
   - We can use a 2D array to store the lengths of common subsequences in the longest common subsequence function.

4. **Bottom-up approach**: Start with the smallest subproblems and build up to the original problem.
   - We can start by calculating the lengths of common subsequences for smaller substrings and then build up to the original strings.

5. **Optimization**: Use dynamic programming to avoid redundant computation and improve performance.
   - We can use dynamic programming to avoid redundant computation by storing the lengths of common subsequences in a 2D array.

6. **Correct the decode_cyclic function**: The decode_cyclic function is not correctly reversing the groups of three characters.
   - We can fix this by changing the line `groups = [group[2] + group[:2] for group in groups]` to `groups = [group[2] + group[:2] for group in groups if len(group) == 3 else group]`.

7. **Add test cases**: Add test cases to ensure that the functions are working correctly.

## Modified Code:

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group
    
## Modified planning:
## Modified Code:
## Modified Code:
## Modified Planning:
## Modified Planning:
## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Code:
## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Code:

## Modified Code:
## Modified Planning:

## Modified Planning:

## Modified Code:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Code:
## Modified Code:
## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Code:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Code:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Planning:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Planning:

## Modified Planning:

## Modified Code:

## Modified Planning:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Code:

## Modified Planning:

## Modified Planning:

## Modified Code:
## Modified Code:
## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified Planning:

## Modified
```
 
'''

# input_for_improving_code = [
#     {
#         "role": "user",
#         "content": text
#     }
# ]

# def chat(input_for_improving_code):
#     response = client.chat.completions.create(
#     model="meta-llama/Llama-3.1-8B-Instruct",
#     messages=input_for_improving_code
#     )
#     return response.choices[0].message.content, response.usage.prompt_tokens, response.usage.completion_tokens
  

def parse_code(response: str) -> str:
    if "```" not in response:
        return response

    code_pattern = r'```((.|\n)*?)```'
    if "```Python" in response:
        code_pattern = r'```Python((.|\n)*?)```'
    if "```Python3" in response:
        code_pattern = r'```Python3((.|\n)*?)```'
    if "```python" in response:
        code_pattern = r'```python((.|\n)*?)```'
    if "```python3" in response:
        code_pattern = r'```python3((.|\n)*?)```'
    if "```C" in response:
        code_pattern = r'```C((.|\n)*?)```'
    if "```c" in response:
        code_pattern = r'```c((.|\n)*?)```'
    if "```C++" in response:
        code_pattern = r'```C\+\+((.|\n)*?)```'
    if "```c++" in response:
        code_pattern = r'```c\+\+((.|\n)*?)```'
    if "```Java" in response:
        code_pattern = r'```Java((.|\n)*?)```'
    if "```java" in response:
        code_pattern = r'```java((.|\n)*?)```'
    if "```Node" in response:
        code_pattern = r'```Node((.|\n)*?)```'
    if "```node" in response:
        code_pattern = r'```node((.|\n)*?)```'
    if "```Rust" in response:
        code_pattern = r'```Rust((.|\n)*?)```'
    if "```rust" in response:
        code_pattern = r'```rust((.|\n)*?)```'
    if "```PHP" in response:
        code_pattern = r'```PHP((.|\n)*?)```'
    if "```php" in response:
        code_pattern = r'```php((.|\n)*?)```'
    if "```Go" in response:
        code_pattern = r'```Go((.|\n)*?)```'
    if "```go" in response:
        code_pattern = r'```go((.|\n)*?)```'
    if "```Ruby" in response:
        code_pattern = r'```Ruby((.|\n)*?)```'
    if "```ruby" in response:
        code_pattern = r'```ruby((.|\n)*?)```'
    if "```C#" in response:
        code_pattern = r'```C#((.|\n)*?)```'
    if "```c#" in response:
        code_pattern = r'```c#((.|\n)*?)```'
    if "```csharp" in response:
        code_pattern = r'```csharp((.|\n)*?)```'

    code_blocks = re.findall(code_pattern, response, re.DOTALL)

    if type(code_blocks[-1]) == tuple or type(code_blocks[-1]) == list:
        code_str = "\n".join(code_blocks[-1])
    elif type(code_blocks[-1]) == str:
        code_str = code_blocks[-1]
    else:
        code_str = response

    return code_str
  
def parse_code_(response: str) -> str:
    if "```" not in response:
        return response

    code_pattern = r'```(?:[a-zA-Z0-9#\+\-]*)\n((?:.|\n)*?)```'
    code_blocks = re.findall(code_pattern, response, re.DOTALL)

    if code_blocks:
        code_str = "\n".join(code_blocks)
    else:
        code_str = response

    return code_str
  
  
# response, _, _ = chat(input_for_improving_code)
# print(response)

print("============code==============")
# print(parse_code_(text))



def is_code_blocks_closed(text: str) -> str:
    """
    Ensures that all code blocks in the input text are properly closed with triple backticks.
    If a code block is opened but not closed, this function adds the closing triple backticks
    before the next section header or at the end of the text.
    """
    lines = text.splitlines()
    in_code_block = False

    for line in lines:
        if line.strip().startswith('```') and not in_code_block:
            in_code_block = True
        elif line.strip().startswith('```') and in_code_block:
            in_code_block = False
    return not in_code_block
  
print(is_code_blocks_closed(text))
print(parse_code(text))
  