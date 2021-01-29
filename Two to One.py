def longest(a1, a2):
  a = a1 + a2
  b = ""
  for i in a:
    if i in b:
      pass
    else:
      b += i
  b = sorted(b)
  return ''.join(b)
    

print(longest("aretheyhere", "yestheyarehere"))