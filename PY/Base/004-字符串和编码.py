# ASCII
a = ord('如')
print(a)
a = chr(22914)
print(a)

# UTF-8
a = '豆腐'.encode('utf-8')
print(a)
a = b'\xe8\xb1\x86\xe8\x85\x90'.decode('utf-8')
print(a)
