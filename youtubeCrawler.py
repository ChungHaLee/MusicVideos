from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import time
import pandas as pd

from pytube import YouTube
from pytube.cli import on_progress


def download(link):
    yt = YouTube(link, on_progress_callback=on_progress)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    stream.download('./data')


def search_keyword(music, singer):
    keyword = '{} {} official MV'.format(music, singer).replace(' ', '+')
    return keyword


def extract_source(soup_source):
    # 콘텐츠 모든 정보
    content = soup_source.find(class_ = 'yt-simple-endpoint style-scope ytd-video-renderer')
    # 콘텐츠 제목만 추출
    content_title = content.get_text().replace("\n", "")

    # 콘텐츠 링크만 추출
    content_link = "https://youtube.com" + content['href']

    # 조회수 & 업로드 날짜 추출
    content_record_src = soup_source.find(class_ = 'style-scope ytd-video-meta-block')
    content_view_cnt = content_record_src.find_all('span', 'inline-metadata-item')[0].get_text().replace('조회수 ', '').replace('\n', '')
    content_upload_date = content_record_src.find_all('span', 'inline-metadata-item')[1].get_text().replace('\n', '')

    return content_title, content_link, content_view_cnt, content_upload_date


def scraping(driver, keyword):
    # 스크래핑 할 URL 세팅
    URL = "https://www.youtube.com/results?search_query=" + keyword
    # 크롬 드라이버를 통해 지정한 URL의 웹 페이지 오픈
    driver.get(URL)
    # 웹 페이지 로딩 대기
    time.sleep(3)

    html_source = driver.page_source
    soup_source = BeautifulSoup(html_source, 'html.parser')

    title, link, view_cnt, upload_date = extract_source(soup_source)
    # Youtube video download
    download(link)

    return title, link, view_cnt, upload_date


def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # song meta data
    songs = pd.DataFrame({'music': ['Super Shy', 'Queencard'], 'singer': ['NewJeans', '(G)I-DLE']})
    keywords = [search_keyword(song['music'], song['singer']) for _, song in songs.iterrows()]

    data_info = [scraping(driver, keyword) for keyword in keywords]
    data_info_df = pd.DataFrame(data_info, columns=['title', 'link', 'view', 'upload_date'])
    data_info_df.to_csv("./youtube_songs_info.csv", index=False)


main()
