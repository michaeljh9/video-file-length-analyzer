import os
import csv
from moviepy.editor import VideoFileClip

def get_video_length(file_path):
    try:
        clip = VideoFileClip(file_path)
        duration = clip.duration
        clip.close()
        return duration
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return None

def process_folder(folder_path):
    video_data = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.mkv', '.mp4', '.avi')):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                duration = get_video_length(file_path)
                if duration is not None:
                    video_data.append([relative_path, duration])
    
    # Sort the video_data list alphabetically by file path
    video_data.sort(key=lambda x: x[0].lower())
    
    return video_data

def main():
    folder_path = input("Enter the folder path containing video files: ")
    
    if not os.path.isdir(folder_path):
        print("Invalid folder path. Please try again.")
        return

    video_data = process_folder(folder_path)

    output_file = os.path.join(folder_path, "video_lengths.csv")
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File Path", "Duration (seconds)"])
        
        # Write the data with rounded duration values
        for row in video_data:
            writer.writerow([row[0], f"{row[1]:.2f}"])

    print(f"CSV file has been created: {output_file}")

if __name__ == "__main__":
    main()