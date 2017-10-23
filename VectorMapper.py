# Vector Mapper
# --> A simple tool to manually create vector maps for Autoware's Openplanner from a pointcloud
# --> Author: Jakub Tomasek, jakub@tomasek.fr

import numpy as np
import matplotlib.pyplot as plt
import pypcd


coords = []

def onclick(event):
    ix, iy = event.xdata, event.ydata
    print '\n x = %f, y = %f' % (ix, iy)
    global coords
    coords.append((ix, iy))

    if len(coords) == 2:
        fig.canvas.mpl_disconnect( cid )

    return coords



def main():
	pc = pypcd.PointCloud.from_path('/home/jakub/Desktop/output.pcd')
	zipped_pc = zip(*pc.pc_data)
	x = zipped_pc[0]
	y = zipped_pc[1]
	z = zipped_pc[2]

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(x, y, c=z, s = 0.1, lw = 0 )
	cid = fig.canvas.mpl_connect('button_press_event', onclick)
	fig.show()
	raw_input("Press Enter to finish...")

if __name__ == "__main__":
    main()