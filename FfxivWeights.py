bl_info = {
    "name": "FFXIV Weight Normalizser",
    "blender": (2, 80, 0),
    "category": "Object",
}


import bpy


class FfxivWeights(bpy.types.Operator):
    """FFXIV Weight Normalizer"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.ffxiv_weights"        # Unique identifier for buttons and menu items to reference.
    bl_label = "FFXIV Weight Normalizer"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.

        bpy.ops.object.vertex_group_quantize(group_select_mode='BONE_DEFORM', steps=255)
        bpy.ops.object.vertex_group_limit_total(group_select_mode='BONE_DEFORM', limit=8)
        bpy.ops.object.vertex_group_normalize_all(group_select_mode='BONE_DEFORM', lock_active=False)
        print("Weights Processed")

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

def menu_func(self, context):
    self.layout.operator(FfxivWeights.bl_idname)

def register():
    bpy.utils.register_class(FfxivWeights)
    bpy.types.VIEW3D_MT_object.append(menu_func)  # Adds the new operator to an existing menu.

def unregister():
    bpy.utils.unregister_class(FfxivWeights)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()