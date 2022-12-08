import open3d as o3d

source_fileDir="source/"
source = o3d.io.read_point_cloud(source_fileDir+"cloud_bin_10.ply")

# visualize colored point cloud
o3d.visualization.draw_geometries([source])