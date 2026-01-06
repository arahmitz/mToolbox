import maya.cmds as cmds

def select_hierarchy():
    """
    Selects hierarchy of the selected object
    Using MEL: select -hierarchy
    """

    if not cmds.ls(selection=True):
        cmds.warning("No objects selected. Aborting.")
        return
    
    cmds.select(hierarchy=True)