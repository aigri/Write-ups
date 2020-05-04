with open("petite_frappe_2.txt", "r") as fd:
    content = fd.readlines()

chars = {46: "l", 24:"a", 65:" ", 39:"s", 32:"o", 30:"u", 28:"t", 31:"i", 57:"n", 55:"v", 26:"e", 54:"c", 53:"x", 33:"p", 47:"m", 56:"b",
    27:"r", 38:"q", 40:"d", 59:".", 41:"f", 42:"g", 17:"_", 25:"z", 29:"y"}

pressed = []
released = []
out = ""
for line in content:
    line = line.strip()
    num = int(line[-2:])
    if num == 62:
        continue
    line = line[:-3]
    
    if line.startswith("press"): #startswitch
        if not num in chars.keys():
            print("Passing " + str(num))
        pressed.append(num)
        out += chars[num]
    elif line.startswith("release"):
        if num in pressed:
           pass
        else:
            ValueError(line)
    else:
        raise ValueError(line)

print(out)