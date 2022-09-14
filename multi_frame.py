import os
import argparse
import numpy as np
import open3d as o3d

def main(args):
    print(f'args:\t{args}')
    # ================== #
    # set file directory #
    # ================== #

    # the dir where point cloud frames are stored
    folder_path = args.dir_name
    # get all point cloud frames' file name
    files = os.listdir(folder_path)

    # ======================== #
    # set visualization window #
    # ======================== #

    # create a Visualizer class instance
    vis = o3d.visualization.Visualizer()
    # create a window to display it
    vis.create_window(window_name=folder_path, width=3840, height=2560, left=0, top=0)
    # get window's render option parameter
    render_option = vis.get_render_option()
    # set the background color to black
    if args.bg_color == 'black':
        render_option.background_color = np.array([0, 0, 0])
    # set the background color to white
    elif args.bg_color == 'white':
        render_option.background_color = np.array([255, 255, 255])
    # set the displayed point size
    render_option.point_size = float(args.point_size)
    # get the view control parameters
    view_control = vis.get_view_control()

    # =================================================== #
    # prepare the point cloud and do some initializations #
    # =================================================== #

    # create a PointCloud class instance
    pcd = o3d.geometry.PointCloud()
    # add geometry to the scene
    vis.add_geometry(pcd)
    # for resetting view in first display
    to_reset = True

    # ================================================ #
    # loop through point cloud frames and visualize it #
    # ================================================ #

    for file in files:
        # zoom in
        view_control.set_zoom(0.3)
        # get file path and print it
        data_path = os.path.join(folder_path, file)
        # load the point cloud data 
        # (this line is according to the file type and its structure)
        # for example: xxx.bin is the file type and each point has 6 attributes
        point_cloud_data = np.fromfile(data_path, dtype=np.float32).reshape(-1, int(args.point_attr_nums))
        # get the x, y, z coordinates of each point
        point_xyz = point_cloud_data[:, :3]
        # convert float64 numpy array of shape (n, 3) to Open3D format.
        pcd.points = o3d.utility.Vector3dVector(point_xyz)
        # update geometry
        vis.update_geometry(pcd)
        # reset the view point for visualizing normally
        if to_reset:
            vis.reset_view_point(True)
            to_reset = False
        vis.poll_events()
        vis.update_renderer()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Point Cloud Frames Visualization Args.')
    parser.add_argument('dir_name', help='The directory that storing the point cloud frame files.')
    parser.add_argument('--bg_color', default='black', help='The displayed window\'s background color. (\'black\' or \'white\')')
    parser.add_argument('--point_size', default=1.5, help='The displayed size of the point.')
    parser.add_argument('--point_attr_nums', default=6, help='The attribute number of each point.')
    args = parser.parse_args()
    main(args)
