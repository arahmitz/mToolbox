import maya.cmds as cmds
from madtools.utils.selection import get_selection

def point_to_average():
    """
    Points (T) the last selected object to the average translation (T) of all other selected objects

    When selected:
    - Last object is being driven
    - All others are the points for the average
    """
    selection = get_selection("Point To Average")

    if selection:
        if len(selection) < 2:
            cmds.warning("Point tool needs at least 2 selected objects. Point.")
            return
        else:
                # selection[-1] is the driven object
                constraint = (cmds.pointConstraint(selection[:-1], selection[-1], mo=False))
                cmds.delete(constraint) 