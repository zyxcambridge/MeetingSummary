from pydub import AudioSegment

# Load the audio file
audio_path = "OpenPCDet-show-train-infer.mp3"
audio = AudioSegment.from_mp3(audio_path)

# Extract the first 10 seconds (10,000 milliseconds)
audio_10s = audio[:60000]

# Save the 10-second segment
output_path = "OpenPCDet-show-train-infer-60s.mp3"
audio_10s.export(output_path, format="mp3")

output_path

# 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
# echo 'export OPENAI_API_KEY="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"' >> ~/.bashrc
# source ~/.bashrc


# echo 'export OPENAI_API_KEY="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"' >> ~/.zshrc
# source ~/.zshrc



# import requests

# def create_transcription(api_token, audio_file_path):
#     url = "https://api.openai.com/v1/audio/transcriptions"
#     headers = {
#         "Authorization": f"Bearer {api_token}"
#     }
#     files = {
#         "file": open(audio_file_path, "rb")
#     }
#     data = {
#         "model": "whisper-1",
#         "language": "zh"  # Optional, ISO-639-1 code for Chinese
#     }

#     response = requests.post(url, headers=headers, files=files, data=data)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return f"Error: {response.status_code}, {response.json()}"

# def main():
#     # Set API token
#     # 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

#     api_token = "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"

#     # Audio file path
#     audio_file_path = "OpenPCDet-show-train-infer-10s.mp3"  # Replace with your audio file path

#     # Transcribe audio
#     result = create_transcription(api_token, audio_file_path)
#     print("Transcription Result:", result)

# if __name__ == "__main__":
#     main()
