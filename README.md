# Dynamic Object Tracking and 3D Reconstruction of Multiple Falling Objects from a Single-View Video
Real-time falling object detection using RGB camera data using Co-tracker, Open3D, and COLMAP.

## Team Members

- Shri Dharshan Elango - elang020@umn.edu
- Sidharth Kudupudi - kudup001@umn.edu
- Deepti Jobi - jobi0008@umn.edu

## Roles

- Sidharth Kudupudi - Co-tracker Implementation and 3d Reconstruction 
- Shri Dharshan Elango - 3d Reconstruction and Segmentation 
- Deepti Jobi - Setup, Simulation and Segmentation

## Scripts

### Main.ipynb – Tracking and Reconstruction
- **Usage:**  
  Run the Jupyter Notebook following the sections in order.

### Synthetic Data Creation
- **Files (in `IsaacSimFiles` folder):**  
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

### Citation
```bibtex
@inproceedings{karaev2025cotracker3,
  title={CoTracker3: Simpler and better point tracking by pseudo-labelling real videos},
  author={Karaev, Nikita and others},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  year={2025}
}
@inproceedings{schonberger2016mvs,
  title={Pixelwise View Selection for Unstructured Multi-View Stereo},
  author={Sch{\"o}nberger, Johannes L and Zheng, Enliang and Pollefeys, Marc and Frahm, Jan-Michael},
  booktitle={European Conference on Computer Vision},
  year={2016}
}
@misc{cotracker2023github,
  author       = {Karaev, Nikita and Facebook Research},
  title        = {CoTracker: Video Point Tracking Library},
  howpublished = {\url{https://github.com/facebookresearch/co-tracker}},
  year         = {2023},
  note         = {Accessed: 2025-02-12}
}
