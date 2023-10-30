#coding=utf-8
# 作者：张益新

################################################################################################

# coding=utf-8
from moviepy.editor import VideoFileClip
import requests
import json

def extract_audio_from_video(video_path, audio_path):
    """
    提取视频文件的音频并保存为MP3
    """
    # 加载MP4文件
    video = VideoFileClip(video_path)
    
    # 提取音频
    audio = video.audio
    
    # 保存音频为MP3
    audio.write_audiofile(audio_path)


def create_transcription(api_token, audio_file_path):
    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    files = {
        "file": open(audio_file_path, "rb")
    }
    data = {
        "model": "whisper-1",
        "language": "zh"  # Optional, ISO-639-1 code for Chinese
    }

    response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.json()}"


def write_to_txt(transcription, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        if isinstance(transcription, dict):
            f.write(json.dumps(transcription, ensure_ascii=False, indent=4))
        else:
            f.write(transcription)
  

def generate_summary(api_token, transcription):
    """
    使用OpenAI GPT-3.5 API生成会议纪要。
    """
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }
    data = {
        # "model": "gpt-4-0613",
        "model": "gpt-3.5-turbo-16k-0613",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },
            {
                "role": "user",
                "content": "用英文输出会议纪要："
            },
            {
                "role": "user",
                "content": f"{transcription}"
            },
            {
                "role": "user",
                "content": "用中文输出会议纪要：请根据以上内容和以下要点生成会议纪要：\n* 会议主题：\n* 会议时间：\n* 会议地点：\n* 参会人员：\n* 会议议程：\n* 会议内容：\n* 会议结论：\n* 要记录明确的内容的，比如，xxx要在几号前完成什么工作，我们得出的结论是什么等等 ：\n会议纪要编写人：\n* 会议纪要审核人："
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.json()}"

          
def main():
    # 设置API令牌
    api_token = "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"
    
    # # 视频和音频文件路径
    # video_path = "OpenPCDet-show-train-infer.mp4"
    # audio_path = "OpenPCDet-show-train-infer.mp3"
    
    # # # 提取音频
    # extract_audio_from_video(video_path, audio_path)
    
    # # 音频转录
    # # Replace with your own API token and audio file path
    # # audio_file_path = "OpenPCDet-show-train-infer-60s.mp3"
    # audio_file_path = audio_path

    # result = create_transcription(api_token, audio_file_path)
    # print("Transcription Result:", result)

    # write_to_txt(result, "transcription_result.txt")

    # Read the transcription from the text file (you would replace this with your own transcription text)
    with open('transcription_result.txt', 'r', encoding='utf-8') as f:
        transcription = f.read()

    # Generate the summary
    summary_response = generate_summary(api_token, transcription)
    if 'choices' in summary_response:
        summary_text = summary_response['choices'][0]['message']['content']
        # Print or save the summary
        print("Generated Summary:", summary_text)
    else:
        print("An error occurred:", summary_response)



if __name__ == "__main__":
    main()

