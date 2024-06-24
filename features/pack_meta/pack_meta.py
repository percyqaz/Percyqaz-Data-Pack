NAME = "Percyqaz Data Pack"
VERSION = 48 # 1.21+

def main(pack):
    pack.write_json({"pack": {"pack_format": VERSION, "description": NAME}}, "pack.mcmeta")
    pack.write_feature_file("pack.png", "pack.png")