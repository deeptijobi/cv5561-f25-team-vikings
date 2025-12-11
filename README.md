# Dynamic Object Tracking and 3D Reconstruction of Multiple Falling Objects from a Single-View Video
Real-time falling object detection using RGB camera data using Co-tracker, Open3D, and COLMAP.

## Team Members - OCCIPITAL

- Shri Dharshan Elango - elang020@umn.edu
- Sidharth Kudupudi - kudup001@umn.edu
- Deepti Jobi - jobi0008@umn.edu

## Roles

- Sidharth Kudupudi - Object Detection and Segmentation
- Shri Dharshan Elango - Feature Extraction
- Deepti Jobi - Setup, Simulation & Optimisation

## Scripts

Main.ipynb for Tracking and Reconstruction
  - Usage:
    - Run the Jupyter Notebook as instructed.
Synthetic Data Creation
  - IsaacSimFiles folder: Contains files used for dataset simulation in the Isaac Sim 2023 environment.
    - SpawnObjects.py
    - MP4Gen.py
    - CameraSpawn.usd
  - Usage:
    - Generate dataset in Isaac Sim:
    - Open spawnObjects.py.
    - Click Run to begin recording frames.
    - Stop the simulation when finished.
    - Run MP4Gen.py (Will compile frames into an MP4 video)
    
Dataset folder: Contains information about the generated dataset.

