file_name = "misc100"

with open(file_name, "rb") as f:
    data_lines = f.read()

data_lines = data_lines.replace(b"lovelive!", b"")

#data_lines = data_lines.replace(b"l", b"").replace(b"o", b"").replace(b"v", b"").replace(b"e", b"").replace(b"i", b"").replace(b"!", b"")

#replace_char = ["l", "o", "v", "e", "i", "!"]
#print(len(replace_char))

#for i in replace_char:
    #data_lines = data_lines.replace(i, "")

with open(file_name, "wb") as f:
    f.write(data_lines)
