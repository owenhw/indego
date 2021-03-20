from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from scraping.models import Report



class Command(BaseCommand):
    # define a function to get the page content
    def fetch(self):
        headers = {'user-agent' : 'OwenHW@gmail.com'}

        return requests.get('https://www.rideindego.com/about/data'
                            , headers=headers)


    # define a function to parse the page content
    def parse(self, request):
        soup = BeautifulSoup(request.content, 'html.parser')
        # use css tags to select the links for each fiscal quarter's dataset

        containers = soup.select(
            '#post-535 > section > ul:nth-child(4) > li > a'
        )

        # return the link objects
        return containers


    # define a function to record each link
    def record(self, report_links):
        for report in report_links:
            url = report['href']
            title = report.text

            # check to see if the url is already in db
            # this could probably break easily
            try:
                #save in db
                Report.objects.create(
                    url=url,
                    title=title
                )
                print(f'{title} report entered')
            except:
                print('duplicate report ignored')


    # define logic of command
    def handle(self, *args, **options):
        content = self.fetch()

        if content.status_code == 200:
            links = self.parse(content)
            self.record(links)
            self.stdout.write('scraping complte')
            
        else:
            self.stdout.write( f'bad request : {content.status_code}')
