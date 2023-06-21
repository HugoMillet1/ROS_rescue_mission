#! /usr/bin/env python3

 

## install visualization_tutorials

 

import rospy

from std_msgs.msg import Float32MultiArray

import numpy as np

import cv2

import roslib; roslib.load_manifest('visualization_marker_tutorials')

from visualization_msgs.msg import Marker

from visualization_msgs.msg import MarkerArray

 

topic = 'visual_marker_array'

publisher = rospy.Publisher(topic, MarkerArray)

 

rospy.init_node('register')

 

mArray = MarkerArray()

x = 0

maxArrayNum = 8008

 

cv2.homography

class ObjectProcessing:

    def __init__(self):

        # Initialise Node

        rospy.init_node('image_processing')

        self.objlistener = rospy.Subscriber("/objects", self.get_object, queue_size=1)

        self.object_id = Float32MultiArray()

 

        # Kinect camera is 640 x 480

        self.camera_center = 320

        self.object_width = 0

        self.object_height = 0

        self.object_center = 0

 

    def get_object(self, obj):

        self.object_id = obj.data[0]

        self.object_width = obj.data[1]

        self.object_height = obj.data[2]

        #my_mat =

 

        visu = Marker()

        visu.header.frame_id = "/odom"

        visu.action = visu.ADD

        visu.id = visuId

 

        visu.scale.x = 0.2

        visu.scale.y = 0.2

        visu.scale.z = 0.2

 

        visu.lifetime = rospy.Duration.from_sec(100)

 

        # data will range from 10 to 18

        if self.object_id == 10:

            print("Death threat")

            visu.color.a = 1.0 #RED

            visu.color.r = 1.0

            visu.color.g = 1.0

            visu.color.b = 0.0

            visu.type = visu.CYLINDER

        elif self.object_id == 11:

            print("error ?")

            visu.color.a = 1.0 #BLUE

            visu.color.r = 1.0

            visu.color.g = 1.0

            visu.color.b = 0.0

            visu.type = visu.SPHERE

        elif self.object_id == 12:

            print("Radioactive")

            visu.color.a = 1.0 #YELLOW

            visu.color.r = 1.0

            visu.color.g = 1.0

            visu.color.b = 0.0

            visu.type = visu.CYLINDER

        elif self.object_id == 13:

            print("Smoke")

            visu.color.a = 1.0 #BLUE

            visu.color.r = 1.0

            visu.color.g = 1.0

            visu.color.b = 0.0

            visu.type = visu.CUBE

        elif self.object_id == 14:

            print("Fire")

            visu.color.a = 1.0 #RED

            visu.color.r = 1.0

            visu.color.g = 1.0

            visu.color.b = 0.0

            visu.type = visu.CUBE

        elif self.object_id == 15:

            print("Alive_Worker")

            visu.color.a = 1.0 #GREEN

            visu.color.r = 1.0

            visu.color.g = 1.0

            visu.color.b = 0.0

            visu.type = visu.SPHERE

        elif self.object_id == 16:

            print("Warning sign")

            visu.color.a = 1.0 #ORANGE

            visu.color.r = 1.0

            visu.color.g = 1.0

            visu.color.b = 0.0

            visu.type = visu.CYLINDER

        elif self.object_id == 17:

            print("Biohazard")

            visu.color.a = 1.0 #GREEN

            visu.color.r = 1.0

            visu.color.g = 1.0

            visu.color.b = 0.0

            visu.type = visu.CYLINDER

        elif self.object_id == 18:

            print("Dead_worker")

            visu.color.a = 1.0 #RED

            visu.color.r = 1.0

            visu.color.g = 1.0

            visu.color.b = 0.0

            visu.type = visu.SPHERE

        else:

            print("no object detected")

       

        if(x > maxArrayNum):

            mArray.markers.pop(0)

 

        mArray.markers.append(visu)

 

        visuId = 0

        for num in mArray.markers:

            num.id = visuId

            visuId += 1

 

        publisher.publish(mArray)

       

       

       

    while not rospy.is_shutdown():

   

 

        visu.pose.orientation.w = 1.0

        visu.pose.position.x = variable

        visu.pose.position.y = 1

        visu.pose.position.z = 1

        visu.pose.position.w = 1

 

       

        # We add the new marker to the MarkerArray, removing the oldest

        # marker from it when necessary

       

 

        # Renumber the marker IDs

       

 

        # Publish the MarkerArray

       

x += 1

 

if __name__ == "__main__":

    obj = ObjectProcessing()

    rospy.spin()

