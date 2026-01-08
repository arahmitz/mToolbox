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
    constraints = []

    if selection:
        if len(selection) < 2:
            cmds.warning("Snap tool needs at least 2 selected objects. Aborting Snap to Average.")
            return
        else:
            for driver in selection[:-1]:
                # selection[-1] <=> driven
                constraints.append(cmds.parentConstraint(driver, selection[-1], mo=False)) 
            for constraint in constraints:
                cmds.delete(constraint)