from PIL import Image
from PIL import ImageDraw

imgx, imgy = 512, 512

image = Image.new("RGB", (imgx, imgy))
draw = ImageDraw.Draw(image)

x1_coordinate = 0
y1_coordinate = imgy

x2_coordinate = (imgx/2)
y2_coordinate = 0

x3_coordinate = imgx
y3_coordinate = imgy

counter = 0

def seprinskii_algorythm(x1_coordinate, x2_coordinate, x3_coordinate, y1_coordinate, y2_coordinate, y3_coordinate, image, counter):
	serpinskii_lines(image, x1_coordinate, x2_coordinate, x3_coordinate, y1_coordinate, y2_coordinate, y3_coordinate)

	if counter <5:

		coordinates = []
		coordinates.append(x1_coordinate)
		coordinates.append(x2_coordinate)
		coordinates.append(x3_coordinate)
		coordinates.append(y1_coordinate)
		coordinates.append(y2_coordinate)
		coordinates.append(y3_coordinate)




		x1_coordinate = (coordinates[0] + coordinates[1])/2 
		y1_coordinate = (coordinates[3] + coordinates[4])/2
		x2_coordinate = (coordinates[1] + coordinates[2])/2
		y2_coordinate = (coordinates[4] + coordinates[5])/2
		x3_coordinate = (coordinates[0] + coordinates[2])/2
		y3_coordinate = (coordinates[3] + coordinates[5])/2

		del coordinates[:]

		counter+=1

		seprinskii_algorythm(x1_coordinate, x2_coordinate, x3_coordinate, y1_coordinate, y2_coordinate, y3_coordinate, image, counter)

	else: 
	

		return image



def serpinskii_lines(image, x1_coordinate, x2_coordinate, x3_coordinate, y1_coordinate, y2_coordinate, y3_coordinate):
	draw.line(((x1_coordinate, y1_coordinate), (x2_coordinate, y2_coordinate)), fill=200, width=3)
	draw.line(((x2_coordinate, y2_coordinate), (x3_coordinate, y3_coordinate)), fill=200, width=3)
	draw.line(((x3_coordinate, y3_coordinate), (x1_coordinate, y1_coordinate)), fill=200, width=3)

	return image

serpinskii_lines(image, x1_coordinate, x2_coordinate, x3_coordinate, y1_coordinate, y2_coordinate, y3_coordinate)
seprinskii_algorythm(x1_coordinate, x2_coordinate, x3_coordinate, y1_coordinate, y2_coordinate, y3_coordinate, image, counter)
seprinskii_algorythm((x1_coordinate+x2_coordinate)/2, x2_coordinate, (x3_coordinate+x2_coordinate)/2, (y1_coordinate+y2_coordinate)/2, y2_coordinate, (y3_coordinate+y2_coordinate)/2, image, counter)
seprinskii_algorythm(x1_coordinate, (x1_coordinate+x2_coordinate)/2, (x1_coordinate+x3_coordinate)/2, y1_coordinate, (y2_coordinate+y3_coordinate)/2, (y1_coordinate+y3_coordinate)/2, image, counter)
seprinskii_algorythm((x1_coordinate+x3_coordinate)/2, (x2_coordinate+x3_coordinate)/2, x3_coordinate, (y1_coordinate+y3_coordinate)/2, (y2_coordinate+y3_coordinate)/2, y3_coordinate, image, counter)

image.show()
