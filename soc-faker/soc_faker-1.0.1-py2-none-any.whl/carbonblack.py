###
###
## This script is optimized for Carbon Black Defense queries.  Different products will have different query syntax.
## User will need to modify this script to generate queries in their tool's query language for a given IOC.
###
###


import pendulum

### INPUTS MUST BE MAPPED IN SCRIPT INPUTS IN INTEGRATIONS EDITOR ###
ingestion_time = sw_context.inputs['ingestion_time']
indicator = sw_context.inputs['indicator']
indicator_type = sw_context.inputs['indicator_type']
### /INPUTS ###

start_time = pendulum.parse(ingestion_time).add(days=-14).to_iso8601_string() # begin search 2 weeks earlier than indicator discovered.
end_time = pendulum.now().to_iso8601_string()



if indicator_type == "URL":
  query_prefix = None		# Full URL not supported in CB
  query_prefix = 'domain'
  indicator=indicator.split('//')[-1].split('/')[0]
elif indicator_type == "DOMAIN":
  query_prefix = 'domain'
elif indicator_type == "IP":
  query_prefix = 'ipaddr'
elif indicator_type == "EMAIL": 
  query_prefix = None # not supported in CB
  query_prefix = 'email' # Example for email syntax, if exists
elif indicator_type == "HASH":
  query_prefix = 'md5'
else:
  query_prefix = None
  
if query_prefix:
  q = "{}:{} AND last_server_update:[{} TO {}]".format(query_prefix, indicator, start_time, end_time)
else:
  q = None


if q:
  sw_outputs.append({'query':q, 'query_start_time':start_time, 'query_end_time':end_time})






  ###
###
## THIS SCRIPT IS A PLACEHOLDER INTENDED TO SIMULATE RESULTS FROM CARBON BLACK DEFENSE. REPLACE THIS TASK WITH A TASK
## THAT EXECUTES THE QUERY AGAINST YOUR SIEM/TOOL AND RETURNS THE RESULTS THAT ARE NEEDED TO GENERATE A REPORT AS A JSON OBJECT.
###
## The JSON object should look like [{'id':'result1','ip':'127.0.0.1'}, {'id':'result2','ip':'192.168.1.1'}] with results
## and like [] if there are no results (i.e. don't return None, return "[]" on negative)
###
###

import random
import json
import string
import re
import pendulum


### INPUTS MUST BE MAPPED IN SCRIPT INPUTS IN INTEGRATIONS EDITOR ###
indicator = sw_context.inputs['indicator']
indicator_type = sw_context.inputs['indicator_type']
query = sw_context.inputs['query']

sTime = sw_context.inputs['query_start_time']
eTime = sw_context.inputs['query_end_time']
### /INPUTS ###

start_time = pendulum.parse(sTime)
end_time = pendulum.parse(eTime)
time_diff = start_time.diff(end_time, True)
time_diff_min = time_diff.in_minutes()


def generateHex(digits):
    return "".join([random.choice(string.hexdigits) for n in xrange(digits)]).lower()


def generateNumbers(digits):
    return "".join([random.choice(string.digits) for n in xrange(digits)]).lower()


workstations = {}
for _ in range(100):
    firstname = random.choice(['Liam', 'Noah', 'William', 'James', 'Logan', 'Benjamin', 'Mason', 'Elijah', 'Oliver', 'Jacob', 'Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Evelyn', 'Abigail'])
    lastname = random.choice(['Smith', 'Taylor', 'Hayes', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Johnson', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'Williams', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Jones', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Brown', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Davis', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Miller', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Wilson', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Moore', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz'])
      
    finit = firstname[:1]
    username = "{}{}".format(finit.lower(), lastname.lower())

    workstations["SWIMLANE\\WS-{}-{}".format(username, generateHex(6))] = {
        'username': username,
        'fullname': "{} {}".format(firstname, lastname),
        'ip_addr': "192.168.{}.{}".format(random.randint(1, 250), random.randint(1, 250)),
    }

clean_programs = [
    r'C:\Program Files\Microsoft Office\root\Office16\Winword.exe',
    r'C:\Program Files\Microsoft Office\root\Office16\Outlook.exe',
    r'C:\Program Files\Microsoft Office\root\Office16\Excel.exe',
    r'C:\Program Files\Microsoft Office\root\Office16\Powerpoint.exe',
    r'C:\Program Files\Microsoft Office\root\Office16\Access.exe',
    r'C:\Program Files (x86)\Slack\Slack.exe',
    r'C:\Program Files\Google\Chrome\Chrome.exe',
    r'C:\Program Files\Microsoft Internet Explorer\iexplore.exe',
    r'C:\Windows\System32\LSASS.exe',
    r'C:\Windows\System32\rundll32.exe',
]

clean_program_filenames = [
    'chrome.exe',
    'powerpoint.exe',
    'iexplore.exe',
    'explorer.exe',
    'outlook.exe',
    'acrobat.exe',
    'rundll32.exe',
]

dirty_programs = []
dirty_program_paths = [
    r'C:\TEMP\1',
    r'C:\Users\Administrator',
    r'C:\Users\Local',
    r'C:',
]
dirty_program_filenames = [
    'temp.exe',
    'temp.hta',
    'installer.exe',
    'quick_install.exe',
    'chrome.exe',
    'adobe.exe',
]
for _ in range(10):
    dirty_program_filenames.append('{}.exe'.format(generateHex(random.randint(16, 32))))
    dirty_program_filenames.append('{}.exe'.format(generateNumbers(random.randint(1, 20))))
    dirty_program_filenames.append('{}.hta'.format(generateHex(random.randint(16, 32))))
    dirty_program_filenames.append('{}.hta'.format(generateNumbers(random.randint(1, 20))))

for _ in range(100):
    dirty_programs.append(r"{}\{}".format(random.choice(dirty_program_paths), random.choice(dirty_program_filenames)))


def generateResults():
    prog = "\"{}\"".format(random.choice(clean_programs + dirty_programs))
    file = re.sub(r'^.*\\', '', prog).strip('"')
    prog_start = start_time.add(minutes=random.randint(1, time_diff_min - 60)).add(seconds=random.randint(-59, 0))
    prog_end = prog_start.add(seconds=random.randint(30, 600))
    ws_key = random.choice(list(workstations))


    ws = workstations[ws_key]
    uname = ws['username']
    ip = ws['ip_addr']
    
    r = {
        "process_md5": indicator if indicator_type == "HASH" else generateHex(32),
        "cmdline": prog,
        "hostname": ws_key,
        "start": prog_start.to_iso8601_string(),
        "interface_ip": ip,
        "process_pid": generateNumbers(4),
        "username": "{}".format(uname),
        "last_server_update": prog_end.to_iso8601_string(),
        "unique_id": "{}-{}-{}-{}-{}".format(generateHex(8), generateHex(4), generateHex(4), generateHex(4), generateHex(12)),
        "domain": indicator if indicator_type == "DOMAIN" else None,
        "ip_addr": indicator if indicator_type == "IP" else None,
    }
    return r

results = []
if random.randint(0, 1) == 1: # only generate hits in 50% of queries.
    for _ in range(random.randint(0, 20)):
        results.append(generateResults())

sw_outputs.append({'query_results': "{}".format(json.dumps(results))})










###
###
## This script requires modification to match the JSON elements of your SIEM output.  Make changes in the commented section below.
## The fields will match the output in your JSON structure that comes out of the "TH: Execute Query" task
###
###


import json, pendulum

### EDIT THIS SECTION FOR YOUR SIEM'S METADATA VALUES AND TITLES ###
meta = { 
        'Event ID': 'unique_id',  # Human Label : json_key
        'Hostname': 'hostname',
        'Username': 'username',
        'Command Line': 'cmdline',
        'Process PID' : 'process_pid',
        'Execution Start': 'start',
        'Execution End': 'last_server_update',
        'Process Hash': 'process_md5',
        'Domain(s) Contacted': 'domain',
        'IP Address(es) Contacted': 'ip_addr',
}
### /EDIT ###

### INPUTS MUST BE MAPPED IN SCRIPT INPUTS IN INTEGRATIONS EDITOR ###

indicator = sw_context.inputs['indicator']
indicator_type = sw_context.inputs['indicator_type']
ingestion_time = sw_context.inputs['ingestion_time']

query = sw_context.inputs['query']
query_results_json = sw_context.inputs['query_results']

sTime = sw_context.inputs['query_start_time']
eTime = sw_context.inputs['query_end_time']

### /INPUTS ###

try:
    query_results = json.loads(query_results_json)
except:
    query_results = []

case_start_time = None
case_end_time = None
affected_resources = []
    
res_num = len(query_results)
if res_num > 0:
    r = "=== AUTOMATED INCIDENT REPORT ===\n\n"
    r += "Swimlane ingested the indicator {} [{}] at {}.\nSwimlane identified this indicator as a positive indicator of malicious activity, and ran automated queries in Carbon Black Defense.\n\n".format(indicator, indicator_type, ingestion_time)
    r += "Query Parameters: \n    Query: {}\n    Query Start Time: {}\n    Query End Time: {}\n\n".format(query, sTime, eTime)
    r += "The following {} results were obtained:\n\n".format(len(query_results))

    resultNum = 1
    for result in query_results:
        r += "Result # {}\n".format(resultNum)
        for header, key in meta.iteritems():
            if header == 'Execution Start' and result[key]:
                cur_start_time = pendulum.parse(result[key])
                if case_start_time is None or (case_start_time and cur_start_time < case_start_time):
                    case_start_time = cur_start_time
            elif header == 'Execution End' and result[key]:
                cur_end_time = pendulum.parse(result[key])
                if case_end_time is None or (case_end_time and cur_end_time > case_end_time):
                    case_end_time = cur_end_time
            elif header == 'Hostname':
                if result[key] and result[key] not in affected_resources:
                    affected_resources.append(result[key])
            r += "    {}: {}\n".format(header, result[key])
        resultNum += 1
        r += "\n"

    r += "=== END AUTOMATED INCIDENT REPORT ===\n\n"

else:
    r = "=== AUTOMATED INVESTIGATION REPORT ===\n\n"
    r += "Swimlane ingested the indicator {} [{}] at {}.\nSwimlane identified this indicator as a positive indicator of malicious activity, and ran automated queries in Carbon Black Defense.\n\n".format(indicator, indicator_type, ingestion_time)
    r += "Query Parameters: \n    Query: {}\n    Query Start Time: {}\n    Query End Time: {}\n\n".format(query, sTime, eTime)
    r += "No results were found.\n\n"
    r += "=== END AUTOMATED INVESTIGATION REPORT ===\n\n"

title = "IOC SEARCH: {} - {} RESULTS".format(indicator, res_num)


# Decide severity based on number of affected resources/hostnames
ar_num = len(affected_resources)

if ar_num > 10:
  severity = 'Critical'
elif ar_num > 5:
  severity = 'High'
elif ar_num > 1:
  severity = 'Moderate'
elif ar_num > 0:
  severity = 'Low'
else:
  severity = 'Informational'

if case_start_time:  
    c_s_t = case_start_time.to_iso8601_string()
else:
    c_s_t = None

if case_end_time:  
    c_e_t = case_end_time.to_iso8601_string()
else:
    c_e_t = None

    
    
  
sw_outputs.append({'description_of_case': r, 
                   'title':title, 
                   'case_severity':severity, 
                   'case_start_time':c_s_t,
                   'case_end_time':c_e_t,
                   'case_detected_time':eTime if c_e_t is not None else None, 
                   'case_status':'In Handling', 
                   'indicators':indicator, 
                   'affected_resources': "\n".join(affected_resources),
                  })