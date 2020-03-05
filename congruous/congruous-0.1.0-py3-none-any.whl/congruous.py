import click
import csv
from fuzzywuzzy import fuzz, process
from app.reports import match_records, show_pie_charts

#  Function to check for supported document types 
def check_document_type(argument): 
    switcher = { 
        "pan" : "zero", 
        "aadhar": "aadhar", 
        "driving_license": "driving_license",
        "voterid": "voterid" 
    }  
    return switcher.get(argument, None) 

# Suggest the correct document for the wrongly typed document
def suggest_document_type(document):
    click.echo("congruous: unsupported document type: {}".format(document))
    supported_docs = ['pan', 'aadhar', 'driving_license', 'voter_id']
    probables = process.extract(document, supported_docs, limit=2)
    click.echo("Did you mean: \n")
    for doc in probables:
        click.echo("\t {}".format(doc[0]))


@click.command()
@click.argument('document_type')
@click.option('--verbose', is_flag=True, help="prints all the verbose messages")
@click.option('--title', help="title on the final report generated")
@click.option('--file', help="data(.csv) to be matched with raw human curated data")
@click.option('--match', help="matches with the file with the given --input")
@click.option('--fields',  multiple=True, help="matches the mentioned fields alone")
@click.option('--describe', help="describes fields that will be matched for given document")
@click.option('--feed', help='saves the data to the inbuilt database supported by congruous')
@click.option('--report', help='generates the final reports and saves it in current directory')
@click.option('--history', is_flag=True, help="displays a time based graph of the accuracy over time")
def cli(document_type, verbose, file, match, fields, describe, feed, report, history, title):

    # Check for the suppported document types 
    document = check_document_type(document_type)
    if check_document_type(document_type) == None:
        suggest_document_type(document_type)
        exit()

    # if history is present 
    if history != False:
        pass

    # Reads the data from the given file path
    if file != None:
        file_records = []
        match_file_records = []
        try: 
            with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for record in reader: 
                    file_records.append(dict(record))
            if match != None:
                with open(match, newline='') as matchfile:
                    reader = csv.DictReader(matchfile)
                    for record in reader: 
                        match_file_records.append(dict(record))

            if len(file_records) == len(match_file_records) and len(file_records)  > 0 :
                for index, rec in enumerate(file_records):
                    match_records(file_records[index], match_file_records[index])

                # from app.reports import pytess_results
                show_pie_charts(title)


            
        except FileNotFoundError as e:
            print('File Not Found: {}'.format(e))

