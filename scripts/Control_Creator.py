import maya.cmds as cmds 

def group_selected_objects():
    #Get the currently selected objects
    sels = cmds.ls(sl=True)
    #Loop through each selected object
    for obj in sels:                                                #}->Provided by Microsoft's Copilot
        #Get the transformation values of the object                #}
        translation = cmds.xform(obj, q=True, t=True, ws=True)      #}
        rotation = cmds.xform(obj, q=True, ro=True, ws=True)        #}
        #Create a new group                                         #}
        group_name = obj + "_Grp"                                   #}
        new_group = cmds.group(em=True, n=group_name)               #}
        #Move and rotate the group to match the selected object
        cmds.xform(new_group, t=translation, ws=True)
        cmds.xform(new_group, ro=rotation, ws=True)
        #Parent the object to the new group
        cmds.parent(obj, new_group)
        #Output the group name for confirmation
        print("Created group: " + new_group)
#Run the function
group_selected_objects()

#String Manipulation
#Google "Python String Documentation"
#rsplit or rpartition works well
#   rPartition[0] + "_Grp"
#
#
#
#
#