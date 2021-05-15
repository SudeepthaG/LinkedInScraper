import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters
import csv

# Change root logger level (default is WARN)
logging.basicConfig(level = logging.INFO)


def on_data(data: EventData):
    # print('[ON_DATA]', data.title, data.company, data.date, data.link, len(data.description))
    # print(data)
    with open('results.csv', mode='a+') as csv_file:
        fieldnames = ['job_id', 'link', 'apply_link', 'title', 'company', 'place', 'description', 'date', 'seniority_level', 'job_function','employment_type', 'industries']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        #
        # writer.writeheader()
        writer.writerow({'job_id':data.job_id, 'link':data.link, 'apply_link':data.apply_link, 'title':data.title, 'company':data.company, 'place':data.place, 'description':data.description, 'date':data.date, 'seniority_level':data.seniority_level, 'job_function':data.job_function,'employment_type':data.employment_type, 'industries':data.industries})



def on_error(error):
    print('[ON_ERROR]', error)


def on_end():
    print('[ON_END]')


scraper = LinkedinScraper(
    chrome_executable_path="/Users/sudeepthamouniganji/Desktop/chromedriver", # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver)
    chrome_options=None,  # Custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=2,  # Slow down the scraper to avoid 'Too many requests (429)' errors
    # proxies=[
    #         'http://localhost:6666',
    #         'http://localhost:7777',
    # ]
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

queries = [
    # this query uses no filter and gives 27 jobs aross world in any company and job.
    Query(
        options=QueryOptions(
            optimize=True,  # Blocks requests for resources like images and stylesheet
            limit=27  # Limit the number of jobs to scrape
        )
    ),

    # this query uses no filter and gives 50 jobs across US in any company and any job. The results.csv is currently based on running this query
    Query(
        options=QueryOptions(
            locations=['United States'],
            optimize=True,  # Blocks requests for resources like images and stylesheet
            limit=50  # Limit the number of jobs to scrape
        )
    ),
    # this query uses filters and gives 5 jobs in u.s in particular company
    Query(
        query='Engineer',
        options=QueryOptions(
            locations=['United States'],
            optimize=False,
            limit=5,
            filters=QueryFilters(
                company_jobs_url='https://www.linkedin.com/jobs/search/?f_C=162479&geoId=92000000',
                # Filter by companies
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                experience=None,
            )
        )
    ),
    
    Query(
        query='Software Engineer',
        options=QueryOptions(
            locations=['United States'],
            optimize=False,
            limit=5,
            filters=QueryFilters(
                company_jobs_url='https://www.linkedin.com/jobs/search/?f_C=162479&geoId=92000000',
                # Filter by companies
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                experience=None,
            )
        )
    ),
    Query(
        query='Data Scientist',
        options=QueryOptions(
            locations=['United States'],
            optimize=False,
            limit=5,
            filters=QueryFilters(
                company_jobs_url='https://www.linkedin.com/jobs/search/?f_C=162479&geoId=92000000',
                # Filter by companies
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                experience=None,
            )
        )
    ),
    Query(
        query='Data Analyst',
        options=QueryOptions(
            locations=['United States'],
            optimize=False,
            limit=5,
            filters=QueryFilters(
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                experience=None,
            )
        )
    ),
]

scraper.run(queries)
