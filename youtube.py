import requests
import json
list = []

f = open("youtubeVideoProp.txt", "r")
for x in f:
    url = ('https://www.googleapis.com/youtube/v3/videos?id=' + x + '&key=AIzaSyA4C8NVeR4O6XgB3WM_2WduPYjhN6kc3_c&fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics').replace('\n','')
    id = requests.get(url)
    jsonString = json.dumps(id.json(), ensure_ascii=False)
    with open("YoutubeProp.json",'a',encoding = 'utf-8') as jsonFile:
        jsonFile.write(jsonString)
        jsonFile.close()
f.close()


# f = open("youtubeCommentProp.txt", "r")
# for x in f:
#     url = ('https://youtube.googleapis.com/youtube/v3/commentThreads?part=id&part=snippet&id=' + x + '&key=AIzaSyA4C8NVeR4O6XgB3WM_2WduPYjhN6kc3_c&fields=items(id%2Csnippet(videoId%2CtopLevelComment(snippet(videoId%2CtextDisplay%2CauthorChannelUrl%2CauthorChannelId))))&prettyPrint=true').replace('\n','')
#     id = requests.get(url)
#     jsonString = json.dumps(id.json(), ensure_ascii=False)
#     with open("CommentProp.json",'a',encoding = 'utf-8') as jsonFile:
#         jsonFile.write(jsonString)
#         jsonFile.close()
# f.close()

