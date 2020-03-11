

def print_lol (the_list):
  for m in the_list:
    if isinstance(m, list):
      print_lol(m)
    else:
      print(m)

