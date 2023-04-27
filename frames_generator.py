
import cv2
import os
import glob
from tqdm import tqdm
import uuid

# Checking Functionalities
# Function to extract frames
def FrameCapture(path,folder_name,uid):
    vidObj = cv2.VideoCapture(path)
    # Used as counter variable
    count = 0
    counter = 1
    max_frames = 600
  
    # checks whether frames were extracted

    success = 1
    text = f"itms_{uid}_"
    saving_folder = os.path.join('raw_data',folder_name)
    if not os.path.exists(saving_folder):
        os.makedirs(saving_folder)
    print(f"The Frames are saving to {saving_folder}")

    while success:
        success, image = vidObj.read()
        for i in tqdm(range(0, max_frames*counter), desc ="Number of Frames"):
            if count%counter == 0:            
                filename = f"{text}{count}.jpg"
                save_file = os.path.join('raw_data',folder_name,filename)
                cv2.imwrite(save_file, image)
            count += 1
        print(f"Total {max_frames} has been downloaded to {folder_name}")

            
def vid_gen(folder_name,uid):
    saving_folder=os.path.join('raw_data',folder_name)
    img1 = os.listdir(saving_folder)[0]
    y=os.path.join(saving_folder,img1)
    img = cv2.imread(y)
    dimensions = img.shape
    frame_size = (dimensions[1],dimensions[0])

    video_name = f"Output_{uid}"
    out_vid_file = f'raw_data/{video_name}.avi'
    out = cv2.VideoWriter(out_vid_file,cv2.VideoWriter_fourcc(*'DIVX'), 20, frame_size)
    for_vid_path = saving_folder+"/*.jpg"
    for filename in tqdm(glob.glob(for_vid_path)):
        img = cv2.imread(filename)
        out.write(img)
    print(f"The Video has been saved as {out_vid_file}")

    out.release()
if __name__ == '__main__':
    uid = uuid.uuid4()
    uid = uid.fields[1]
    folder_name = "Frames_check"
    FrameCapture(r"F:\MasterCode\yolov7\runs\detect\exp14\ex_1.mp4",folder_name,uid)
    vid_gen(folder_name,uid)

    # rtsp://admin:admin@192.168.0.84:554