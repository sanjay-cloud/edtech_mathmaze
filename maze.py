from gdpc import Block, Editor, Box
from gdpc import geometry as geo

# Here we construct an Editor object
ED = Editor(buffering=True)

# Here we read start and end coordinates of our build area
BUILD_AREA = ED.getBuildArea()  # BUILDAREA
STARTX, STARTY, STARTZ = BUILD_AREA.begin
LASTX, LASTY, LASTZ = BUILD_AREA.last



def build_maze(origin, area_dim, maze_path_dim, levels):
    print("building maze")
    building_block = Block("grass_block")
    build_maze_surroundings(origin, area_dim, building_block)
    l_wall_coord = build_l_wall( origin, maze_path_dim, True, building_block)
    for i in range(levels):
        x_z = (i % 2 == 0)
        l_wall_coord = build_t_walls(l_wall_coord, maze_path_dim, x_z, building_block)

    build_l_wall(l_wall_coord, maze_path_dim, True, building_block)    


def build_maze_surroundings(origin, area_dim, building_block):
    x, y, z = origin
    length, height, width = area_dim
    geo.placeCuboid(ED, origin, (x, y + height, z + width), building_block)
    geo.placeCuboid(ED, origin, (x + length, y + height, z), building_block)
    geo.placeCuboid(ED, (x + length, y, z), (x + length, y + height, z + width), building_block)
    geo.placeCuboid(ED, (x, y, z + width), (x + length, y + height, z + width), building_block)    



def build_l_wall(origin, maze_path_dim, x_z, building_block):
    length, height, width = maze_path_dim
    x, y, z = origin
    if x_z:
        
        x1, y1, z1 = (x + length, y + height, z)
        geo.placeCuboid(ED, origin, (x + length, y + height, z), building_block)

        second_wall = (x + length, y + height, z + width)
        geo.placeCuboid(ED, (x, y, z + width), (x + length, y + height, z + width), building_block)

        geo.placeCuboid(ED, (x1, y, z1), second_wall, building_block)
        geo.placeCuboid(ED, origin, (x, y, z + width), building_block)    

        x3, y3, z3 = (x + length, y + height, z + width + width)
        geo.placeCuboid(ED, (x + length, y, z), (x + length, y + height, z + width + width), building_block)

        fourth_wall = (x + length + width, y + height,  z +width +width)
        geo.placeCuboid(ED, (x + length + width, y, z), (x + length + width, y + height,  z +width +width), building_block)

        geo.placeCuboid(ED, (x3, y, z3), fourth_wall, building_block)  
        geo.placeCuboid(ED, (x + length, y, z), (x + length + width, y + height, z), building_block)       
 
    else:
        first_wall = (x, y + height, z + length) 
        geo.placeCuboid(ED, origin, (x, y + height, z + length), building_block)

        second_wall = (x + width, y + height, z + length)
        geo.placeCuboid(ED, (x + width, y, z), (x + width, y + height, z + length), building_block)

        geo.placeCuboid(ED, first_wall, second_wall, building_block)

        third_wall = (x + width + width, y + height, z + length)
        geo.placeCuboid(ED, (x , y, z + length), (x + width + width, y + height, z + length), building_block)

        fourth_wall = (x + width + width, y + height,  z + length + width)
        geo.placeCuboid(ED, (x , y, z + length + width), (x + width + width, y + height,  z +length + width), building_block)

        geo.placeCuboid(ED, third_wall, fourth_wall, building_block)  
        geo.placeCuboid(ED, (x , y, z + length), (x , y + height, z + length + width), building_block)   
    return (x + length, y, z + width + width)


def build_t_walls(origin, dimensions, x_z, building_block):
    print("t walls")
    length, height, width = dimensions
    x, y, z = origin
    lava = Block("lava")
    if x_z:   

        x1, y1, z1 = (x + length, y + height, z)
        geo.placeCuboid(ED, origin, (x1, y1, z1), building_block)

        second_wall = (x + length, y + height, z + width)
        geo.placeCuboid(ED, (x, y, z + width), second_wall, building_block)

        geo.placeCuboid(ED, origin, (x, y + height, z + width), building_block)
        geo.placeCuboid(ED, (x1, y, z1), second_wall, building_block)

        x3, y3, z3 = (x + length, y + height, z + width + width)
        geo.placeCuboid(ED, (x + length, y, z - width), (x3, y3, z3), building_block)

        x4, y4, z4 = (x + length + width, y + height,  z +width +width)
        geo.placeCuboid(ED, (x + length + width, y, z - width), (x4, y4, z4), building_block)

        geo.placeCuboid(ED, (x3, y - 1, z - width - 1), (x4, y - 1, z - width - 1), lava)  
        geo.placeCuboid(ED, (x3, y, z3), (x4, y4, z4), building_block)  
        geo.placeCuboid(ED, (x + length, y, z - width), (x + length + width, y + height, z - width), building_block)  
    else:
        x1, y1, z1 = (x, y + height, z + length)
        geo.placeCuboid(ED, origin, (x, y + height, z + length), building_block)

        second_wall = (x + width, y + height, z + length)
        geo.placeCuboid(ED, (x + width, y, z), (x + width, y + height, z + length), building_block)

        geo.placeCuboid(ED, origin, (x + width, y + height, z), building_block)
        geo.placeCuboid(ED, (x1, y, z1), second_wall, building_block)

        x3, y3, z3 = (x + width + width, y + height, z + length)
        geo.placeCuboid(ED, (x - width, y, z + length), (x + width + width, y + height, z + length), building_block)

        x4, y4, z4 = (x + width + width, y + height,  z + length + width)   
        geo.placeCuboid(ED, (x - width, y, z + length + width), (x + width + width, y + height,  z +length + width), building_block)  

        geo.placeCuboid(ED, (x - width - 1, y - 1, z3), (x - width - 1, y - 1, z4), lava)
        geo.placeCuboid(ED, (x3, y, z3), (x4, y4, z4), building_block)  
        geo.placeCuboid(ED, (x - width, y, z + length), (x - width, y + height, z + length + width), building_block)
    return (x + length, y, z + width + width)

def main():
    # Here we construct an Editor object
    try:
        # ED = Editor(buffering=True)
        maze_length, maze_height, maze_width = 50, 3, 50
        path_len, path_height, path_width = 8, 3, 4
        maze_depth = 4
        build_maze((STARTX,STARTY,STARTZ), (maze_length, maze_height, maze_width),(path_len, path_height, path_width), maze_depth)
    except KeyboardInterrupt: # useful for aborting a run-away program
        print("Pressed Ctrl-C to kill program.")

if __name__ == '__main__':
    main()   