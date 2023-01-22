import pixellib
from pixellib.semantic import semantic_segmentation
# Setting the file path for the input video


segment_video = semantic_segmentation()
segment_video.load_ade20k_model("deeplabv3_xception65_ade20k.h5")

def segment_vid(vdo_path):
    input_video_file_path = vdo_path
    segment_video.process_video_ade20k(
        input_video_file_path, 
        frames_per_second=30,
        output_video_name="./Videos/segmented.mp4",
    )
    
    
def segment_image(img_path):
    segment_video.segmentAsAde20k(img_path, output_image_name="./Images/segmented.jpg")
    
    


