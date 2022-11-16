hours = 0
minutes = 0

output = open("text2.txt", "w")

count = 0
while(hours < 24):
    minutes = (minutes + 15) % 60
    if(minutes == 0):
        hours += 1
    if hours == 24:
        break
    count += 1
    if(hours < 10):
        output.write(f"0{hours}")
    else:
        output.write(f"{hours}")

    if(minutes == 0):
        output.write(f"_00,")
    else:
        output.write(f"_{minutes},")

output.close()

print(count)

