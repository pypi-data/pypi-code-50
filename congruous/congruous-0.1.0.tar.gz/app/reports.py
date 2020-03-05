from matplotlib import pyplot as plt 


pytess_results = {
	"total_records": {
        "total": 0,
		"correct": 0,
		"incorrect": 0
	},
	"date": {   
		"correct": 0,
		"incorrect": 0
	},
	"month": {
		"correct": 0,
		"incorrect": 0
	},
	"year": {
		"correct": 0,
		"incorrect": 0
	},
	"pan_id": {
		"correct": 0,
		"incorrect": 0
	},
    "name": {
		"correct": 0,
		"incorrect": 0
	},
    "father_name":{
        "correct": 0,
		"incorrect": 0
    }
}


def match_records(pan_record, tesseract_record):
    
    record_flag = 0

    # print(pan_record)
    # print(tesseract_record)
    pytess_results['total_records']['total'] += 1
    try : 

        if tesseract_record != None:

            if 'pan_id' in tesseract_record.keys() and pan_record['pan_id'] == tesseract_record['pan_id']:
                pytess_results['pan_id']['correct'] += 1
            else: 
                pytess_results['pan_id']['incorrect'] += 1
                record_flag = 1

            if  'date' in tesseract_record.keys(): 
                if pan_record['date']  == tesseract_record['date']:
                    pytess_results['date']['correct'] += 1
            else: 
                pytess_results['date']['incorrect'] += 1
                record_flag = 1

            
            if 'month' in tesseract_record.keys():
                if pan_record['month']  == tesseract_record['month']:
                    pytess_results['month']['correct'] += 1
            else: 
                pytess_results['month']['incorrect'] += 1
                record_flag = 1

            if 'year' in tesseract_record.keys():
                if pan_record['year']  == tesseract_record['year']:
                    pytess_results['year']['correct'] += 1
            else: 
                pytess_results['year']['incorrect'] += 1
                record_flag = 1
        else: 
            record_flag = 1

        if record_flag == 0:
            pytess_results['total_records']['correct'] += 1
        else:
            pytess_results['total_records']['incorrect'] += 1
    
        # print(pytess_results)
        # input()

    except Exception as e :

        # print('tesseract_record : ', tesseract_record, e)
        pass     



def show_pie_charts(title):

	print(pytess_results)

	fig = plt.figure() 
	fig.suptitle(title, fontsize=16)


	slices_total = [pytess_results['total_records']['correct'],pytess_results['total_records']['incorrect'] ]
	color_total = [ '#47B39C', '#EC6B56']

	slices_pan = [pytess_results['pan_id']['correct'],pytess_results['pan_id']['incorrect'] ]
	color_pan = [ '#47B39C', '#EC6B56']

	slices_date = [pytess_results['date']['correct'],pytess_results['date']['incorrect'] ]
	color_date = [ '#47B39C', '#EC6B56']

	slices_month = [pytess_results['month']['correct'],pytess_results['month']['incorrect'] ]
	color_month = [ '#47B39C', '#EC6B56']

	slices_year = [pytess_results['year']['correct'],pytess_results['year']['incorrect'] ]
	color_year = [ '#47B39C', '#EC6B56']

	ax1 = fig.add_axes([0, 0, .5, .5], aspect=1)
	ax1.pie(slices_total, labels = slices_total, colors=color_total ,wedgeprops={'edgecolor' :'black'}, autopct='%1.0f%%', radius = 1.7)

	ax2 = fig.add_axes([1, .0, .5, .5], aspect=1)
	ax2.pie(slices_pan, labels = slices_pan, colors=color_pan ,wedgeprops={'edgecolor' :'black'}, autopct='%1.0f%%', radius = 1.7)

	ax3 = fig.add_axes([2, .0, .5, .5], aspect=1)
	ax3.pie(slices_date, labels = slices_date, colors=color_date ,wedgeprops={'edgecolor' :'black'}, autopct='%1.0f%%', radius = 1.7)

	ax4 = fig.add_axes([3, .0, .5, .5], aspect=1)
	ax4.pie(slices_month, labels = slices_month, colors=color_date ,wedgeprops={'edgecolor' :'black'}, autopct='%1.0f%%', radius = 1.7)

	ax5 = fig.add_axes([4, .0, .5, .5], aspect=1)
	ax5.pie(slices_year, labels = slices_year, colors=color_date ,wedgeprops={'edgecolor' :'black'}, autopct='%1.0f%%', radius =1.7)

	ax1.set_title('Complete Record Match %\n\n\n\n')
	ax2.set_title('Pan Number Match %\n\n\n')
	ax3.set_title('DOB Date Match %\n\n\n')
	ax4.set_title('DOB Month Match %\n\n\n')
	ax5.set_title('DOB Year Match %\n\n\n')
	# import os 
	# print(os.getcwd())
	plt.savefig(str(title) + '.png',  bbox_inches='tight')