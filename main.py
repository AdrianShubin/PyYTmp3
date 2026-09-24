import subprocess
from pathlib import Path
import yt_dlp

print("YouTube to mp3\n")
print("Enter the amount of kbps that you want")
print("Valid options are: 128, 192, or 320")

kbps = int(input())
if not kbps in [128, 192, 320]:
    raise ValueError(f"Kbps cannot be {kbps}")

is_playlist = input("\nIs it a playlist url / multiple urls? [Y/n]\n").lower() == "y"
dir = Path.home() / "Music"

multiple_videos = False

urls = []

if is_playlist:
    playlist_dir = input("\nEnter the playlist name:\n")
    if playlist_dir == "":
        raise ValueError("Playlist needs a name")
    
    dir = dir / playlist_dir
    dir.mkdir(parents=True, exist_ok=True)

    multiple_videos = input("\nAre there multiple urls you will paste? [Y/n]\n").lower() == "y"
    if multiple_videos:
        print("\nEnter the urls:")
        urls = input().split(" ")
    else:
        print("\nEnter the url:")
        urls.append(input())
else:
    print("\nEnter the url:")
    urls.append(input())

output = "%(title)s.%(ext)s"

for url in urls:
    subprocess.run(
        ["yt-dlp", "-x", "--audio-format", "mp3", "--audio-quality", f"{kbps}K", "-o", output, url],
        cwd=dir,
        check=True
    )
    subprocess.run(["echo"])
