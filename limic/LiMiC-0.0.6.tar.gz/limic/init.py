COUNTRIES = (("countries",),{'type':str,'nargs':'*','help':"countries to work on",'metavar':'COUNTRY'})
OVERPASS = (("-u","--overpass-url"),{'type':str,'dest':'overpass_url','help':"define url for Overpass API to be URL",'metavar':'URL'})
NOGT = (("-g","--no-graph-tool"),{'action':'store_true','dest':'no_gt','default':False,'help':"do not perform graph_tool tests"})
CONFIG = [
    ("stage0",{'help':"generate map data and all graph files (VERY SLOW)",'args':[OVERPASS,NOGT,COUNTRIES]}),
    ("stage1",{'help':"download map data and generate all graph files (SLOW)",'args':[OVERPASS,NOGT,COUNTRIES]}),
    ("stage2",{'help':"download NX graph files and other graph files",'args':[NOGT,COUNTRIES]}),
    ("stage3",{'help':"download all graph files (RECOMMENDED)",'args':[NOGT,COUNTRIES]})
]
BASE_URL="http://caracal.imada.sdu.dk/d4e/"
COUNTRIES="Albania,Andorra,Austria,Belarus,Belgium,Bosnia and Herzegovina,Bulgaria,Croatia,Cyprus,Czechia,Denmark,Estonia,Faroe Islands,Finland,France,Georgia,Germany,Gibraltar,Greece,Guernsey,Hungary,Iceland,Ireland,Isle of Man,Italy,Jersey,Kosovo,Latvia,Liechtenstein,Lithuania,Luxembourg,Macedonia,Malta,Moldova,Monaco,Montenegro,Netherlands,Norway,Poland,Portugal,RU,Romania,San Marino,Serbia,Slovakia,Slovenia,Spain,Sweden,Switzerland,Turkey,Ukraine,United Kingdom"

def download_file(url,file_name):
    from requests import get
    from shutil import copyfileobj
    r = get(url, stream=True)
    f = open(file_name, 'wb')
    copyfileobj(r.raw, f)
    return file_name

def download_caches(countries):
    from limic.util import start,end,file_size
    for country in countries:
        start("Downloading cache for",country)
        url = BASE_URL+"cache."+country.replace(" ","%20")
        file_name = download_file(url,"cache."+country)
        end('')
        file_size(file_name)

def download_graphs(suffix,countries):
    from limic.util import start,end,file_size
    for country in countries:
        start("Downloading",suffix.upper(),"graph for",country)
        url = BASE_URL+"graph."+country.replace(" ","%20")+"."+suffix
        file_name = download_file(url,"graph."+country+"."+suffix)
        end('')
        file_size(file_name)

def download_merged():
    from limic.util import start,end,file_size
    for suffix in "nx","gt","npz":
        start("Downloading merged",suffix.upper(),"graph for Europe")
        url = BASE_URL+"merged.Europe."+suffix
        file_name = download_file(url,"merged.Europe."+suffix)
        end('')
        file_size(file_name)

def fill_all(overpass_url,countries):
    from limic.fill import fill
    for country in countries:
        file_name = "cache."+country
        fill(overpass_url,file_name=file_name,area=None,around=1000,eps=0.01,safe_dist=100,penalty=20,max_workers=None)

def extract_all(overpass_url,countries):
    from limic.extract import extract
    for country in countries:
        file_name_in = "cache."+country
        file_name_out = "graph."+country+".nx"
        extract(file_name_in,file_name_out,overpass_url,area=None,around=1000,eps=0.01,safe_dist=100,penalty=20)

def convert_nx_gt_all(countries):
    from limic.convert import convert_nx_gt
    for country in countries:
        file_name_in = "graph."+country+".nx"
        file_name_out = "graph."+country+".gt"
        convert_nx_gt(file_name_in,file_name_out)

def convert_nx_npz_all(countries):
    from limic.convert import convert_nx_npz
    for country in countries:
        file_name_in = "graph."+country+".nx"
        file_name_out = "graph."+country+".npz"
        convert_nx_npz(file_name_in,file_name_out)

def convert_gt_npz_all(countries):
    from limic.convert import convert_gt_npz
    for country in countries:
        file_name_in = "graph."+country+".gt"
        file_name_out = "graph."+country+".npz"
        convert_gt_npz(file_name_in,file_name_out)

def merge_all(countries):
    from limic.merge import merge_nx
    from limic.convert import convert_nx_npz
    file_names = list(map(lambda country:"graph."+country+".nx",countries))
    merge_nx(file_names,"merged.Europe.nx")
    convert_nx_npz("merged.Europe.nx","merged.Europe.npz")

def common(countries):
    if not countries:
        countries = COUNTRIES.split(",")
    return countries

def convert_merge_all(countries,no_gt):
    if no_gt:
        convert_nx_npz_all(countries)
    else:
        convert_nx_gt_all(countries)
        convert_gt_npz_all(countries)
    if len(countries) >= 2:
        merge_all(countries)

def init_stage0(overpass_url,countries,no_gt):
    countries = common(countries)
    fill_all(overpass_url,countries)
    extract_all(overpass_url,countries)
    convert_merge_all(countries,no_gt)

def init_stage1(overpass_url,countries,no_gt):
    countries = common(countries)
    download_caches(countries)
    extract_all(overpass_url,countries)
    convert_merge_all(countries,no_gt)

def init_stage2(countries,no_gt):
    countries = common(countries)
    download_graphs("nx",countries)
    convert_merge_all(countries,no_gt)

def init_stage3(countries,no_gt):
    countries = common(countries)
    for suffix in "nx", "npz", "gt":
        download_graphs(suffix,countries)
    if len(countries) >= 2:
        merge_all(countries)
