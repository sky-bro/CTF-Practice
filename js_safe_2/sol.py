chs = []
chs.extend(['_', '@', '!', '?', '-'])
chs.extend(map(lambda i: chr(i+ord('0')), range(10)))
chs.extend(map(lambda i: chr(i+ord('a')), range(26)))
chs.extend(map(lambda i: chr(i+ord('A')), range(26)))
print(chs)
# print('1' in chs)

code = "¢×&Ê´cÊ¯¬$¶³´}ÍÈ´T©Ð8Í³Í|Ô÷aÈÐÝ&¨þJ"
for i in range(len(code)):
    if i%4 == 0:
        print(chr(ord(code[i]) ^ 0xfd), end="")
    if i%4 == 1:
        print(chr(ord(code[i]) ^ 0x99), end="")
    if i%4 == 2:
        print(chr(ord(code[i]) ^ 0x15), end="")
    if i%4 == 3:
        print(chr(ord(code[i]) ^ 0xf9), end="")
print()


for k in range(4):
    print(k)
    for i in range(256):
        begin = True
        for j in range(k, len(code), 4):
            if (not chr(ord(code[j]) ^ i) in chs):
                begin = False
                break
        if (begin):
            print(hex(i))