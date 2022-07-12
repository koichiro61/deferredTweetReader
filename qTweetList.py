import datetime
from datetime import timedelta

class qTweetList:

	statusList = [] # list of status fetched by 'usertimeline' method
	queuedTime = datetime.datetime.min
	
	def __init__(self, stl=[], qt=datetime.datetime.min):
		statusList = stl
		queuedTime = qt
		
	def show(self, time_zone):
		for i in reversed(range(0, len(self.statusList))):
			#print('\n{:02d}:{}{}'.format(i,'-'*30, self.statusList[i].id))
			print('\n{:02d}:{}'.format(i,'-'*50))
			ctutc = self.statusList[i].created_at
			ct = ctutc.astimezone(time_zone)		
			print('author: {} created at {}\n'.
				format(	self.statusList[i].user.screen_name, ct))
			print(self.statusList[i].text)
			
		print('\nqueued at {}\n'.format(self.queuedTime.strftime('%Y-%m-%d %H:%M:%S%z')))
