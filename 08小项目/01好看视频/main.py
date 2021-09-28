

import requests
import json
import os

def haokan_spider():
    url = 'https://haokan.baidu.com/web/video/feed?tab=gaoxiao_new&act=pcFeed&pd=pc&num=20&shuaxin_id=1632757717834'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    response = requests.get(url,headers=headers).json()
    # print(response)
    videos = response['data']['response']['videos']
    print(videos)
    if not os.path.exists('./videos'):
        os.makedirs('./videos')
    else:
        print('该文件已存在，无需创建')

    for index in videos:
        title = index['title']
        # print(title)
        play_url = index['play_url']
        path = 'videos/'
        video_content = requests.get(url=play_url,headers=headers).content
        with open(path + title + '.mp4 ','wb') as f:
            print("---开始下载视频---")
            f.write(video_content)
            f.close()
            print("---下载成功---" + "\n")

if __name__ == '__main__':
    haokan_spider()