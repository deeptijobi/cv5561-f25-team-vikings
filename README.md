# Dynamic Object Tracking and 3D Reconstruction of Multiple Falling Objects from a Single-View Video
Real-time falling object detection using RGB camera data using Co-tracker, Open3D and COLMAP.

## Team Members - OCCIPITAL

- Shri Dharshan Elango - elang020@umn.edu
- Sidharth Kudupudi - kudup001@umn.edu
- Deepti Jobi - jobi0008@umn.edu

## Roles

- Sidharth Kudupudi - Object Detection and Segmentation
- Shri Dharshan Elango - Feature Extraction
- Deepti Jobi - Setup, Simulation & Optimisation

## Scripts

### Main.ipynb – Tracking and Reconstruction
- **Usage:**  
  Run the Jupyter Notebook following the sections in order.

### Synthetic Data Creation
- **Files (in `isaacSimFiles` folder):**  
  - `SpawnObjects.py`  
  - `MP4Gen.py`  
  - `CameraSpawn.usd`  

- **Usage:**    
     - Open `SpawnObjects.py`.  
     - Click **Run** to begin recording frames.  
     - **Stop** the simulation when finished.   
     - Run `MP4Gen.py` (will compile frames into an MP4 video)

### Dataset
- **Folder:** `Dataset`  
- **Contents:** Generated dataset information.

