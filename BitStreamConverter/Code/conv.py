import glob
import os

try:
    import numpy as np
except ModuleNotFoundError:
    # If numpy is not installed, try installing it
    try:
        import subprocess
        subprocess.check_call(["pip", "install", "numpy"])
        import numpy as np  # Try importing again after installation
    except Exception as e:
        print(f"Error installing or importing 'numpy': {e}")
        exit()

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

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

width = int(48)
height = int(32)


def save_bin(frame_resized):
    # Original order: Map pixels according to the order read from the video file
    mapped_pixels_original = frame_resized.reshape(-1, frame_resized.shape[-1])

    numpy_original_pixels = np.array(mapped_pixels_original).flatten()

    binary_data_original = numpy_original_pixels.tobytes()

    return binary_data_original


def process_frame(frame_resized):

    # Original order: Map pixels according to the order read from the video file
    mapped_pixels_original = frame_resized.reshape(-1, frame_resized.shape[-1])

    mapped_pixels_original_d1 = []
    mapped_pixels_original_d2 = []
    mapped_pixels_original_d3 = []
    mapped_pixels_original_d4 = []
    mapped_pixels_original_d5 = []
    mapped_pixels_original_d6 = []

    index = 1
    for i in range(1, 33):
        for j in range(1, 49):
            print("Processing: " + str(index) + " | FOR: " + str(i) + " / " + str(j))
            if(1 <= index <= 16 or 49 <= index <= 64 or 97 <= index <= 112 or 145 <= index <= 160 or 193 <= index <= 208 or 241 <= index <= 256 or 289 <= index <= 304 or 337 <= index <= 352 or 385 <= index <= 400 or 433 <= index <= 448 or 481 <= index <= 496 or 529 <= index <= 544 or 577 <= index <= 592 or 625 <= index <= 640 or 673 <= index <= 688 or 721 <= index <= 736):
                # Trigger an action for DISPLAY_1_Formula
                mapped_pixels_original_d1.append(mapped_pixels_original[index - 1])
            elif(17 <= index <= 32 or 65 <= index <= 80 or 113 <= index <= 128 or 161 <= index <= 176 or 209 <= index <= 224 or 257 <= index <= 272 or 305 <= index <= 320 or 353 <= index <= 368 or 401 <= index <= 416 or 449 <= index <= 464 or 497 <= index <= 512 or 545 <= index <= 560 or 593 <= index <= 608 or 641 <= index <= 656 or 689 <= index <= 704 or 737 <= index <= 752):
                # Trigger an action for DISPLAY_2_Formula
                mapped_pixels_original_d2.append(mapped_pixels_original[index - 1])
            elif(33 <= index <= 48 or 81 <= index <= 96 or 129 <= index <= 144 or 177 <= index <= 192 or 225 <= index <= 240 or 273 <= index <= 288 or 321 <= index <= 336 or 369 <= index <= 384 or 417 <= index <= 432 or 465 <= index <= 480 or 513 <= index <= 528 or 561 <= index <= 576 or 609 <= index <= 624 or 657 <= index <= 672 or 705 <= index <= 720 or 753 <= index <= 768):
                # Trigger an action for DISPLAY_3_Formula
                mapped_pixels_original_d3.append(mapped_pixels_original[index - 1])
            elif(769 <= index <= 784 or 817 <= index <= 832 or 865 <= index <= 880 or 913 <= index <= 928 or 961 <= index <= 976 or 1009 <= index <= 1024 or 1057 <= index <= 1072 or 1105 <= index <= 1120 or 1153 <= index <= 1168 or 1201 <= index <= 1216 or 1249 <= index <= 1264 or 1297 <= index <= 1312 or 1345 <= index <= 1360 or 1393 <= index <= 1408 or 1441 <= index <= 1456 or 1489 <= index <= 1504):
                # Trigger an action for DISPLAY_4_Formula
                mapped_pixels_original_d4.append(mapped_pixels_original[index - 1])
            elif(785 <= index <= 800 or 833 <= index <= 848 or 881 <= index <= 896 or 929 <= index <= 944 or 977 <= index <= 992 or 1025 <= index <= 1040 or 1073 <= index <= 1088 or 1121 <= index <= 1136 or 1169 <= index <= 1184 or 1217 <= index <= 1232 or 1265 <= index <= 1280 or 1313 <= index <= 1328 or 1361 <= index <= 1376 or 1409 <= index <= 1424 or 1457 <= index <= 1472 or 1505 <= index <= 1520):
                # Trigger an action for DISPLAY_5_Formula
                mapped_pixels_original_d5.append(mapped_pixels_original[index - 1])
            elif (801 <= index <= 816 or 849 <= index <= 864 or 897 <= index <= 912 or 945 <= index <= 960 or 993 <= index <= 1008 or 1041 <= index <= 1056 or 1089 <= index <= 1104 or 1137 <= index <= 1152 or 1185 <= index <= 1200 or 1233 <= index <= 1248 or 1281 <= index <= 1296 or 1329 <= index <= 1344 or 1377 <= index <= 1392 or 1425 <= index <= 1440 or 1473 <= index <= 1488 or 1521 <= index <= 1536):
                # Trigger an action for DISPLAY_6_Formula
                mapped_pixels_original_d6.append(mapped_pixels_original[index - 1])
            index += 1

    numpy_mapped_pixels_modified_d1 = np.array(mapped_pixels_original_d1)
    numpy_mapped_pixels_modified_d2 = np.array(mapped_pixels_original_d2)
    numpy_mapped_pixels_modified_d3 = np.array(mapped_pixels_original_d3)
    numpy_mapped_pixels_modified_d4 = np.array(mapped_pixels_original_d4)
    numpy_mapped_pixels_modified_d5 = np.array(mapped_pixels_original_d5)
    numpy_mapped_pixels_modified_d6 = np.array(mapped_pixels_original_d6)

    numpy_d1_tr = numpy_mapped_pixels_modified_d1.reshape((16, 16, 3))
    numpy_d2_tr = numpy_mapped_pixels_modified_d2.reshape((16, 16, 3))
    numpy_d3_tr = numpy_mapped_pixels_modified_d3.reshape((16, 16, 3))
    numpy_d4_tr = numpy_mapped_pixels_modified_d4.reshape((16, 16, 3))
    numpy_d5_tr = numpy_mapped_pixels_modified_d5.reshape((16, 16, 3))
    numpy_d6_tr = numpy_mapped_pixels_modified_d6.reshape((16, 16, 3))

    for arr in [numpy_d1_tr, numpy_d2_tr, numpy_d3_tr, numpy_d4_tr, numpy_d5_tr, numpy_d6_tr]:
        for i in range(1, 16, 2):
            arr[i] = arr[i, ::-1]

    mapped_pixels_modified_d1_out = numpy_d1_tr.reshape((256, 3))
    mapped_pixels_modified_d2_out = numpy_d2_tr.reshape((256, 3))
    mapped_pixels_modified_d3_out = numpy_d3_tr.reshape((256, 3))
    mapped_pixels_modified_d4_out = numpy_d4_tr.reshape((256, 3))
    mapped_pixels_modified_d5_out = numpy_d5_tr.reshape((256, 3))
    mapped_pixels_modified_d6_out = numpy_d6_tr.reshape((256, 3))

    mapped_pixels_modified_output = np.concatenate((mapped_pixels_modified_d1_out, mapped_pixels_modified_d2_out, mapped_pixels_modified_d3_out, mapped_pixels_modified_d4_out, mapped_pixels_modified_d5_out, mapped_pixels_modified_d6_out), axis=0)

    mapped_pixels_modified_output_flat = mapped_pixels_modified_output.flatten()

    # Extract GRB values and pack into bytes for the modified order
    binary_data_modified = (mapped_pixels_modified_output_flat.tobytes())

    return binary_data_modified


for input_file_path in input_files:
    # Load the video
    cap = cv2.VideoCapture(input_file_path)

    file_name = os.path.basename(input_file_path)[:-4]  # Extract filename without extension

    data_output_folder = os.path.join(output_folder, f'{file_name}_output')
    os.makedirs(data_output_folder, exist_ok=True)

    output_bin_pre_file_path = os.path.join(data_output_folder, f'{file_name}_original_datastream.bin')
    output_bin_pre_file = open(output_bin_pre_file_path, 'wb')  # Open in binary write mode

    output_bin_file_path = os.path.join(data_output_folder, f'{file_name}_modified_datastream.bin')
    output_bin_file = open(output_bin_file_path, 'wb')  # Open in binary write mode

    # Set up VideoWriter for the modified video

    print(f"Processing file: {input_file_path}")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame
        resized_frame = cv2.resize(frame, (width, height))

        # Process frame
        binary_data_original_out = save_bin(resized_frame)
        binary_data_modified_out = process_frame(resized_frame)

        output_bin_pre_file.write(binary_data_original_out)
        output_bin_file.write(binary_data_modified_out)

    # Release resources for the current video
    cap.release()
    output_bin_pre_file.close()
    output_bin_file.close()

print("Processing complete.")
