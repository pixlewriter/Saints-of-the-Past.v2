def toggle(bool):
  if bool == True:
    bool = False
    print(bool)
    return bool
  elif bool == False:
    bool = True
    return bool
  else:
    print(f"Bool cannot be turned into a bool: {bool}")
  return bool