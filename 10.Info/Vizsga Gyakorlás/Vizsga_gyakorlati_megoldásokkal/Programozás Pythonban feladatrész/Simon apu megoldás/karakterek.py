szo=None
while szo !="":
    szo= input("Adjon meg mondatot, vagy szót. Az ENTER lenyomásával tud továbbhaladni!")
    lines = file.readline()
    for i in range(0, len(szo)):
        munkatarsak.append(Munkatarsak(lines[i]))


