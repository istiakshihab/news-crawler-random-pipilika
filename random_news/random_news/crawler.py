from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler

from spiders.titleprothomalo import ProthomAloTSpider
from spiders.titlebanglabdnews import BanglaBdnewsTSpider
from spiders.titlebanglatribune import BanglatribuneTSpider
from spiders.paraprothomalo import ProthomAloPSpider
from spiders.parabanglatribune import BanglatribunePSpider
from spiders.parabanglabdnews import BanglaBdnewsPSpider

job_defaults = {'max_instances': 3}

process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
            'FEED_URI': 'output_file.csv',
            'FEED_FORMAT': 'csv',
        })

# process = CrawlerProcess({
#     'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',

# })

sched = TwistedScheduler(job_defaults=job_defaults)
ptime = 0
ttime= 0

sched.add_job(process.crawl, 'interval', args=[ProthomAloTSpider], minutes=ttime)
sched.add_job(process.crawl, 'interval', args=[BanglaBdnewsTSpider], minutes=ttime)
sched.add_job(process.crawl, 'interval', args=[BanglatribuneTSpider], minutes=ttime)
sched.add_job(process.crawl, 'interval', args=[ProthomAloPSpider], minutes=ptime)
sched.add_job(process.crawl, 'interval', args=[BanglatribunePSpider], minutes=ptime)
sched.add_job(process.crawl, 'interval', args=[BanglaBdnewsPSpider], minutes=ptime)
sched.start()
process.start(False)
