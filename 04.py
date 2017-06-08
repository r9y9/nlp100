s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = s.split(" ")
foo = [(words[idx - 1][0], idx) for idx in [1, 5, 6, 7, 8, 9, 15, 16, 19]]
bar = [(words[idx - 1][:2], idx)
       for idx in [2, 3, 4, 10, 11, 12, 13, 14, 17, 18, 20]]
foobar = {x: y for (x, y) in foo + bar}
print(foobar)
