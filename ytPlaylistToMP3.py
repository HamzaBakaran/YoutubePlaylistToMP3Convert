from pytube import YouTube, Playlist
import os

OUTPUT_PATH = "/home/hamza/Desktop/Python scripts"  # Replace this with your desired output path

def download_and_convert_to_mp3(video_url):
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=OUTPUT_PATH)
    base, _ = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(f"Converted: {yt.title} to MP3")

def main():
    playlist_url = input("Enter the URL of the YouTube playlist: ")
    
    # Create the output directory if it doesn't exist
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    # Extract videos from playlist and process each one
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        download_and_convert_to_mp3(video_url)

if __name__ == "__main__":
    main()
