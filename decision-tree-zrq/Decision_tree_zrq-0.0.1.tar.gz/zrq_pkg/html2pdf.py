# 导入库
import pdfkit

'''将网页url生成pdf文件'''
def url_to_pdf(url, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r'E:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_url(url, to_file, configuration=config)
    print('完成')

# 这里传入我知乎专栏文章url，转换为pdf



'''将html文件生成pdf文件'''
def html_to_pdf(html, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r'E:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_file(html, to_file, configuration=config)
    print('完成')

# html_to_pdf('','out_2.pdf')



'''将字符串生成pdf文件'''
def str_to_pdf(string, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r'E:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_string(string, to_file, configuration=config)
    print('完成')

if __name__ == '__main__':
    url_to_pdf(r'http://127.0.0.1:8888/notebooks/%E9%A2%84%E6%B5%8B-checkpoint.ipynb', 'out_1.pdf')
    str_to_pdf('This is test!', 'out_3.pdf')
    # html_to_pdf('','out_2.pdf')