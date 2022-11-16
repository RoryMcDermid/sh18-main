hours = 0
minutes = 0

output = open("text.txt", "w")

output.write(f"00_00 DECIMAL(9,6) NOT NULL,\n")
while(hours < 24):
    minutes = (minutes + 15) % 60
    if(minutes == 0):
        hours += 1
    if hours == 24:
        break
    if(hours < 10):
        output.write(f"0{hours}")
    else:
        output.write(f"{hours}")

    if(minutes == 0):
        output.write(f"_00 DECIMAL(9,6) NOT NULL,\n")
    else:
        output.write(f"_{minutes} DECIMAL(9,6) NOT NULL,\n")

output.close()