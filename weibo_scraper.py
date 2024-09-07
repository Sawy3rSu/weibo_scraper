import os
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# 使用本地的 Chrome 浏览器数据避免登录
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:/Users/xxxxxx/AppData/Local/Google/Chrome/User Data")#使用本地浏览器缓存避免登录问题
chrome_options.add_argument("--profile-directory=Default")
#chrome_options.add_argument("--headless")  # 运行在后台

# 初始化 Selenium WebDriver
driver = webdriver.Chrome(options=chrome_options)

# 定义要搜索的关键词列表
keywords = ['xxxxxx', 'xxxxxxx', 'xxxxxx', 'xxxxxxx', 'xxxxxxx']  # 可以添加更多关键词

# 保存生成的文件路径
saved_files = []

for keyword in keywords:
    try:
        # 打开指定微博页面
        driver.get('https://weibo.com/u/xxxxxxxxx')  # 替换为目标页面

        # 等待页面加载
        time.sleep(10)  # 根据网络情况调整

        # 等待并找到搜索框
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="搜索他的微博"]'))
        )
        
        # 输入关键词并提交搜索
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)  # 提交搜索
        # 等待搜索结果加载
        time.sleep(5)

        # 模拟滚动加载
        SCROLL_PAUSE_TIME = 2
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # 滚动到页面底部
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)

            # 计算新的滚动高度并与之前的高度进行比较
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # 处理“展开”按钮，展开所有被缩进的微博内容
        try:
            expand_buttons = driver.find_elements(By.XPATH, '//span[@class="expand"]')
            for button in expand_buttons:
                driver.execute_script("arguments[0].click();", button)
            time.sleep(2)
        except Exception as e:
            print(f"点击展开按钮时出错: {e}")

        # 获取页面内容
        page_source = driver.page_source

        # 使用 BeautifulSoup 解析页面内容
        soup = BeautifulSoup(page_source, 'html.parser')

        # 查找所有微博的父容器
        weibo_containers = soup.find_all('div', attrs={'data-index': re.compile(r'^\d+$')})

        print(f"找到 {len(weibo_containers)} 条微博内容")

        weibo_data = []

        for idx, container in enumerate(weibo_containers, start=1):
            try:
                # 提取发布时间
                time_element = container.find('a', class_=re.compile(r'^head-info_time_'))
                time_text = time_element.get_text(strip=True) if time_element else "未知时间"

                # 提取微博内容
                content_element = container.find('div', class_=re.compile(r'^detail_text_'))
                content_text = content_element.get_text(strip=True) if content_element else "无内容"

                # 提取微博标题（如果有）
                title_element = container.find('div', class_=re.compile(r'^card-article_cut2_'))
                title_text = title_element.get_text(strip=True) if title_element else "无标题"

                weibo_data.append({
                    'time': time_text,
                    'title': title_text,
                    'content': content_text
                })
            except Exception as e:
                print(f"第 {idx} 条微博抓取出错: {e}")

        # 检查是否抓取到数据
        if not weibo_data:
            print(f"未抓取到关于 '{keyword}' 的任何微博数据，请检查选择器是否正确。")
        else:
            # 将结果保存到文件，每个关键词一个文件
            output_path = f'C:/Users/xxxxxxxxxxx/Desktop/weibo_scraper/{keyword}_weibo_report.txt'  #输出目录
            with open(output_path, 'w', encoding='utf-8') as f:
                for weibo in weibo_data:
                    f.write(f"发布时间: {weibo['time']}\n")
                    f.write(f"标题: {weibo['title']}\n")
                    f.write(f"内容: {weibo['content']}\n")
                    f.write("="*50 + "\n")

            print(f"微博数据已保存到 {output_path}")
            saved_files.append(output_path)  # 记录保存的文件路径

        # 重置页面，准备搜索下一个关键词
        driver.get('about:blank')
        time.sleep(2)

    finally:
        print(f"关键词 '{keyword}' 处理完成。")

# 关闭浏览器
driver.quit()

# 合并所有生成的txt文件
merged_output_path = 'C:/Users/xxxxxxx/Desktop/weibo_scraper/merged_weibo_report.txt'  #输出目录

with open(merged_output_path, 'w', encoding='utf-8') as merged_file:
    for file_path in saved_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            merged_file.write(f.read())
            merged_file.write("\n\n")  # 添加换行以分隔每个文件的内容

print(f"所有微博数据已合并到 {merged_output_path}")
