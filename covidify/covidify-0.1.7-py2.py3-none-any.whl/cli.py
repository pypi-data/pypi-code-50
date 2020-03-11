import os
import sys
import covidify
import click
import getpass
from covidify.config import SCRIPT
from covidify.utils.utils import replace_arg_space
USER = getpass.getuser()

def check_output_folder(var, msg):
    '''
    Check if the output folder is valid, if not
    just default to dekstop 
    '''
    
    if not var:
        print('%sMESSAGE: %s' % (' '*5, msg))
        return '/Users/'+ USER +'/Desktop/covidify-output/'
    else:
        return var

def check_source_arg(var, msg):
    '''
    Check if the datasource is valid, if not then just
    default to the john hopkin github repo
    '''

    if var is None:
        print('%sMESSAGE: %s' % (' '*5, msg))
        return 'git'
    elif 'wiki' in var or 'git' in var:
        return var
    else:
        print('%sMESSAGE: %s' % (' '*5, 'invalid source given'))
        sys.exit()
        
def check_country(country, msg):
    '''
    Do some regex work on passed country string
    because multi word args are not supported
    '''
    
    if not country:
        print('%sMESSAGE: %s' % (' '*5, msg))
        return 'Global'
    else:
        country_str = replace_arg_space(country[0])
        return country_str

@click.group()
def cli():
    '''
    ☣  COVIDIFY ☣ \n
     - use the most up-to-date data to generate reports of confirmed cases, fatalities and recoveries. 
    '''
    pass

@cli.command()
@click.option('--output',  help='Folder to output data and reports [Default: /Users/' + USER + '/Desktop/covidify-output/]')
@click.option('--source',  help='There are two datasources to choose from, John Hopkins github repo or wikipedia -- options are git or wiki respectively [Default: git]')
@click.option('--country', help='Filter reports by a country', multiple=True, type=str)
def run(output, source, country):
    
    #Do checks on args
    country_str = check_country(country, '\033[1;31m No country specified, defaulting to global cases \033[0;0m')    
    output = check_output_folder(output, '\033[1;31m No output directory given, defaulting to /Users/' + USER + '/Desktop/covidify-output/ \033[0;0m')
    source = check_source_arg(source, '\033[1;31m No source given, defaulting to John Hopkin CSSE github repo \033[0;0m')

    #get the path of covidify in site-packages
    env = covidify.__path__[0]
    
    os.system(env + SCRIPT + ' ' + env + ' ' + output + ' ' + source + ' ' + country_str)