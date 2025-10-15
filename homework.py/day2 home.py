Para= """Python is an interpreted, high-level and general-purpose programming language.
It is an object-oriented language too, which simply means it can model entities in the real world.
It has a simple, clean syntax, object encapsulation, good library support, and optional named parameters.
It was created by Guido van Rossum and was first released in 1991.Python emphasizes the readability of code
with its notable use of significant whitespace or indentation."""

length = len(Para)
print("length of Para", length)

First_char = Para[0]
Last_char = Para[-1]

print("First character:", First_char)
print("Last character:", Last_char)

preview = Para[:50]
print("preview(first 50 chars):", preview)


Para_caps = Para.replace("Python", "PYTHON")
print(Para_caps)

para_lower = Para.lower()
print(para_lower)

Para_strip = Para.strip()
print(Para_strip)

words_list = Para_strip.split()
print(words_list)

if "course" in Para:
    print("the word  'course' found in the Para.")

final_message = "The course description is {} characters long and has {} words.".format(len(Para_strip), len(words_list))
print(final_message)