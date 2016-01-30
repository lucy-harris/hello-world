import random,urllib2
activities_to_do=['a','b','c']
activities_to_do = urllib2.urlopen('https://raw.githubusercontent.com/bellcodo/potential-octo-chainsaw/master/code_activities_we_like.lst').read()
activities_to_do=activities_to_do.split()
print     activities_to_do       
going_to_do=random.choice(activities_to_do)
print going_to_do
  
