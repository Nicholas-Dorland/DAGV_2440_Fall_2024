import maya.cmds as cmds

def rename_sequentially(name):
    sels = cmds.ls(sl=True)

    #Setup: rpartition twice to isolate the #'s and calculate based off of that
    working = name.rpartition("_")[0]
    working = working.rpartition("_")[2]
    pad = len(working)
    count = 1

    #Remane each object using information provided earlier
    for obj in sels:
        new_name = name.replace(working, str(count).zfill(pad))
        count += 1
        cmds.rename(obj, new_name)

# Example usage: rename selected objects to "Leg_##_Jnt"
rename_sequentially("Left_And_Right_Arm_##_Geo")