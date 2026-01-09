import maya.cmds as cmds
from mtoolbox.utils.selection import get_selection

def create_joints():
    """
    Creates a chain with zeroed JO of user selected length and name. Selects the first joint at the end.
     
    If an object is selected, chain will be snapped to that object, otherwise it'll start at world origin.
    """
    spacing = 5
    joint_count = 3
    base_name = 'joint'

    for joint in range(joint_count):
        if joint == joint_count-1:
            joint_name = base_name + '_' +  str(joint) + '_end'
        else:
            joint_name = base_name + '_' +  str(joint)
        cmds.joint(name=joint_name, p=(joint * spacing, 0, 0))

create_joints()
