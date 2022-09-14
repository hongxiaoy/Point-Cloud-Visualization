import open3d as o3d
import numpy as np
import argparse


def main(args):
    pcl = np.fromfile(args.file_name, dtype=np.float32).reshape(-1, int(args.point_attr_num))
    pcl_xyz = pcl[:, :3]

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pcl_xyz)

    vis = o3d.visualization.Visualizer()
    vis.create_window(width=3840, height=2560, left=0, top=0)

    render_option = vis.get_render_option()
    render_option.background_color = np.array([0, 0, 0])
    render_option.point_size = 1.5

    vis.add_geometry(pcd)

    view_control = vis.get_view_control()
    vis.reset_view_point(True)
    view_control.set_zoom(0.4)

    vis.run()
    vis.destroy_window()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Point Cloud Single Frame Visualization Args.')
    parser.add_argument('file_name', help='The file name of the point cloud frame you want to display.')
    parser.add_argument('--point_attr_num', default=6, help='The attribute number of each point.')
    args = parser.parse_args()
    main(args)