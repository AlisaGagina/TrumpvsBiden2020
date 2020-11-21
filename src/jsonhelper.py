import json

def open_many_jsons(jfile):
	jlist=[]
	with open(jfile, 'r') as f:
		for line in f:
			try: jline=json.loads(line)
			except ValueError as e: continue
			jlist.append(jline)
	return jlist
def dump_many_jsons(jlist, jname):
	with open(jname, 'w') as f:
		for line in jlist:
			print(json.dumps(line), file=f)

