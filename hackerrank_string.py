#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Writef your code here
    abc=first_name.title()
    cde=last_name.title()
    print(f"Hello {abc} {cde} ! You just deployed into python")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
  
    print_full_name(first_name, last_name)