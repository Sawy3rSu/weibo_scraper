### **README (中文版本)**

---

#### **项目概述：**

该脚本可以自动化搜索微博上基于多个关键词的帖子。通过使用 Selenium WebDriver 来控制 Chrome 浏览器，脚本能够执行搜索、模拟滚动加载更多内容、点击“展开”按钮展开长微博，最后提取每个关键词的相关微博数据（发布时间、标题、内容）并分别保存到不同的文本文件中。

#### **运行环境要求：**

1. 你的系统上需要安装 Python 3.x。
2. 需要安装以下 Python 库：
   - `selenium`
   - `beautifulsoup4`
   - `requests`
   - `python-docx`（可选，如果希望将内容保存为 `.docx` 文件）
   - `re`
   - `time`

   使用以下命令安装这些库：

   ```bash
   pip install selenium beautifulsoup4 requests python-docx
   ```

3. 安装 Chrome 浏览器和 Chrome WebDriver，确保 `chromedriver` 的版本与 Chrome 浏览器的版本一致。下载地址：[点击这里](https://sites.google.com/a/chromium.org/chromedriver/)。

4. 脚本使用本地 Chrome 用户数据避免手动登录微博。默认路径为：
   
   ```
   C:/Users/Yi/AppData/Local/Google/Chrome/User Data
   ```

   请对该路径进行修改，确保与您的系统相符，。

#### **脚本运行步骤：**

1. **编辑关键词**：你希望搜索的关键词应该在脚本开始的 `keywords` 列表中定义。你可以根据需要添加、删除或修改这些关键词。
   ```python
   keywords = ['关键词1', '关键词2', '关键词3']
   ```

2. **运行脚本**：在终端中执行以下命令运行 Python 脚本：
   ```bash
   python script_name.py
   ```

3. **输出结果**：
   - 对于 `keywords` 列表中的每个关键词，脚本将搜索相应的微博帖子，抓取数据并保存为以 `{关键词}_weibo_report.txt` 命名的文本文件。
   - 输出文件将保存在以下目录：
     ```
     C:/Users/Yi/Desktop/
     ```

4. **结果格式**：每个文件将包含抓取到的微博信息，包括：
   - **发布时间**：微博发布的时间。
   - **标题**：微博的标题（如果有）。
   - **内容**：微博的完整内容。

#### **定制说明：**
- 你可以根据网络速度修改 `time.sleep()` 值，来调整页面加载和滚动的时间。
- 如果遇到不同结构的微博内容，可能需要更新 `BeautifulSoup` 的选择器。

---

#### **使用示例：**

如果 `keywords` 列表包含以下内容：
```python
keywords = ['aaa', 'bbb', 'ccc']
```
脚本将生成三个单独的文件：
1. `aaa_weibo_report.txt`
2. `bbb_weibo_report.txt`
3. `ccc_weibo_report.txt`

每个文件将包含与相应关键词相关的所有抓取到的微博帖子。

最后会将多个txt文件合并并保存为merged_weibo_report.txt。

---

### **README (English Version)**

---

#### **Project Overview:**

This script automates the process of searching and extracting Weibo posts based on multiple keywords. Using the Selenium WebDriver to control a Chrome browser, the script performs searches, simulates scrolling for loading more content, clicks on "expand" buttons for long posts, and then extracts and saves the relevant Weibo data (time, title, content) for each keyword into separate text files.

#### **Requirements:**

1. Python 3.x installed on your system.
2. The following Python libraries:
   - `selenium`
   - `beautifulsoup4`
   - `requests`
   - `python-docx` (optional, used if you want to save to `.docx`)
   - `re`
   - `time`

   Install these packages using the command:

   ```bash
   pip install selenium beautifulsoup4 requests python-docx
   ```

3. Chrome browser and Chrome WebDriver. Ensure the `chromedriver` version matches your Chrome browser version. Download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).

4. Use your local Chrome user data to avoid manual login to Weibo. The script uses the following path:
   
   ```
   C:/Users/Yi/AppData/Local/Google/Chrome/User Data
   ```

   Ensure you modify the path to match your system if necessary.

#### **Script Execution:**

1. **Edit Keywords**: The keywords you wish to search for should be defined in the `keywords` list at the start of the script. You can add, remove, or modify these keywords as needed.
   ```python
   keywords = ['keyword1', 'keyword2', 'keyword3']
   ```

2. **Run the Script**: Execute the Python script in your terminal:
   ```bash
   python script_name.py
   ```

3. **Outputs**: 
   - For each keyword in the `keywords` list, the script will search the corresponding Weibo posts, scrape the data, and save the results in a text file named as `{keyword}_weibo_report.txt`.
   - The output files will be saved in the directory:
     ```
     C:/Users/Yi/Desktop/
     ```

4. **Results**: Each file will contain the scraped information about Weibo posts, including:
   - **Post Time**: Time the post was made.
   - **Title**: The title of the post (if available).
   - **Content**: The full content of the post.

#### **Customization:**
- You can adjust the timing for page loading and scrolling by modifying `time.sleep()` values according to your network speed.
- To handle different types of post structures, you might need to update the `BeautifulSoup` selectors.

---

#### **Usage Example:**

If your `keywords` list contains:
```python
keywords = ['information security', 'mid-autumn festival', 'national day']
```
The script will create three separate files:
1. `information_security_weibo_report.txt`
2. `mid_autumn_festival_weibo_report.txt`
3. `national_day_weibo_report.txt`

Each file will contain all the posts scraped related to the respective keyword.

---

This **README** file provides guidance on how to set up and run the Weibo scraping automation script both in English and Chinese versions.
