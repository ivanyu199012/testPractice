#
import json
from os.path import exists
import requests
from bs4 import BeautifulSoup

URL = "https://school.programmers.co.kr/learn/courses/30/lessons/17677"

def main():
	practice_name, sample_io_dict_list, param_list = get_practice_name_n_sample_io_dict()
	print(f'{ practice_name, sample_io_dict_list, param_list= }')

	filename = gen_code_file(practice_name, sample_io_dict_list, param_list)
	print(f'{ filename= }')

	tasks_obj = None
	with open('.vscode/tasks.json', 'r', encoding="utf-8") as f:
		tasks_obj = json.load( f )

	tasks_obj[ "tasks" ].append( {
		"label": f"Run { filename }",
		"type": "shell",
		"command": "testEnv\\Scripts\\python.exe",
		"args": [ filename ]
	} )

	with open('.vscode/tasks.json', "w", encoding="utf-8") as f:
		f.write( json.dumps( tasks_obj, indent=4, ensure_ascii=False ) )



def gen_code_file(practice_name, sample_io_dict_list, param_list):

	filename = practice_name.replace(' ', '_') + ".py"
	# if exists( filename ):
	# 	raise Exception( f"File { filename } already exists" )

	lines = []
	lines.append("#")
	lines.append(f"def solution( { ', '.join( param_list ) } ):")
	lines.append(f"\tanswer = { sample_io_dict_list[ 0 ][ 'answer' ] }")
	lines.append(f"\treturn answer")
	lines.append(f"")
	lines.append(f"if __name__ == '__main__':")
	for sample_io_dict in sample_io_dict_list:
		param_val_list = []
		# param_str = ", ".join( [ "\"" +  sample_io_dict[ param ] + "\"" for param in param_list ] )
		for param in param_list:
			input = sample_io_dict[ param ]
		if ( isinstance( input, str ) and input.isdigit() ) or input[ 0 ] in ( '[', '{' ):
			param_val_list.append( sample_io_dict[ param ] )
		elif isinstance( input, str ):
			param_val_list.append( "\"" + sample_io_dict[ param ] + "\"" )

		param_str = ", ".join( param_val_list )
		lines.append("\tprint(f'{ solution( " + param_str + " )= }, expected_answer = " + sample_io_dict[ 'answer' ] + "')")
		with open( filename, 'w' ) as f:
			f.write( '\n'.join( lines ) )

	return filename


def get_practice_name_n_sample_io_dict():
	response = requests.get( URL )

	if response.status_code != 200:
		raise Exception(f"{ response.status_code= }")

	html = response.text
	soup = BeautifulSoup( html, 'html.parser' )

	code_practice_name = soup.title.string.split( "코딩테스트 연습 - " )[ 1 ].split( "| 프로그래머스" )[ 0 ].strip()

	table_sample_io = soup.find( "h3", string='예제 입출력' ).findNext( "table" )
	headers = [header.text for header in table_sample_io.find_all('th')]
	param_list = headers[:-1]
	sample_io_dict_list = [{headers[i]: cell.text for i, cell in enumerate(row.find_all('td'))} for row in table_sample_io.find_all('tr')]
	sample_io_dict_list = sample_io_dict_list[1:]

	return code_practice_name, sample_io_dict_list, param_list


if __name__ == '__main__':
	main()