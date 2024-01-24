import glob
import os

try:
    import cv2
except ModuleNotFoundError:
    # If cv2 is not installed, try installing it
    try:
        import subprocess
        subprocess.check_call(["pip", "install", "opencv-python"])
        import cv2  # Try importing again after installation
    except Exception as e:
        print(f"Error installing or importing 'cv2': {e}")
        exit()

# Define the input and output folders
input_folder = '../Input'
output_folder = '../Output/Video'

# Get all .mp4 files in the input folder
input_files = glob.glob(os.path.join(input_folder, '*.mp4'))

for input_file_path in input_files:
    # Load the video
    cap = cv2.VideoCapture(input_file_path)

    # Get input video properties
    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(5)

    # Create output video paths based on input file name
    file_name = os.path.basename(input_file_path)[:-4]  # Extract filename without extension
    output_video_path = os.path.join(output_folder, f'{file_name}_downscaled_video.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_video_path, fourcc, fps, (48, 32))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame to 48x32
        frame_resized = cv2.resize(frame, (48, 32))

        # Write resized frame to the output video
        output_video.write(frame_resized)

    # Release resources for the current video
    cap.release()
    output_video.release()

    print(f"Downscaled video saved to: {output_video_path}")

print("Processing complete.")
