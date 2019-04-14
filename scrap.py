from selenium import webdriver
import pandas as pd

my_url = 'https://techolution.app.param.ai/jobs/'

driver = webdriver.PhantomJS()
driver.get(my_url)

# returns all the job cards present in the url
jobs = driver.find_elements_by_class_name('job_list_card')

job_details = []
job_name = []
job_type = []
job_location = []
job_experience = []
job_days = []

# extracts required information from the job cards and store them in lists
for job in jobs:
    job_details = job.text
    job_details = job_details.split('\n')
    job_name.append(job_details[0])
    job_type.append(job_details[1].split(' · ')[0])
    job_location.append(job_details[1].split(' · ')[1])
    job_experience.append(job_details[1].split(' · ')[2])

# The following code extracts number of days attribute for each job
days = 0
date_posted = driver.find_elements_by_xpath('//span[@class="date_posted"]')
for date in date_posted:
    date_contents = date.get_attribute('textContent').split(' ')
    # converting the extracted data into number of days 
    if(date_contents[1] == 'month'):
        days = 30
    elif(date_contents[1] == 'days'):
        days = int(date_contents[0])
    elif(date_contents[1] == 'months'):
        days = int(date_contents[0])*30
    job_days.append(str(days) + ' days')

# creates a dictonary using the above lists 
data_dict = {'title':job_name, 'type':job_type, 'location':job_location, 'experience':job_experience, 'job_posted':job_days}
# converting dictonary into pandas dataframe
df = pd.DataFrame(data_dict)
# sorting the dataframe based on job posted coloumn
df.sort_values('job_posted')
# storing the dataframe to csv file
df.to_csv('out.csv', encoding='utf-8',index=False)