import cm2py as cm2
from math import sin, cos, floor
from pyperclip import copy

blocks = []
save = cm2.Save()
text = ""

size = int(input("Size of the circle (in Roblox studs): "))
curs, cent, conc = "","",""
while curs not in ["Y", "N"]:
    curs = input("Should it be cursed (smooth) or uncursed (on-grid)? (Y/N): ").upper()
while cent not in ["Y", "N"]:
    cent = input("Should there be a center? (Y/N): ").upper()
while conc not in ["Y", "N"]:
    conc = input("Should there be connections to the center? (MAY LAG SERVER) (Y/N): ").upper()

print("Generating...",end=" ")

for i in range(1,360,1):
    x = [sin(i)*size if curs == "Y" else floor(sin(i)*size)][0]
    y = [cos(i)*size if curs == "Y" else floor(cos(i)*size)][0]
    blocks.append(save.addBlock(cm2.AND, (x,0,y), False, None, curs == "N"))

print("Done")

if cent == "Y":
    print("Adding center...", end=" ")
    center = save.addBlock(cm2.FLIPFLOP,(0,0,0))
    print("Done")
    if conc == "Y":
        print("Adding connections...", end=" ")
        for block in blocks:
            save.addConnection(block, center)
        print("Done")

print("Exporting save...", end=" ")
text = save.exportSave()
print("Done")

print("Copying save to clipboard...", end=" ")
copy(text)
print("Done!\n")

print("Paste the text inside the register and press Enter and stamp the save to see it!")
