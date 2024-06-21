import os
from bs4 import BeautifulSoup
import json
from playwright.sync_api import sync_playwright
import time

def login_and_extract_urls(email, password, url, output_file):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://www.facebook.com/login')
        page.fill('input[name="email"]', email)
        page.fill('input[name="pass"]', password)
        with page.expect_navigation():
            page.click('button[name="login"]')
        page.goto(url, wait_until="networkidle")
        time.sleep(5)

        a_tag_selector = '.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1sur9pj.xkrqix3.xzsf02u.x1s688f'
        a_tags = page.query_selector_all(a_tag_selector)
        urls = [a.get_attribute('href') for a in a_tags[:10]]

        with open(output_file, 'w', encoding='utf-8') as file:
            for url in urls:
                file.write(url + '\n')
            print(f"First 10 URLs saved to {output_file}")

        browser.close()

def login_and_save_content(email, password, url, output_file):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://www.facebook.com/login')
        page.fill('input[name="email"]', email)
        page.fill('input[name="pass"]', password)
        with page.expect_navigation():
            page.click('button[name="login"]')
        page.goto(url, wait_until="networkidle")

        see_more_button_selector = 'div.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1sur9pj.xkrqix3.xzsf02u.x1s688f[role="button"]'
        if page.is_visible(see_more_button_selector):
            page.click(see_more_button_selector)
            print("Clicked the 'See More' button.")
            time.sleep(4)

        specific_divs_selector = '.html-div.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd'
        specific_divs = page.query_selector_all(specific_divs_selector)
        divs_html = [div.inner_html() for div in specific_divs]

        with open(output_file, 'w', encoding='utf-8') as file:
            for div_html in divs_html:
                file.write(div_html + '\n')
            print(f"Specific divs content saved to {output_file}")

        browser.close()

def extract_content(file_path, start_marker, end_marker):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            start_index = content.find(start_marker)
            if start_index == -1:
                print("Start marker not found.")
                return

            start_index += len(start_marker)
            end_index = start_index + 400
            if end_index == -1:
                print("End marker not found.")
                return

            extracted_content = content[start_index:end_index].strip()
            print("Extracted Content:")
            return extracted_content

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_to_json(html_content, nameFile, folder):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator="\n")
    reversed_text = text

    data = {'reversed_text': reversed_text}
    json_path = os.path.join(folder, f'{nameFile}.json')
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print(f"Text has been reversed and saved to {json_path}")

def process_user_profiles(email, password, url_file, start_marker, end_marker, company_name):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://www.facebook.com/login')
        page.fill('input[name="email"]', email)
        page.fill('input[name="pass"]', password)
        with page.expect_navigation():
            page.click('button[name="login"]')

        if not os.path.exists(company_name):
            os.makedirs(company_name)

        with open(url_file, 'r', encoding='utf-8') as file:
            urls = file.readlines()

        for url in urls:
            url = url.strip()
            print(f"Processing URL: {url}")
            page.goto(url, wait_until="networkidle")
            time.sleep(3)

            specific_divs_selector = '.html-div.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd'
            specific_divs = page.query_selector_all(specific_divs_selector)
            divs_html = [div.inner_html() for div in specific_divs]

            output_file = os.path.join(company_name, f'{url.split("/")[-1]}.txt')
            with open(output_file, 'w', encoding='utf-8') as file:
                for div_html in divs_html:
                    file.write(div_html + '\n')
                print(f"Specific divs content saved to {output_file}")

            html_content = extract_content(output_file, start_marker, end_marker)
            if html_content:
                extract_to_json(html_content, url.split("/")[-1], company_name)

        browser.close()

# Personal connection email and password
email = 'xxxxxxx@gmail.com'  
password = 'xxxxxx!'  

# Step 1: Extract URLs from search results
company_name = 'Microsoft'
search_url = f'https://www.facebook.com/search/people/?q={company_name}'
url_output_file = 'list_users.txt'
login_and_extract_urls(email, password, search_url, url_output_file)

# Step 2: Process each user profile URL
start_marker = 'class="xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a'
end_marker = 'class="html-div xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6"'
process_user_profiles(email, password, url_output_file, start_marker, end_marker, company_name)
