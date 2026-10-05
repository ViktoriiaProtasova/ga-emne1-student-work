from pathlib import  Path

packing_list = ["passport", "clothes", "toothbrush", "phone charger", "sunglasses", "shoes"]

packing_list_path = Path("..") / "data" / "packing_list.txt"

with open(packing_list_path, "w", encoding="utf-8") as file:
    for thing in packing_list:
        file.write(f"{thing}\n")