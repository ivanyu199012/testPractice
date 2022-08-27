def solution(sizes):
	answer = 0

	width = 0
	height = 0
	for size in sizes:
		if size[ 0 ] > size[ 1 ]:
			width = size[ 0 ] if width < size[ 0 ] else width
			height = size[ 1 ] if height < size[ 1 ] else height
			continue

		width = size[ 1 ] if width < size[ 1 ] else width
		height = size[ 0 ] if height < size[ 0 ] else height

	return width * height

if __name__ == '__main__':
	print( solution( [[60, 50], [30, 70], [60, 30], [80, 40]] ) )
	print( solution( [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]] ) )
	print( solution( [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]] ) )