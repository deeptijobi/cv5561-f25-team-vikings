import cv2
import os

OUTPUT_DIR = "D:/isaac_output"

print("Converting frames to MP4 video...")

fps = 120

possible_dirs = [
    os.path.join(OUTPUT_DIR, "rgb"),
    OUTPUT_DIR
]

frame_dir = None
frames = []

for check_dir in possible_dirs:
    if os.path.exists(check_dir):
        temp_frames = sorted([f for f in os.listdir(check_dir) if f.endswith('.png')])
        if temp_frames:
            frame_dir = check_dir
            frames = temp_frames
            print(f"Found {len(frames)} frames in: {frame_dir}")
            break

if frames and frame_dir:
    output_video = os.path.join(OUTPUT_DIR, "video_120fps.mp4")
    
    print("Processing frames...")
    first_frame = cv2.imread(os.path.join(frame_dir, frames[0]))
    height, width = first_frame.shape[:2]
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
    
    for i, frame_file in enumerate(frames):
        img = cv2.imread(os.path.join(frame_dir, frame_file))
        video.write(img)
        
        if (i + 1) % 100 == 0:
            print(f"  Processed {i + 1}/{len(frames)}")
    
    video.release()
    
    file_size = os.path.getsize(output_video) / (1024 * 1024)

    print(f"Location: {output_video}")
    print(f"Size: {file_size:.1f} MB")
    print(f"Duration: {len(frames)/fps:.1f} seconds")
    print(f"Frames: {len(frames)}")
else:
    print("ERROR: No frames found!")