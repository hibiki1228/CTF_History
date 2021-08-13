import csv

with open('./ask.csv') as f:
  #print(f.read())
  bits = []
  for row in csv.reader(f):
    bits.append(row[0])
    
  s = ""
  c = 0
  #print(bits)
  for i in range(len(bits)):
      val = int(bits[i])
      c = (c << 1) | val
      if i % 8 == 7:
          s = s + chr(c)
          c = 0
  print(s)

# s = "WANI"
# for i in range(len(s)):
#     val = s[i]
#     for j in range(8):
#         b = (ord(val) >> (7 - j)) & 0x01
#         bits.append(b)

# print(bits)
