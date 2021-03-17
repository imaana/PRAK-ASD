def cetak(n):
  for x in range(1, n+1):
      if x % 3 == 0 and x % 5 == 0:
          print("Python UMS")
      elif x % 3 == 0:
          print('Python')
      elif x % 5 == 0:
          print('UMS')
      else:
          print(str(x))
