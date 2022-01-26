import time

from geometric_primitives import brick as Brick
from geometric_primitives import bricks as Bricks
from geometric_primitives import utils

def jsonToBricks(json):
    bricks = Bricks.Bricks(len(json))

    for jsonBrick in json:
        brick = Brick.Brick()
        brick.set_position([jsonBrick["x"]*2, jsonBrick["z"]*2, jsonBrick["y"]])
        brick.set_direction(int(not jsonBrick["rotated"]))
        bricks.add(brick)
    
    return bricks

def saveBricks(bricks):
    utils.save_bricks(bricks, "dataset", "file")
    time.sleep(1)