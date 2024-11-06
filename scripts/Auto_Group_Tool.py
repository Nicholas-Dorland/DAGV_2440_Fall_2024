import maya.cmds as cmds

#Get the selection
sels = cmds.ls(sl=True)[0] + "_Grp"

#Group the selection
sels = cmds.group(n=sels)
print(sels)

#Select the Handler

#Calculate the Center
    #Move the Handler

#obj = cmds.polySphere90[0]
#name = "Bob"
#age = 60
#newString = name + " is turning " + str(age) + " years old!!!"
#obj = cmds.rename(obj, newString)

import maya.cmds as cmds 
def group_selected_objects(): 
    # Get the currently selected objects 
    selected_objects = cmds.ls(selection=True) 
    # Loop through each selected object 
    for obj in selected_objects: 
        # Get the transformation values of the object 
        translation = cmds.xform(obj, query=True, translation=True, worldSpace=True) 
        rotation = cmds.xform(obj, query=True, rotation=True, worldSpace=True) 
        # Create a new group 
        group_name = f"{obj}_Grp" 
        new_group = cmds.group(empty=True, name=group_name) 
        # Move and rotate the group to match the selected object 
        cmds.xform(new_group, translation=translation, worldSpace=True) 
        cmds.xform(new_group, rotation=rotation, worldSpace=True) 
        # Parent the object to the new group 
        cmds.parent(obj, new_group) 
        # Output the group name for confirmation 
        print(f"Created group: {new_group}") 
# Run the function 
group_selected_objects()