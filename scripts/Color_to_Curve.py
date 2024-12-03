import maya.cmds as cmds

def change_shape_node_color(color):
    #Define a mapping from color names to color indices - Provided by Microsoft's Copilot
    color_map = {
        "original": 0,
        "black": 1,
        "dark gray": 2,
        "light gray": 3,
        "maroon": 4,
        "dark blue": 5,
        "blue": 6,
        "dark green": 7,
        "dark purple": 8,
        "magenta": 9,
        "brown": 10,
        "light brown": 11,
        "dark brown": 12,
        "red": 13,
        "green": 14,
        "blue green": 15,
        "blueish gray": 16,
        "aqua": 17,
        "pale blue": 18,
        "dark pink": 19,
        "yellow": 20,
        "white": 21,
        "pale yellow": 22,
        "light grayish blue": 23,
        "pale green": 24,
        "light yellow": 25,
        "light peach": 26,
        "bright yellow": 27,
        "pale cyan": 28,
        "pale grayish blue": 29,
        "pale blueish green": 30,
        "dark pale grayish blue": 31,
    }
    
    
    if isinstance(color, str):
        color = color_map.get(color.lower(), 0)  # Default to color 0 (original color) if not found - Also provided by Copilot
    
    #Get the selected objects
    sels = cmds.ls(sl=True)
    
    for obj in sels:
        #List all shape nodes of the selected object
        nodes = cmds.listRelatives(obj, f=True, s=True)
        
        for shape in nodes:
            #Enable override and set the color
            cmds.setAttr(f"{shape}.overrideEnabled", 1)
            cmds.setAttr(f"{shape}.overrideColor", color)


change_shape_node_color("red")