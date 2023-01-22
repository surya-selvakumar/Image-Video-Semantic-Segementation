import streamlit as st 
from segment import segment_vid, segment_image
import os
from PIL import Image

st.header('Semantic Segmentation')
tab1, tab2 = st.tabs(["Image Segmentation", "Video Segmentation"])

with tab1:
    img = st.file_uploader('Upload Image', type=["jpg"])
    img_path = './Images/uploaded.jpg'
    if img is not None:
        with open(img_path, 'wb') as f:
            f.write(img.read())
            
        if st.button('Segment Image'):
            segment_image(img_path)
            st.warning('Segmentation Completed')
            image = Image.open('./Images/segmented.jpg')
            st.image(image)
        
    
        
        
with tab2:
    vdo = st.file_uploader('Upload video')
    vid_path = './Videos/uploaded.mp4'
    
    if vdo is not None:
        with open(vid_path, 'wb') as f:
            f.write(vdo.read())
            
        if st.button('Segment Video'):
            segment_vid(vid_path)
            os.system("ffmpeg -i ./Videos/segmented.mp4 -vcodec libx264 ./Videos/segmented_out.mp4 -y")
            st.warning('Segmentation Completed')
            
            video = open('./Videos/segmented_out.mp4', 'rb')
            video_bytes = video.read()
            st.video(video_bytes)