

curl https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@OpenPCDet-show-train-infer-10s.mp3" \
  -F model="whisper-1"


# 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
# echo 'export OPENAI_API_KEY="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"' >> ~/.bashrc
# source ~/.bashrc


# echo 'export OPENAI_API_KEY="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"' >> ~/.zshrc
# source ~/.zshrc


    # api_token = "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"



  curl https://api.openai.com/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "prompt": "一种点标注的点云落地解决方案 以激光雷达为背景",
    "n": 2,
    "size": "1024x1024"
  }'


'''
会议纪要的prompt如下：

* 会议主题：
* 会议时间：
* 会议地点：
* 参会人员：
* 会议议程：
* 会议内容：
* 会议结论：
* 会议纪要编写人：
* 会议纪要审核人：

以下是一些具体的提示：

* 会议主题：简明扼要地概括会议的主题，以便读者快速了解会议内容。
* 会议时间：会议开始和结束的时间。
* 会议地点：会议召开的地点。
* 参会人员：会议的参与者。
* 会议议程：会议的具体议题。
* 会议内容：会议讨论的具体内容。
* 会议结论：会议的最终结论或决定。
* 会议纪要编写人：会议纪要的编写者。
* 会议纪要审核人：会议纪要的审核者。

在编写会议纪要时，需要注意以下几点：

* 要客观、准确地记录会议内容，避免主观臆断。
* 要注意使用简洁明了的语言，避免使用专业术语或缩写。
* 要注意会议纪要的完整性，确保记录了会议的所有重要内容。

我们一般写纪要就是要记录明确的内容的，比如，xxx要在几号前完成什么工作，我们得出的结论是什么等等

在会议结束后，应及时编写会议纪要，并尽快将会议纪要发给参会人员。
'''






