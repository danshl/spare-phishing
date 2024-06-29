import requests
from bs4 import BeautifulSoup
import json

def extract_linkedin_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the name
    name_tag = soup.find('h1', {'class': 'top-card-layout__title'})
    name = name_tag.text.strip() if name_tag else "N/A"

    # Extract the "About" section
    about_tag = soup.find('div', {'class': 'VMvxltwDKHWDfbJsrvgPqoGbtVbSMaE'})
    about = about_tag.text.strip() if about_tag else "N/A"

    # Extract the education
    education_section = soup.find('section', {'id': 'education-section'})
    education = []
    if education_section:
        schools = education_section.find_all('li', {'class': 'result-card'})
        for school in schools:
            school_name = school.find('h3').text.strip()
            degree = school.find('p', {'class': 'degree'}).text.strip() if school.find('p', {'class': 'degree'}) else ''
            field_of_study = school.find('p', {'class': 'field-of-study'}).text.strip() if school.find('p', {'class': 'field-of-study'}) else ''
            education.append({
                'school_name': school_name,
                'degree': degree,
                'field_of_study': field_of_study
            })

    # Extract interests
    interests_section = soup.find('section', {'id': 'interests'})
    interests = []
    if interests_section:
        interest_items = interests_section.find_all('li', {'class': 'entity-list-item'})
        for interest_item in interest_items:
            interest_name = interest_item.find('span', {'class': 'pv-entity__summary-title'}).text.strip()
            interests.append(interest_name)

    # Extract posts
    posts = []
    post_links = soup.find_all('a', {'class': 'app-aware-link'})
    for idx, post_link in enumerate(post_links):
        aria_label = post_link.get('aria-label')
        if aria_label and 'View full post.' in aria_label:
            post_content = aria_label.split('View full post.')[1].strip()
            posts.append({
                'post_id': idx + 1,
                'content': post_content
            })

    linkedin_data = {
        'name': name,
        'about': about,
        'education': education,
        'interests': interests,
        'posts': posts
    }

    return linkedin_data

# URL of the LinkedIn profile page
linkedin_url = 'https://www.linkedin.com/in/danshl/'

# Extract LinkedIn data
linkedin_data = extract_linkedin_data(linkedin_url)

# Convert to JSON
linkedin_json = json.dumps(linkedin_data, ensure_ascii=False, indent=4)

# Print the JSON
print(linkedin_json)

# Optionally save to a file
with open('linkedin_data.json', 'w', encoding='utf-8') as f:
    f.write(linkedin_json)


profile_url = 'https://www.linkedin.com/in/danshl/'
