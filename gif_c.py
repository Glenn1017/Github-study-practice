import imageio.v3 as iio
filenames = ['team-pic1.png','team-pic2.png']
images = []
for i in filenames:
    images.append(iio.imread(i))

iio.imwrite('team.gif',images,duration = 500, loop = 0)