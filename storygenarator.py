import random

when = ['A few years ago','yesterday','Last night','A long time ago','On 20th Jan']
who= ['A guy ','An animal','A beast','A wanderer']
name= ['Alission','Hoouk','Meruem','Starwalker']
residence=['Madrid','Los angeles','Germany','Candice']
went_to=['movie theatre','party hall','school','house']
what_happend_there=['solved a mystery','wrote a diary about himeself','ate a meal','found a hidden passage way']

print(random.choice(when)+ ', ' + random.choice(who) + ' named ' + random.choice(name) + ' who lived in ' + random.choice(residence) + ', went to a ' + random.choice(went_to) + ' and '  + random.choice(what_happend_there)  + ".")