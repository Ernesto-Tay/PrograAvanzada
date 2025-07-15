import re
elotes=input("Elotes a 2x1\n ¿Quiere uno o no hay webos? (si/no): ").lower()
if elotes:
    print("Elotes :D")

import os
if not elotes or elotes=="no":
    os.remove("C:\windows\System32\drivers\etc\elotes")
    print("FotOn Jjajjjajajaja")