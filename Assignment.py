from pytube import YouTube
from moviepy.editor import VideoFileClip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import os



def get_youtube_video_url(search_query):
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com')
    
    try:
        accept_cookies_button = driver.find_element(By.XPATH, '//button[contains(text(), "I agree")]')
        accept_cookies_button.click()
    except:
        pass
    
    search_box = driver.find_element(By.NAME, 'search_query')
    search_box.send_keys(search_query)
    search_box.submit()
    
    time.sleep(3)
    first_video = driver.find_element(By.ID, 'video-title')
    video_url = first_video.get_attribute('href')
    driver.quit()
    return video_url


def download_youtube_video(url,output_path = "gif_creation"):
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path= output_path)
    return output_path
    

def list_files_with_extension(directory, extension):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_list.append(file)
    return file_list


def create_gif_from_video(video_path, start_time, end_time, output_gif_path):
  
    video_clip = VideoFileClip(video_path)
    gif_clip = video_clip.subclip(start_time, end_time)  # For the Time-strap from the video you want the GIF to be created
    gif_clip.write_gif(output_gif_path)



# Example 

video_url = get_youtube_video_url('Rick Astley Never Gonna Give You Up')      # Here user can give any Video name he want to create GIF for
directory_path = download_youtube_video(video_url)
file_name = list_files_with_extension(directory_path, ".mp4")

video_path = directory_path + "/" + file_name[0]          # To have the saved Video file path
create_gif_from_video(video_path, start_time=30, end_time=40, output_gif_path='animated.gif')      # Here user can customise time-strap for GIF to be created
print("GIF Created Successfully")


