import textwrap
sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''

prefix = '> '
text_without_Indentation = textwrap.dedent(sample_text)

# Split the string into a list of lines
lines = text_without_Indentation.splitlines()

# Filter out lines without text
lines = [line for line in lines if line.strip()]

# Add the prefix to each line
for i in range(len(lines)):
    lines[i] = prefix + lines[i]

# Join the modified lines back into a single string
modified_text = '\n'.join(lines)

print(modified_text)
