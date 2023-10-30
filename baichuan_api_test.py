# Creating a Python script that combines all the functionalities including transcription and meeting summary generation.

import requests
import json
import time
import hashlib
from moviepy.editor import VideoFileClip

def calculate_md5(input_string):
    md5 = hashlib.md5()
    md5.update(input_string.encode('utf-8'))
    encrypted = md5.hexdigest()
    return encrypted

def extract_audio_from_video(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

def do_request(api_key, secret_key, transcription):
    url = "https://api.baichuan-ai.com/v1/chat"
    chinese_prompt = """
    请根据以上内容和以下要点生成会议纪要：
    * 会议主题：
    * 会议时间：
    * 会议地点：
    * 参会人员：
    * 会议议程：
    * 会议内容：
    * 会议结论：
    * 任务与责任：
    * 会议纪要编写人：
    * 会议纪要审核人：
    """
    data = {
        "model": "Baichuan2-53B",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant specialized in generating meeting summaries."
            },
            {
                "role": "user",
                "content": "Generate a meeting summary in English based on the following transcription:"
            },
            {
                "role": "user",
                "content": f"{transcription}"
            },
            {
                "role": "user",
                "content": f"Generate a meeting summary in Chinese: {chinese_prompt}"
            }
        ]
    }
    
    json_data = json.dumps(data)
    time_stamp = int(time.time())
    signature = calculate_md5(secret_key + json_data + str(time_stamp))
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
        "X-BC-Request-Id": "your requestId",
        "X-BC-Timestamp": str(time_stamp),
        "X-BC-Signature": signature,
        "X-BC-Sign-Algo": "MD5",
    }

    response = requests.post(url, data=json_data, headers=headers)
    
    if response.status_code == 200:
        print("请求成功！")
        print("响应header:", response.headers)
        print("响应body:", response.text)
        response_data = json.loads(response.text)
        print(response_data['data']['messages'][0]['content'])
    else:
        print("请求失败，状态码:", response.status_code)

def main():
    # Replace with your own API token and Secret Key
    api_key = "3446a532391d8f443bcf0b74879c6f9f"
    secret_key = "/XOC6eKi5UtmdCRvhO94eOJ7J3Q="

    # # Video and audio file paths
    # video_path = "your_video_path_here.mp4"
    # audio_path = "your_audio_path_here.mp3"
    
    # # Extract audio from video
    # extract_audio_from_video(video_path, audio_path)
    
    # Read the transcription from the text file
    with open('transcription_result.txt', 'r', encoding='utf-8') as f:
        transcription = f.read()
    
    # Make the API request for summary
    do_request(api_key, secret_key, transcription)

if __name__ == "__main__":
    main()


