print("new file now")
print("one more")
print("hello")
# Intentionally check for the use of an undefined variable 'test' for a specific test case,
# catching and logging the resultant name error.
try:
    # The following line uses an undefined variable 'test' as part of a specific test case.
    print(test)
except NameError as e:
    print(f"Caught an exception: {e}")
