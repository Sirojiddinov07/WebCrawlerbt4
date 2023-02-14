from bs4 import BeautifulSoup
import requests
import time


print('put some skill that you are not famillar with')
unfamiliar_skill = input('>>>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml' )
    jobs = soup.find_all('li', class_ ="clearfix job-bx wht-shd-bx")
    for i, job in enumerate(jobs):
        published_date = job.find('span', class_ ='sim-posted').span.text
        if 'few' in published_date:
            campany_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{i}.txt', 'w') as f:
                    f.write(f'Company Name: {campany_name.strip()} \n')
                    f.write(f'Required  skill: {skills.strip()} \n')
                    f.write(f'more info: {more_info}')

                print(f'File saved: {i}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes ...')
        time.sleep(time_wait*60)
