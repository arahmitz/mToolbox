import maya.cmds as cmds
from mtoolbox.utils.selection import get_selection

def snap_to_average():
    """
    Snaps the last selected object to the average transform(T/R/S) of all other selected objects

    When selected:
    - Last object is being driven
    - All others are the points for the average
    """
    selection = get_selection("Snap to Average")

    if selection:
        if len(selection) < 2:
            cmds.warning("Snap tool needs at least 2 selected objects. Aborting Snap to Average.")
            return
        else:
                # selection[-1] is the driven object
                constraint = (cmds.parentConstraint(selection[0], selection[1:], mo=False))
                cmds.delete(constraint) 