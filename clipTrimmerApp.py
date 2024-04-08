import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_video_clip(input_file, output_folder):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return
    
    # Check if the output folder exists, create it if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Use moviepy to extract the video clip
    output_file = os.path.join(output_folder, os.path.basename(input_file))
    output_file = os.path.splitext(output_file)[0] + f"_clip_0-20s.mp4"

    start_time = 5 * 60 + 27  # 1 minute 20 seconds
    end_time = 5 * 60 + 46  # 2 minute 20 seconds

    video_clip = VideoFileClip(input_file).subclip(start_time, end_time)
    video_clip.write_videofile(output_file)

    print(f"Video clip saved: {output_file}")

if __name__ == "__main__":
    input_file = "/home/harish/Downloads/pluto"
    output_folder = "/home/harish/Downloads"

    extract_video_clip(input_file, output_folder)
