import requests
import json
import xlsxwriter
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H_%M_%S")
workbook = xlsxwriter.Workbook('YoutubeList.xlsx')
worksheet = workbook.add_worksheet(str(dt_string))

def get_chName():
    row = 0
    col = 0
    count = 0
    error = 0
    f = open("youtubeVideoProp.txt", "r")
    for x in f:
        try:
            # url = ('https://www.googleapis.com/youtube/v3/videos?id=' + x + '&key=AIzaSyA4C8NVeR4O6XgB3WM_2WduPYjhN6kc3_c&fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics').replace('\n','')
            url = ('https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id=' + x + '&key=AIzaSyA4C8NVeR4O6XgB3WM_2WduPYjhN6kc3_c&fields=items(snippet(channelId%2C%20channelTitle))').replace('\n','')
            id = requests.get(url)
            data = id.json()
            channelId = data['items'][0]['snippet']['channelId']
            channelTitle = data['items'][0]['snippet']['channelTitle']
            dataForWrite = [channelTitle, channelId]
            worksheet.write(row, col, channelTitle)
            worksheet.write(row, col + 1, channelId)
            row += 1
            url_success = 'https://www.youtube.com/watch?v=' + str(x)
            with open("YoutubePropSuccess.txt",'a',encoding = 'utf-8') as txtFile:
                txtFile.write(str(url_success))
                txtFile.close()
                count += 1
        except:
            url_error = 'https://www.youtube.com/watch?v=' + str(x)
            # print('Get Error : https://www.youtube.com/watch?v=' + str(url))
            with open("YoutubePropError.txt",'a',encoding = 'utf-8') as txtFile:
                txtFile.write(str(url_error))
                txtFile.close()
                error += 1
    print('Success : ' + str(count))
    print('Error : ' + str(error))
    f.close()
    workbook.close()

def get_Stat():
    row = 0
    col = 3
    count = 0
    error = 0
    f = open("channelList.txt", "r")
    for x in f:
        try:
            # url = ('https://www.googleapis.com/youtube/v3/videos?id=' + x + '&key=AIzaSyA4C8NVeR4O6XgB3WM_2WduPYjhN6kc3_c&fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics').replace('\n','')
            url = ('https://youtube.googleapis.com/youtube/v3/channels?part=statistics&id=' + x + '&key=AIzaSyA4C8NVeR4O6XgB3WM_2WduPYjhN6kc3_c&fields=items(statistics)').replace('\n','')
            id = requests.get(url)
            data = id.json()
            channelId = data['items'][0]['snippet']['channelId']
            channelTitle = data['items'][0]['snippet']['channelTitle']
            dataForWrite = [channelTitle, channelId]
            worksheet.write(row, col, channelTitle)
            worksheet.write(row, col + 1, channelId)
            row += 1
            url_success = 'https://www.youtube.com/watch?v=' + str(x)
            with open("YoutubePropSuccess.txt",'a',encoding = 'utf-8') as txtFile:
                txtFile.write(str(url_success))
                txtFile.close()
                count += 1
        except:
            url_error = 'https://www.youtube.com/watch?v=' + str(x)
            # print('Get Error : https://www.youtube.com/watch?v=' + str(url))
            with open("YoutubePropError.txt",'a',encoding = 'utf-8') as txtFile:
                txtFile.write(str(url_error))
                txtFile.close()
                error += 1
    print('Success : ' + str(count))
    print('Error : ' + str(error))
    f.close()
    workbook.close()
if __name__ == "__main__":
    get_Stat()

# f = open("youtubeCommentProp.txt", "r")
# for x in f:
#     url = ('https://youtube.googleapis.com/youtube/v3/commentThreads?part=id&part=snippet&id=' + x + '&key=AIzaSyA4C8NVeR4O6XgB3WM_2WduPYjhN6kc3_c&fields=items(id%2Csnippet(videoId%2CtopLevelComment(snippet(videoId%2CtextDisplay%2CauthorChannelUrl%2CauthorChannelId))))&prettyPrint=true').replace('\n','')
#     id = requests.get(url)
#     jsonString = json.dumps(id.json(), ensure_ascii=False)
#     with open("CommentProp.json",'a',encoding = 'utf-8') as jsonFile:
#         jsonFile.write(jsonString)
#         jsonFile.close()
# f.close()

