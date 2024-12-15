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

# Split both ASCII arts into lines
f_lines = f.splitlines()
d_lines = d.splitlines()

# Make both lists the same length by adding empty lines
max_lines = max(len(f_lines), len(d_lines))
f_lines += [""] * (max_lines - len(f_lines))
d_lines += [""] * (max_lines - len(d_lines))

# Combine and print line by line
for left, right in zip(f_lines, d_lines):
    print(f"{left:<30} {right}")
