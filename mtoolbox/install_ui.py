import maya.cmds as cmds
import os, shutil

def onMayaDroppedPythonFile(*args):

    # Setup filepaths
    installer_dir = os.path.dirname(__file__)
    prefs_dir = cmds.internalVar(userPrefDir=True)
    icons_source_dir = os.path.join(installer_dir, "icons")
    icons_target_dir = os.path.join(prefs_dir, "icons", "mtoolbox")
    os.makedirs(icons_target_dir, exist_ok=True)

    # Copy files from scripts/mtoolbox/icons to prefs/icons/mtoolbox
    if os.path.exists(icons_source_dir):
        for file_name in os.listdir(icons_source_dir):
            source_file = os.path.join(icons_source_dir, file_name)
            target_file = os.path.join(icons_target_dir, file_name)
            if os.path.isfile(source_file):
                shutil.copy(source_file, target_file)


    # Current shelf
    current_shelf = cmds.shelfTabLayout('ShelfLayout', q=True, st=True)
    button_name = "mToolbox"


    # Remove old button if exists on this shelf
    if cmds.shelfButton(button_name, exists=True, parent=current_shelf):
        cmds.deleteUI(button_name)

    # Create new button
    cmds.shelfButton(
        button_name,
        parent=current_shelf,
        label="mToolbox",
        image="mtoolbox/mtoolbox.png",
        command="import mtoolbox.mtoolbox_ui as toolbox; toolbox.show_ui()",
        sourceType="python"
    )
