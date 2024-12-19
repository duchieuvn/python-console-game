import os
import time
f = r"""
       _     _
      (')-=-(')
    __(   "   )__
   /00/'-----'\00\
___\\0\\     //0//___
>%%%%)/_\---/_\(%%%%<
"""

d = r"""
   /*\__
  (****@\___
  /*********O
 /***(_____/
 /_____/   U
"""
#reference ASCII art: https://www.asciiart.eu/animals/dogs

# # Split both ASCII arts into lines
# f_lines = f.splitlines()
# d_lines = d.splitlines()

# # Make both lists the same length by adding empty lines
# max_lines = max(len(f_lines), len(d_lines))
# f_lines += [""] * (max_lines - len(f_lines))
# d_lines += [""] * (max_lines - len(d_lines))

# # Combine and print line by line
# for left, right in zip(f_lines, d_lines):
#     print(f"{left:<30} {right}")

def print_at_position(ascii_art, row, col):
    lines = ascii_art.splitlines()  # Split ASCII art into lines
    
    for i, line in enumerate(lines):
        print(f"\033[{row + i};{col}H{line}", end="")  # Move cursor and print each line
    print("\033[0;0H")  # Reset cursor position to top-left

x = 5  # Row
y = 10  # Column

for i in range(20):
   print_at_position(d, x, y+i)
   time.sleep(0.2)
   os.system('cls')