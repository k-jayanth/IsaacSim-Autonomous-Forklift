from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    gazebo_launch_file = os.path.join(
        get_package_share_directory('gazebo_ros'),
        'launch',
        'gazebo.launch.py'
    )

    urdf_file = os.path.join(
        get_package_share_directory('forklift_simulator'),
        'urdf',
        'forklift_b.urdf'
    )

    sdf_file = os.path.join(
        get_package_share_directory('forklift_simulator'),
        'urdf',
        'forklift_b.sdf'
    )

    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    rsp_params = {'robot_description': robot_desc}

    return LaunchDescription([
        DeclareLaunchArgument('robot_namespace', default_value='/'),
        DeclareLaunchArgument('x', default_value='0'),
        DeclareLaunchArgument('y', default_value='0'),
        DeclareLaunchArgument('z', default_value='0.3'),
        DeclareLaunchArgument('urdf', default_value=os.path.join(
            get_package_share_directory('forklift_simulator'), 'urdf', 'forklift_b.urdf')),


        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[rsp_params, {'use_sim_time': use_sim_time}]
        ),

        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
        ),

        IncludeLaunchDescription(
            gazebo_launch_file,
            launch_arguments={}.items()
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_forklift_model',
            output='screen',
            parameters=[{
                'robot_description': robot_desc
            }],
            arguments=[
                '-file', sdf_file,
                '-entity', 'forklift_b',
                '-x', LaunchConfiguration('x'),
                '-y', LaunchConfiguration('y'),
                '-z', LaunchConfiguration('z'),
            ]
        ),
    ])
