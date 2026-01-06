import maya.cmds as cmds
from mtoolbox.utils.selection import get_selection


def delete_history():
    """
    Deletes ALL history of a selected object
    Using: delete -all -constructionHistory
    """

    selection = get_selection("Delete History")
    if not selection:
        return
    
    cmds.delete(all=True, constructionHistory=True)