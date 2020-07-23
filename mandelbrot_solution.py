from PIL import Image

imgx = 3

imgy = 3

image = Image.new("RGB", (imgx, imgy))

z = (0,0)

max_it = 3

counter = 1

y = 2

x = (-2)

z = 0

c = complex(x,y)

def check_z(z, c, x, y, image, counter):

	z = z**2+c

	if abs(z) >= 2:

		if counter == 1:

			image.putpixel((x,y), (60,0,0))
			c = c + 2
			z = 0
			return image, c, z

		if counter == 2:
			image.putpixel((x,y), (0,60,0))
			c = c+2
			z = 0
			return image, c, z

		if counter == 3:
			image.putpixel((x,y), (0,0,60))
			c = c+2
			z = 0
			return image, c, z

	elif abs(z) < 2:
		counter +=1
		return counter
		check_z(z, c, x, y, image, counter)

if y >= -2:
	if x <= 2:
		check_z(z, c, x, y, image, counter)
	elif x > 2:
		y += 2

image.show()

