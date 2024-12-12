import maya.cmds as cmds

def rename_sequentially(name):
    sels = cmds.ls(sl=True)

    #Setup: rpartition twice to isolate the #'s and calculate based off of that
    working = name.rpartition("_")[0]
    working = working.rpartition("_")[2]
    pad = len(working)
    count = 1

    #Rename each object using information provided earlier
    for obj in sels:
        new_name = name.replace(working, str(count).zfill(pad))
        count += 1
        cmds.rename(obj, new_name)

class SequentialRenamerUI:
    #Initialize the window class
    def __init__(self):
        self.window = "renamerUI"
        
        if cmds.window(self.window, ex=True):
            cmds.deleteUI(self.window)
        
        #Setup text layout
        self.window = cmds.window(self.window, t="Sequential Renamer", wh=(300, 100))
        self.layout = cmds.columnLayout(adj=True)
        
        cmds.text(l="Enter naming format:")
        self.name_field = cmds.textField(pht="Name_##_NodeType")
        
        #Setup button and its command
        cmds.button(l="Rename", c=self.rename_callback)
        
        cmds.showWindow(self.window)
    
    #The command to call back to the rename function
    def rename_callback(self, *args):
        name_format = cmds.textField(self.name_field, query=True, text=True)
        rename_sequentially(name_format)

SequentialRenamerUI()
