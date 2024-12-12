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
        "dark brown": 11,
        "red brown": 12,
        "red": 13,
        "bright green": 14,
        "blueish gray": 15,
        "white": 16,
        "yellow": 17,
        "pale blue": 18,
        "aqua": 19,
        "pink": 20,
        "light peach": 21,
        "pale yellow": 22,
        "green": 23,
        "peach": 24,
        "light yellow": 25,
        "yellowish green": 26,
        "pale cyan": 27,
        "pale blueish green": 28,
        "pale grayish blue": 29,
        "grayish purple": 30,
        "dark magenta": 31,
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

class ColorChangerUI:
    #Initialize the window
    def __init__(self):
        self.window = "colorChangerUI"
        
        if cmds.window(self.window, ex=True):
            cmds.deleteUI(self.window)
        
        self.window = cmds.window(self.window, t="Change Shape Node Color", wh=(300, 120))
        self.layout = cmds.columnLayout(adj=True)
        
        #Set up the slider, color preview window, and button
        cmds.text(l="Select color index:")
        self.color_slider = cmds.intSlider(min=0, max=31, v=0, s=1, dc=self.update_color_preview)
        
        self.color_preview = cmds.canvas(w=275, h=40, bgc=self.get_color_rgb(0))
        
        cmds.button(l="Apply Color", c=self.apply_color)
        
        cmds.showWindow(self.window)
    
    def get_color_rgb(self, index):
        #Define RGB values for each index - provided by Microsoft's Copilot
        color_values = [
            (0.627, 0.627, 0.627), # original
            (0, 0, 0), # black
            (0.25, 0.25, 0.25), # dark gray
            (0.6, 0.6, 0.6), # light gray
            (0.75, 0.25, 0.25), # maroon
            (0.2, 0.2, 0.6), # dark blue
            (0, 0, 1), # blue
            (0, 0.4, 0), # dark green
            (0.4, 0, 0.4), # dark purple
            (0.7, 0, 0.7), # magenta
            (0.6, 0.4, 0.2), # brown
            (0.35, 0.15, 0.1), # dark brown
            (0.5, 0.25, 0), # red brown
            (1, 0, 0), # red
            (0, 1, 0), # bright green
            (0.2, 0.4, 0.7), # blueish gray
            (1, 1, 1), # white
            (1, 1, 0), # yellow
            (0.7, 0.7, 1), # pale blue
            (0, 1, 0.7), # aqua
            (1, 0.5, 0.75), # pink
            (1, 0.75, 0.5), # light peach
            (1, 1, 0.75), # pale yellow
            (0, 0.7, 0.4), # green
            (1, 0.6, 0.4), # peach
            (0.9, 0.9, 0.45), # light yellow
            (0.75, 0.9, 0), # yellowish green
            (0.6, 0.9, 0.8), # pale cyan
            (0.7, 0.8, 0.75), # pale blueish green
            (0.6, 0.7, 0.95), # pale grayish blue
            (0.6, 0.35, 0.6), # grayish purple
            (0.75, 0.1, 0.75) # dark magenta
        ]
        return color_values[index]
    
    def update_color_preview(self, index):
        rgb = self.get_color_rgb(index)
        cmds.canvas(self.color_preview, edit=True, bgc=rgb)
    
    #The command for the button
    def apply_color(self, *args):
        color_index = cmds.intSlider(self.color_slider, query=True, v=True)
        change_shape_node_color(color_index)

ColorChangerUI()