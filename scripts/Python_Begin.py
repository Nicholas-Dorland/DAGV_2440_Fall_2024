import maya.cmds as cmds

#Create, shape, and move saucer
cmds.polySphere(sx=30, sy=5, r=1)
cmds.xform(s=[1, 0.476, 1], t=[0, 1.157, 2.160])

#Create, shape, and move body
cmds.polyCylinder()
cmds.xform(s=[0.348, 1, 0.348], ro=[90, 0, 0])

#create, shape, and move left Thruster
cmds.polyCylinder()
cmds.xform(s=[0.179, 1, 0.179], ro=[90, 0, 0], t=[1.113, 0.598, 0])

#Create, shape, and move right Thruster
cmds.polyCylinder()
cmds.xform(s=[0.179, 1, 0.179], ro=[90, 0, 0], t=[-1.113, 0.598, 0])

#Create, shape, and move Neck
cmds.polyCube()
cmds.xform(s=[0.364, 1.345, 0.357], ro=[30, 0, 0], t=[0, 0.614, 1.159])

#Create, shape, and move LT Connector
cmds.polyCube()
cmds.xform(s=[0.242, 1.226, 0.556], ro=[0, 0, -52.523], t=[0.644, 0.267, 0])

#Create, shape, and move RT Connector
cmds.polyCube()
cmds.xform(s=[0.242, 1.226, 0.556], ro=[0, 0, 52.523], t=[-0.644, 0.267, 0])