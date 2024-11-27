import sys
from datetime import datetime
import os
from urllib.parse import urlparse, parse_qs

# [*] Default Environment Variables:
# PWD=/tmp/msmowz/20241121173033774104/001
# OLDPWD=/var/task
# LC_CTYPE=C.UTF-8

# [*] Creator Defined Environment Variables:
# SOMETHING=value

def clean_tiktok_url(url):
    # Add https:// prefix if not present
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    # Handle different TikTok URL formats
    parsed_url = urlparse(url)
    
    # Handle TikTok URLs
    if parsed_url.hostname in ('tiktok.com', 'www.tiktok.com', 'vm.tiktok.com'):
        # Split the path into components
        path_parts = parsed_url.path.split('/')
        
        # Look for the video ID
        for part in path_parts:
            if part.startswith(('video/', 'v/')):
                video_id = part.replace('video/', '').replace('v/', '')
                return f"https://www.tiktok.com/t/{video_id}"
            elif len(part) >= 19 and part.isalnum():  # TikTok video IDs are typically long alphanumeric strings
                return f"https://www.tiktok.com/t/{part}"
    
    return None

def main():
    # Check if URL is provided
    if len(sys.argv) != 2:
        print("[*] Error: Please provide a TikTok URL as an argument")
        sys.exit(1)
    
    tiktok_url = sys.argv[1]
    cleaned_url = clean_tiktok_url(tiktok_url)
    
    if cleaned_url:
        print(f"[*] Privacy-friendly URL: {cleaned_url}")
    else:
        print("[*] Error: Invalid TikTok URL provided")
    
if __name__ == "__main__":
    main()
