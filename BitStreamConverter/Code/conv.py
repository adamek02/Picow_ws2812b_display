import cv2
import glob
import os

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

    output_bin_file_path = os.path.join(output_video_folder, f'{file_name}_datastream.bin')
    output_bin_file = open(output_bin_file_path, 'wb')

    output_txt_file_path = os.path.join(output_video_folder, f'{file_name}_datastream.txt')
    output_txt_file = open(output_txt_file_path, 'w')

    frame_count = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame to 48x32
        frame_resized = cv2.resize(frame, (48, 32))

        # Convert resized frame to 24-bit format (BGR)
        pixels = frame_resized.reshape(-1, 3)  # Reshape to get RGB values for each pixel

        # Convert RGB values to binary and write to the binary file
        binary_data = "".join([format(int(value), '08b') for pixel in pixels for value in pixel])
        binary_data_bytes = bytes(int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8))
        output_bin_file.write(binary_data_bytes)

        # Write the binary data as plain text to the text file
        output_txt_file.write(binary_data)

        # Print progress
        frame_count += 1
        if frame_count % 10 == 0:  # Adjust the frequency of the print statements as needed
            print(f"Processing frame {frame_count} of {input_file_path}")

    # Release resources for the current video
    cap.release()
    output_bin_file.close()
    output_txt_file.close()

print("Processing complete.")
