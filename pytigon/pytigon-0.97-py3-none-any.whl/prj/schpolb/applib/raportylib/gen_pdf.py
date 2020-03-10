import sys
import asyncio

def patch_pyppeteer():
    import pyppeteer.connection
    original_method = pyppeteer.connection.websockets.client.connect

    def new_method(*args, **kwargs):
        kwargs['ping_interval'] = None
        kwargs['ping_timeout'] = None
        return original_method(*args, **kwargs)

    pyppeteer.connection.websockets.client.connect = new_method
patch_pyppeteer()

from pyppeteer import launch

async def _html_to_pdf(address, file_name):
    browser = await launch(args=['--no-sandbox'])
    page = await browser.newPage()
    #await page.emulateMedia('screen')
    await page.goto(address)


    ret = await page.evaluate('''() => {
        return {
            components_count: window.COMPONENTS_COUNT
        }
    }''')

    if 'components_count' in ret and ret['components_count'] > 0:
        components_count = ret['components_count']
        c = 0
        while c<300:
            ret = await page.evaluate('''() => {
                return {
                    mounted_components: window.MOUNTED_COMPONENTS,
                }
            }''')
                        
            if not 'mounted_components' in ret:
                break
            
            if  ret['mounted_components'] >=  components_count:
                break
            
            c+=1
            
            await asyncio.sleep(1)
    
    await asyncio.sleep(1)
    
    displayHeaderFooter = True
    headerTemplate = "<span></span>"
        
    css = '<style>h1 { font-size:10px; margin-left:4in; } </style>'
    
    footerTemplate = css+'<h1><span class="pageNumber"></span>/<span class="totalPages"></span></h1>'
        
    margin = { 
        'top':  '0.5cm',
        'right':  '0cm',
        'bottom':  '1.5cm',
        'left':  '0cm',
    }        
    await page.pdf({'path': file_name, 'displayHeaderFooter': displayHeaderFooter, 'headerTemplate': headerTemplate, 'footerTemplate': footerTemplate, 'margin': margin, 'width': '14in', 'printBackground': True })
    await browser.close()

def html_to_pdf(address, file_name):
    asyncio.get_event_loop().run_until_complete(_html_to_pdf(address, file_name))    

html_to_pdf(sys.argv[1], sys.argv[2])
