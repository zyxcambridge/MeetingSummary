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
    
    # Define the prompt for the assistant
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
        "model": "gpt-3.5-turbo-16k-0613",  # Change this to "gpt-4-32k" if you're using GPT-4
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
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Check if the request was successful
        
        if 'choices' in response.json():
            summary_text = response.json()['choices'][0]['message']['content']
            return summary_text
        else:
            return "Error: Summary not generated."
    except requests.exceptions.RequestException as e:
        return f"API Request failed: {e}"

          
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
    # with open('transcription_result.txt', 'r', encoding='utf-8') as f:
    #     transcription = f.read()


    # # Generate the summary
    # summary_response = generate_summary(api_token, transcription)
    # if 'choices' in summary_response:
    #     summary_text = summary_response['choices'][0]['message']['content']
    #     # Print or save the summary
    #     print("Generated Summary:", summary_text)
    # else:
    #     print("An error occurred:", summary_response)

    #####################################################################
    # API Key = 3446a532391d8f443bcf0b74879c6f9f
    # Secret Key = /XOC6eKi5UtmdCRvhO94eOJ7J3Q=
    

if __name__ == "__main__":
    main()

