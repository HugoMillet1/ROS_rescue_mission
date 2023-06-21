#! /usr/bin/env python3


import rospy
from std_msgs.msg import Float32MultiArray
import numpy as np
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

class ObjectProcessing:
    def __init__(self):
        # Initialise Node
        rospy.init_node('image_processing')
        #  self.objlistener = rospy.Subscriber("/objects", self.get_object, queue_size=1)
        self.pose_listener = rospy.Subscriber(
            "/pose_object", TransformStamped, self.get_position, queue_size=1)
        self.robot_pos = rospy.Subscriber(
            "/odom", Odometry, self.robot_pos_callback, queue_size=1)
        self.object_id = Float32MultiArray()

        topic = 'visual_marker_array'
        self.publisher = rospy.Publisher(topic, Marker, queue_size=1)
        self.mArray = MarkerArray()
        #self.marker = Marker()
        
        self.visu = Marker()
        self.previous_obj_pos = [[0], [0]]

        self.visu.header.frame_id = "odom"

        self.visu.action = 0

        visuId = 0
        self.visu.id = visuId

        self.visu.scale.x = 0.2
        self.visu.scale.y = 0.2
        self.visu.scale.z = 0.2

        self.visu.lifetime = rospy.Duration.from_sec(10000)

        # Kinect camera is 640 x 480
        self.camera_center = 320
        self.object_width = 0
        self.object_height = 0
        self.object_center = 0
        self.robot_pos_x = 0
        self.robot_pos_y = 0
        self.robot_yaw = 0

    def get_position(self, msg):

        temp_yaw = self.robot_yaw
        temp_x = self.robot_pos_x
        temp_y = self.robot_pos_y
        self.object_id = msg.header.frame_id
        self.obj_xpos = msg.transform.translation.x
        print(self.obj_xpos)
        self.obj_ypos = msg.transform.translation.y
        print(self.obj_ypos)
        self.obj_zpos = msg.transform.translation.z
        print(self.obj_zpos)

        self.visu.header.stamp = rospy.Time.now()
        self.visu.ns = "cylinder"
        #self.visu.frame_locked = 1

        if self.object_id == "object_10":
            print("Death threat")
            self.visu.color.a = 1.0  # BLACK
            self.visu.color.r = 0.0
            self.visu.color.g = 0.0
            self.visu.color.b = 0.0

            self.visu.type = 3
        elif self.object_id == "object_11":
            print("error ?")
            self.visu.color.a = 1.0  # RED
            self.visu.color.r = 1.0
            self.visu.color.g = 1.0
            self.visu.color.b = 0.0
            self.visu.type = 2

        elif self.object_id == "object_12":
            print("Radioactive")
            self.visu.color.a = 1.0  # RED
            self.visu.color.r = 0.8
            self.visu.color.g = 1.0
            self.visu.color.b = 0.5
            self.visu.type = 3

        elif self.object_id == "object_13":
            print("Smoke")
            self.visu.color.a = 1.0  # RED
            self.visu.color.r = 0.6
            self.visu.color.g = 0.6
            self.visu.color.b = 0.6
            self.visu.type = 1

        elif self.object_id == "object_14":
            print("Fire")
            self.visu.color.a = 1.0  # RED
            self.visu.color.r = 1.0
            self.visu.color.g = 0.5
            self.visu.color.b = 0.0
            self.visu.type = 1

        elif self.object_id == "object_15":
            print("Alive_Worker")
            self.visu.color.a = 1.0  # RED
            self.visu.color.r = 0.0
            self.visu.color.g = 1.0
            self.visu.color.b = 0.0
            self.visu.type = 2

        elif self.object_id == "object_16":
            print("Warning sign")
            self.visu.color.a = 1.0  # RED
            self.visu.color.r = 1.0
            self.visu.color.g = 0.5
            self.visu.color.b = 0.5
            self.visu.type = 3

        elif self.object_id == "object_17":
            print("Biohazard")
            self.visu.color.a = 1.0  # RED
            self.visu.color.r = 0.0
            self.visu.color.g = 0.7
            self.visu.color.b = 0.6
            self.visu.type = 3

        elif self.object_id == "object_18":
            print("Dead_worker")
            self.visu.color.a = 1.0  # RED
            self.visu.color.r = 0.5
            self.visu.color.g = 0.0
            self.visu.color.b = 0.0
            self.visu.type = 2

        else:
            print("no object detected")
            self.visu.color.a = 1.0  # RED
            self.visu.color.r = 1.0
            self.visu.color.g = 1.0
            self.visu.color.b = 1.0

        print("in position: " + str(self.obj_xpos) +
              ", " + str(self.obj_ypos) + ", " + str(self.obj_zpos))

        # Compute world position of the object applying transform
        rotation_matrix = np.matrix(
            [[math.cos(temp_yaw), -math.sin(temp_yaw)], [math.sin(temp_yaw), math.cos(temp_yaw)]])
        robot_pos = np.matrix([[temp_x], [temp_y]])
        rf_obj_pos = np.matrix([[self.obj_zpos], [-self.obj_xpos]])
        wf_obj_pos = robot_pos + rotation_matrix*rf_obj_pos

        print(wf_obj_pos)

        # Print the marker parameters
        self.visu.pose.position.x = wf_obj_pos[0][0]
        self.visu.pose.position.y = wf_obj_pos[1][0]
        self.visu.pose.position.z = 0.5

        # Increment the marker's ID
        self.visu.id += 1

        # for num in self.mArray.markers:
        #   num.id = visuId
        #  visuId += 1

        self.publisher.publish(self.visu)

        # if abs(wf_obj_pos[0][0]-self.previous_obj_pos[0][0]) < 0.5 and abs(wf_obj_pos[1][0]-self.previous_obj_pos[1][0]) < 0.5:
        #     self.publisher.publish(self.visu)

        self.previous_obj_pos[0][0] = wf_obj_pos[0][0]
        self.previous_obj_pos[1][0] = wf_obj_pos[1][0]

    def robot_pos_callback(self, msg):
        self.robot_pos_x = msg.pose.pose.position.x
        self.robot_pos_y = msg.pose.pose.position.y

        orientation_list = [msg.pose.pose.orientation.x, msg.pose.pose.orientation.y,
                            msg.pose.pose.orientation.z, msg.pose.pose.orientation.w]
        (roll, pitch, self.robot_yaw) = euler_from_quaternion(orientation_list)


if __name__ == "__main__":
    obj = ObjectProcessing()
    rospy.spin()
