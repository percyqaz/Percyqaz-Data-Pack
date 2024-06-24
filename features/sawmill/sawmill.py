import os

def craft_stairs(plank, stair):
    return {
        "type": "minecraft:stonecutting",
        "ingredient": {
            "item": plank
        },
        "result": { 
            "id": stair,
            "count": 1
        }
    }

def craft_slabs(plank, slab):
    return {
        "type": "minecraft:stonecutting",
        "ingredient": {
            "item": plank
        },
        "result": { 
            "id": slab,
            "count": 2
        }
    }

def craft_fence(plank, fence):
    return {
        "type": "minecraft:stonecutting",
        "ingredient": {
            "item": plank
        },
        "result": { 
            "id": fence,
            "count": 1
        }
    }

def craft_fence_gate(plank, gate):
    return {
        "type": "minecraft:stonecutting",
        "ingredient": {
            "item": plank
        },
        "result": { 
            "id": gate,
            "count": 1
        }
    }

def craft_trapdoor(plank, trapdoor):
    return {
        "type": "minecraft:stonecutting",
        "ingredient": {
            "item": plank
        },
        "result": { 
            "id": trapdoor,
            "count": 1
        }
    }

def main(pack):
    for wood in ["oak", "birch", "spruce", "jungle", "acacia", "dark_oak", "crimson", "warped", "mangrove", "cherry", "bamboo"]:
        pack.write_json(craft_stairs("minecraft:" + wood + "_planks", "minecraft:" + wood + "_stairs"), "data/percyqaz/recipe/sawmill_" + wood + "_stairs.json")
        pack.write_json(craft_slabs("minecraft:" + wood + "_planks", "minecraft:" + wood + "_slab"), "data/percyqaz/recipe/sawmill_" + wood + "_slabs.json")
        pack.write_json(craft_fence("minecraft:" + wood + "_planks", "minecraft:" + wood + "_fence"), "data/percyqaz/recipe/sawmill_" + wood + "_fence.json")
        pack.write_json(craft_fence_gate("minecraft:" + wood + "_planks", "minecraft:" + wood + "_fence_gate"), "data/percyqaz/recipe/sawmill_" + wood + "_fence_gate.json")
        pack.write_json(craft_trapdoor("minecraft:" + wood + "_planks", "minecraft:" + wood + "_trapdoor"), "data/percyqaz/recipe/sawmill_" + wood + "_trapdoor.json")