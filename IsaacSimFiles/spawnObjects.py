from omni.isaac.core.utils.stage import open_stage, add_reference_to_stage
from pxr import UsdGeom, Gf, UsdPhysics
import omni.replicator.core as rep
import omni.usd
import numpy as np
import random

CAMERA_USD = "D:/isaacsim2023/CameraSpawn.usd"
OUTPUT_DIR = "D:/isaac_output"
NUM_OBJECTS = 2
HEIGHT_Z = 3.0
X_RANGE = (-0.3, 0.3)
Y_RANGE = (-0.3, 0.3)

ASSET_URL_LIST = [
    "http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/2023.1.1/Isaac/Props/YCB/Axis_Aligned_Physics/003_cracker_box.usd",
    "http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/2023.1.1/Isaac/Props/YCB/Axis_Aligned_Physics/004_sugar_box.usd",
    "http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/2023.1.1/Isaac/Props/YCB/Axis_Aligned_Physics/005_tomato_soup_can.usd",
]

def random_position():
    x = np.random.uniform(*X_RANGE)
    y = np.random.uniform(*Y_RANGE)
    z = np.random.uniform(HEIGHT_Z, HEIGHT_Z + 0.5)
    return np.array([x, y, z])

def random_rotation():
    return np.array([np.random.uniform(0, 360) for _ in range(3)])

def apply_initial_spin_to_mesh(prim_path):
    from pxr import PhysxSchema
    
    stage = omni.usd.get_context().get_stage()
    root_prim = stage.GetPrimAtPath(prim_path)
    
    if root_prim and root_prim.IsValid():
        target_prim = None
        if UsdPhysics.RigidBodyAPI(root_prim):
            target_prim = root_prim
        else:
            for child in root_prim.GetAllChildren():
                if UsdPhysics.RigidBodyAPI(child):
                    target_prim = child
                    print(f"  Found rigid body at: {child.GetPath()}")
                    break
        
        if target_prim:
            rigid_body_api = UsdPhysics.RigidBodyAPI(target_prim)
            physx_rb = PhysxSchema.PhysxRigidBodyAPI.Apply(target_prim)
            physx_rb.CreateAngularDampingAttr().Set(0.0)
            physx_rb.CreateMaxAngularVelocityAttr().Set(1000.0)
            angular_vel = Gf.Vec3f(
                np.random.uniform(-500, 500),
                np.random.uniform(-500, 500),
                np.random.uniform(-500, 500)
            )
            rigid_body_api.CreateAngularVelocityAttr().Set(angular_vel)
        else:
            print(f"  WARNING: No rigid body found!")

open_stage(usd_path=CAMERA_USD)
stage = omni.usd.get_context().get_stage()
add_reference_to_stage(
    usd_path="http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/2023.1.1/Isaac/Environments/Grid/default_environment.usd",
    prim_path="/World/defaultGroundPlane"
)

for i in range(NUM_OBJECTS):
    usd_path = random.choice(ASSET_URL_LIST)
    pos = random_position()
    rot = random_rotation()
    
    prim_path = f"/World/object_{i}"
    add_reference_to_stage(usd_path=usd_path, prim_path=prim_path)
    
    xform_prim = stage.GetPrimAtPath(prim_path)
    if xform_prim and xform_prim.IsValid():
        xformable = UsdGeom.Xformable(xform_prim)
        xformable.ClearXformOpOrder()
        translate_op = xformable.AddTranslateOp()
        translate_op.Set(Gf.Vec3d(float(pos[0]), float(pos[1]), float(pos[2])))
        rotate_op = xformable.AddRotateXYZOp()
        rotate_op.Set(Gf.Vec3f(float(rot[0]), float(rot[1]), float(rot[2])))
        scale_op = xformable.AddScaleOp()
        scale_op.Set(Gf.Vec3f(4.0, 4.0, 4.0))
        
        apply_initial_spin_to_mesh(prim_path) 

print("Scene setup complete!")

render_product = rep.create.render_product("/World/Camera", (1280, 720))
writer = rep.WriterRegistry.get("BasicWriter")
writer.initialize(output_dir=OUTPUT_DIR, rgb=True)
writer.attach([render_product])
