import maya.cmds as cmds

def create_joints():
    """
    Creates a chain with zero-ed JO of user selected length and name. Selects the first joint at the end.
    """
    spacing = 5
    joint_count = 3
    base_name = 'joint'
    add_affix = True
    root_joint = []

    # Create parametered joint chain
    for joint in range(joint_count):

        if add_affix and joint == joint_count-1:
            joint_name = base_name + str(joint+1) + '_end'
        else:
            joint_name = base_name + str(joint+1)
        
        if joint == 0:
            root_joint = joint_name

        cmds.joint(name=joint_name, p=(joint * spacing, 0, 0))
    
    # Select root at the end
    cmds.select(root_joint)
