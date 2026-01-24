import maya.cmds as cmds

def get_selection(action_name="Operation"):
    """
    Return the current selection in Maya
    Warn and return None if nothing is selected
    """

    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning(f'No objects selected. Aborting {action_name}.')
        return None
    
    return selection