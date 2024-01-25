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
output_folder = '../Output/Data'

# Get all .mp4 files in the input folder
input_files = glob.glob(os.path.join(input_folder, '*.mp4'))

for input_file_path in input_files:
    # Load the video
    cap = cv2.VideoCapture(input_file_path)

    # Create output paths based on input file name
    file_name = os.path.basename(input_file_path)[:-4]  # Extract filename without extension

    # Create a folder for each video
    output_video_folder = os.path.join(output_folder, f'{file_name}_output')
    os.makedirs(output_video_folder, exist_ok=True)

    output_hex_file_path = os.path.join(output_video_folder, f'{file_name}_datastream.hex')
    output_hex_file = open(output_hex_file_path, 'w')

    output_txt_file_path = os.path.join(output_video_folder, f'{file_name}_datastream.txt')
    output_txt_file = open(output_txt_file_path, 'w')

    frame_count = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame to 48x32
        frame_resized = cv2.resize(frame, (48, 32))

        # Map pixels according to hardware order
        mapped_pixels = [frame_resized[i, j] for i in range(frame_resized.shape[0]) for j in range(frame_resized.shape[1])]

        # Extract LSB of each color channel and save as binary and hex
        binary_data = ""
        hex_data = ""
        for pixel in mapped_pixels:
            for value in pixel:
                binary_data += format(value & 1, '01b')  # Extract LSB
                hex_data += format(value & 1, '01x')  # Extract LSB and convert to hex

        binary_data_bytes = bytes(int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8))
        output_hex_file.write(hex(int(hex_data, 16))[2:] + '\n')  # Write hex data with newline

        # Write the binary data as plain text to the text file
        output_txt_file.write(binary_data)

        # Print progress
        frame_count += 1
        if frame_count % 10 == 0:  # Adjust the frequency of the print statements as needed
            print(f"Processing frame {frame_count} of {input_file_path}")

    # Release resources for the current video
    cap.release()
    output_hex_file.close()
    output_txt_file.close()

print("Processing complete.")
