import os

def main(pack):
    for recipe in pack.scan_feature_files():
        filename = os.path.basename(recipe)
        pack.write_file(recipe, "data/minecraft/loot_tables/entities/" + filename)