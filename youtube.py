import urllib.request
import re
import webbrowser
import random


chrome_path = f"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
play = input('Search for: ')
play = "+".join(play.split())
print(play)
html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={play}")
x = html.read().decode()
# video_ids = re.search(r"watch\?v=(\S{11})", x)
video_ids = re.findall(r"watch\?v=(\S{11})", x)
res = video_ids
random_idx = random.randint(0, len(res))
webbrowser.get('chrome').open_new_tab(f"https://www.youtube.com/watch?v={res[0]}")
# res = video_ids
print(res)
print(f"https://www.youtube.com/watch?v={res[0]}")
# print(f"https://www.youtube.com/{res.group(0)}")
# def reasons_why(a, b, c):
#     a, b = b, a
#     a = a * c
#     b = b + c
#     return a, 
# if __name__=='__main__':
#     # t = int(input())
#     # for tt in range(t):
#     a, b, c = [int(x) for x in input().strip().split()]
#     ans1, ans2 = reasons_why(a, b, c)
#     print(ans1, ans2)
