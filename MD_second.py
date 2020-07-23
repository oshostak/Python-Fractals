from PIL import Image

xa, xb = -0.675, -0.665
ya, yb = -0.45, -0.4675

imgx, imgy = 512, 512

maxIt = 256

image = Image.new("RGB", (imgx, imgy))

for y in range(imgy):
	cy = y*(yb-ya)/(imgy-1)+ya
	for x in range(imgx):
		cx = x*(xb-xa)/(imgx-1)+xa
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c

		r = i
		g = (i*2)%3
		b = i
		image.putpixel((x, y), (r,g,b))

image.show()
