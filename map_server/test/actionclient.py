#! /usr/bin/env python

import roslib; roslib.load_manifest('map_server')
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import map_server.msg

def loadmap_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('loadmap_as_name', map_server.msg.loadmapAction)

    print "waiting for server"

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    print "server is there"

    # Creates a goal to send to the action server.
    goal = map_server.msg.loadmapGoal(order=20)

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('loadmap_action_client2')
        result = loadmap_client()
    except rospy.ROSInterruptException:
        print "program interrupted before completion"
