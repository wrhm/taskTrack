# taskTrack.py
# Author: William Howard Matchen
# Created: 04Feb2016
# Last edit: 05Feb2016

'''
TODOs
 	- let user edit settings from within shell
 	- Can't add duedates beyond a week from today
 	- Removal matches don't prompt chronologically.
 	- add "ditto" feature
 	- if token is today's DOW, return ord of 1wk from today
 	- add case insensitivity
 	- have different todo lists
 	- have completed task history, per list

Reference: https://docs.python.org/2/library/datetime.html
'''

from datetime import date
import string

dayOfWeek = ['monday','tuesday','wednesday',
			'thursday','friday','saturday','sunday','today','tomorrow']

def dispHelp():
	print ''
	print 'Valid commands:'
	print ' - "add task [, day]": add a new task to the list'
	print ' - "exit"/"quit": exit the shell'
	print ' - "help": show this message'
	print ' - "rm/rem(ove)/del(ete)/did desc": removes a task matching desc'
	print ' - "show": display all tasks'
	print ''

def loadSettings():
	f = open('settings.txt','r')
	lines = f.readlines()
	f.close()
	d = dict()
	for line in lines:
		[s,v] = line.split()
		d[s] = v
	return d

def getDesc(line):
	return ' '.join(line.split()[:-1])

def showTasks():
	f = open('list.txt','r')
	show_list = f.readlines()
	f.close()
	print '\nAll tasks:',
	if len(show_list) == 0:
		print 'None! Congrats!'
	else:
		print ''
	#The next line sorts tasks chronologically
	sorted_list = sorted(show_list, key=lambda x: x.split()[-1])
	for e in sorted_list:
		desc,ordinal = getDesc(e),int(e.split()[-1])
		# print ' - %s'%e,
		if ordinal == 0:
			print ' - "%s"'%(desc)
		else:	
			formatted = date.fromordinal(ordinal).strftime("%a %d %b %Y")
			print ' - "%s" due %s'%(desc,formatted)
	print ''

#Returns the ordinal of the next occurrence of day
def nextDOW(tokens):
	t_ord = date.today().toordinal()
	token = tokens[-1]
	if token not in dayOfWeek:
		return None
	if token == 'today':
		return t_ord
	if token == 'tomorrow':
		return t_ord + 1
	day = dayOfWeek.index(token)
	while date.fromordinal(t_ord).timetuple()[6] != day:
		t_ord = t_ord + 1
	#if tokens[-2] == 'next' and day < :
	#	return t_ord + 7
	return t_ord

print '\n================='
print '==  TaskTrack  =='
print '=================\n'

print 'Loading settings...'
settings = loadSettings()
print 'Settings loaded:'
for val in settings:
	print ' - %s=%s'%(val, settings[val])
print 'Type "help" for help.'

if settings['showOnStart'] == 'True':
	showTasks()
else:
	print ''

response = ''
while response not in ['exit', 'quit']:
	response = raw_input('>> ')
	
	tokens = response.split()
	if tokens[0] == 'help':
		dispHelp()
	elif len(tokens) == 1 and tokens[0] not in ['show']:
		dispHelp()
	elif tokens[0] == 'add':
		f = open('list.txt','a')
		if tokens[-1] in dayOfWeek:
			ordinal = nextDOW(tokens)
			f.write('%s %d\n'%(' '.join(tokens[1:-1]),ordinal))
		# MDY
		# elif len(tokens) >= 5:
		# 	print '### Feature in Dev ###'
		# 	mdy = mdy(tokens[-3:])
		# 	if mdy != None:
		# 		(m,d,y) = mdy
		# 		ordinal = date(y,m,d).toordinal()
		# 		f.write('%s %d\n'%(' '.join(tokens[1:-2]),ordinal))
		else:
			f.write('%s %d\n'%(' '.join(tokens[1:]),0))
		f.close()
		if settings['showOnAdd'] == 'True':
			showTasks()
	elif tokens[0] == 'show':
		showTasks()
	elif tokens[0] in ['remove','delete','rem','del','did','rm']:
		f = open('list.txt','r')
		show_list = f.readlines()
		f.close()
		tbr = string.lower(' '.join(tokens[1:]))
		match = None
		for e in show_list:
			if tbr in e:
				match = e
				break
		if match == None:
			print 'No tasks match "%s".'%tbr
		else:
			for e in show_list:
				if tbr in string.lower(e):
					if raw_input('Remove "%s" (Y/N)? '%getDesc(e))[0] in ['Y','y']:
						f = open('list.txt','w')
						for line in show_list:
							if line != e:
								f.write(line)
						f.close()
						print '"%s" was removed.'%getDesc(e)
						break
		if settings['showOnRem'] == 'True':
			showTasks()
	else:
		dispHelp()