"""Cognitive Reflection Test (CRT)

Frederick, Shane (2005). "Cognitive Reflection and Decision Making". Journal of Economic Perspectives. 19 (4): 25–42. https://www.aeaweb.org/articles?id=10.1257/089533005775196732.

A CRT branch contains a list of pages testing CRT items. A CRT item is a 
dictionary.

CRT item dictionary
-------------------
var : string
    Variable name.
gen_question : callable
    Callable which takes a CRT page and generates a CRT question.
correct : must be comparable with == to CRT question data
    The correct response.
intuitive: must be comparable with == to CRT question data
    The intuitive response.
"""

from hemlock import *

def CRT(crt_b, *items):
    """Add a CRT to a branch
    
    Compute performance summary statistics when last CRT page is submitted.
    """
    crt_pages = [gen_page(crt_b, item) for item in items]
    Submit(crt_b.pages[-1], summary_stats, args=[crt_b, crt_pages])

def gen_page(crt_b, item):
    """Generate CRT page
    
    Assess the response when the CRT page is submitted.
    """
    var = item.get('var')
    crt_p = Page(crt_b, name=var)
    crt_p.timer.var = '{}Time'.format(var)
    crt_p.timer.all_rows = True
    crt_q = item['gen_question']()
    crt_q.page, crt_q.var, crt_q.all_rows = crt_p, var, True
    Submit(crt_p, assess_response, args=[item])
    return crt_p

def assess_response(crt_p, item):
    """Assess CRT question response

    Attach embedded data to the CRT page indicating:
    1. Whether the response was correct.
    2. Whether the response was intuitive.
    """
    data = crt_p.questions[0].data
    var = item.get('var')
    Embedded(
        crt_p, 
        var='{}Correct'.format(var), 
        data=int(item.get('correct') == data),
        all_rows=True
    )
    Embedded(
        crt_p, 
        var='{}Intuitive'.format(var), 
        data=int(item.get('intuitive') == data),
        all_rows=True
    )

def summary_stats(last_p, crt_b, crt_pages):
    """Compute performance summary statistics

    Summary statistics are:
    1. Total correct.
    2. Percent correct.
    3. Total intuitive.
    4. Percent intuitive.
    """
    correct = sum([crt_p.embedded[0].data for crt_p in crt_pages])
    intuitive = sum([crt_p.embedded[1].data for crt_p in crt_pages])
    sum_stats = {
        'CRT.TotalCorrect': correct,
        'CRT.PctCorrect': 100.0* correct / len(crt_pages),
        'CRT.TotalIntuitive': intuitive,
        'CRT.PctIntuitive': 100.0 * intuitive / len(crt_pages)
    }
    [
        Embedded(crt_b, var=var, data=data, all_rows=True)
        for var, data in sum_stats.items()
    ]