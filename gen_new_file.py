#
import json
from os.path import exists
import requests
from bs4 import BeautifulSoup

def main():

	f = open("url.txt", "r")
	url = f.read()

	practice_name, sample_io_dict_list, param_list, output_keyword = get_practice_name_n_sample_io_dict( url )

	filename = gen_code_file(practice_name, sample_io_dict_list, param_list, output_keyword)

	tasks_obj = None
	with open('.vscode/tasks.json', 'r', encoding="utf-8") as f:
		tasks_obj = json.load( f )

	task_label = f"Run { filename }"
	is_created = False
	for task in tasks_obj[ "tasks" ]:
		if task[ "label" ] == task_label:
			is_created = True
			break

	if not is_created:
		tasks_obj[ "tasks" ].append( {
			"label": f"{ task_label }",
			"type": "shell",
			"command": "testEnv\\Scripts\\python.exe",
			"args": [ filename ]
		} )

	with open('.vscode/tasks.json', "w", encoding="utf-8") as f:
		f.write( json.dumps( tasks_obj, indent=4, ensure_ascii=False ) )

	print(f'{ filename= }')
	print(f'{ task_label= }')

def gen_code_file(practice_name, sample_io_dict_list, param_list, output_keyword):

	filename = practice_name.replace(' ', '_') + ".py"
	# if exists( filename ):
	# 	raise Exception( f"File { filename } already exists" )

	output_var_name = "answer"
	lines = []
	lines.append("#")
	lines.append(f"def solution( { ', '.join( param_list ) } ):")
	lines.append(f"\t{ output_var_name } = { sample_io_dict_list[ 0 ][ output_keyword ] }")
	lines.append(f"\treturn { output_var_name }")
	lines.append(f"")
	lines.append(f"if __name__ == '__main__':")
	for sample_io_dict in sample_io_dict_list:
		param_val_list = []
		for param in param_list:
			input = sample_io_dict[ param ]
			if ( isinstance( input, str ) and input.isdigit() ) or input[ 0 ] in ( '[', '{', "\"" ):
				param_val_list.append( sample_io_dict[ param ] )
			elif isinstance( input, str ):
				param_val_list.append( "\"" + sample_io_dict[ param ] + "\"" )

		param_str = ", ".join( param_val_list )
		lines.append("\tprint(f'{ solution( " + param_str + " )= }, ea = " + sample_io_dict[ output_keyword ] + "')")
		with open( filename, 'w' ) as f:
			f.write( '\n'.join( lines ) )

	return filename

def get_practice_name_n_sample_io_dict( url):
	response = requests.get( url )

	if response.status_code != 200:
		raise Exception(f"{ response.status_code= }")

	html = response.text
	soup = BeautifulSoup( html, 'html.parser' )

	code_practice_name = soup.title.string.split( "코딩테스트 연습 - " )[ 1 ].split( "| 프로그래머스" )[ 0 ].strip()

	sample_io_title = None
	SAMPLE_IO_TITLE_LIST = [
		soup.find( "h3", string='예제 입출력' ),
		soup.find( "h5", string='입출력 예' ),
		soup.find( "h5", string='[입출력 예]' ),
		 ]
	for finder in SAMPLE_IO_TITLE_LIST:
		if finder:
			sample_io_title = finder
	table_sample_io = sample_io_title.findNext( "table" )
	headers = [header.text for header in table_sample_io.find_all('th')]
	param_list = headers[:-1]
	output_keyword = headers[ -1 ]
	sample_io_dict_list = [{headers[i]: cell.text for i, cell in enumerate(row.find_all('td'))} for row in table_sample_io.find_all('tr')]
	sample_io_dict_list = sample_io_dict_list[1:]

	return code_practice_name, sample_io_dict_list, param_list, output_keyword


if __name__ == '__main__':
	main()