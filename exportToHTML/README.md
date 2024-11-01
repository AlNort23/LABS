#!/usr/bin/env python3

from pyre import Pyre
from pyre import zhelper
import zmq
import uuid
import json

# Function: get_peer_node
# ------------------------
# Spawn a new Pyre node, because who doesn't love a good fire
#
# Parameters:
#   username (str): The username to ignite the node with
#
# Returns:
#   Pyre: The node
def get_peer_node(username):  # get_peer_node
    n = Pyre(username)
    #n.set_header("CHAT_Header1","example header1")
    #n.set_header("CHAT_Header2","example header2")
    n.start()
    return n

# Function: join_group
# -------------------
# Join the party, connect to a group and get this chat started
#
# Parameters:
#   node (Pyre): The node to join the group with
#   group (str): The party to crash
#
# Returns:
#   None, but plenty of fun
def join_group(node, group):  # join_group
    node.join(group)
    print(f"Joined group: {group}")

# Function: chat_task
# ------------------
# The main event, this is where the chat magic happens
#
# Parameters:
#   ctx (zmq.Context): The ZeroMQ context, used for creating sockets and managing connections
#   pipe (zmq.Socket): The secret message pipe, used for internal communication
#   n (Pyre): The Pyre node, our trusty chat sidekick
#   group (str): The group name, where the party's at
#
# Returns:
#   None, but a whole lot of chatting
def chat_task(ctx, pipe, n, group):  # chat_task
    poller = zmq.Poller()
    poller.register(pipe, zmq.POLLIN)
    # print(n.socket())
    poller.register(n.socket(), zmq.POLLIN)
    # print(n.socket())
    while(True):
        items = dict(poller.poll())
        # print(n.socket(), items)
        if pipe in items and items[pipe] == zmq.POLLIN:
            message = pipe.recv()
            # message to quit
            if message.decode('utf-8') == "$$STOP":
                break
            print(f"YOU: {message.decode('utf-8')}")
            n.shouts(group, message.decode('utf-8'))
        else:
            cmds = n.recv()
            msg_type = cmds.pop(0).decode('utf-8')
            peer_id = uuid.UUID(bytes=cmds.pop(0))
            peer_username = cmds.pop(0).decode('utf-8')
            match msg_type:
                case "SHOUT":
                    intended_group = cmds.pop(0).decode('utf-8')
                    if intended_group == group:
                        # print(f"{peer_username}({peer_id}): {cmds}")
                        print(f"{peer_username}: {cmds.pop(0).decode('utf-8')}")
                case "ENTER":
                    headers = json.loads(cmds.pop(0).decode('utf-8'))
                    # print(f"NODE_MSG HEADERS: {headers}")
                    # for key in headers:
                    #    print("key = {0}, value = {1}".format(key, headers[key]))
                    # print( f"{peer_username}({peer_id}): is now connected." )
                    print( f"{peer_username}: is now connected." )
                case "JOIN":
                    #print( f"{peer_username}({peer_id}): joined {cmds.pop(0).decode('utf-8')}." )
                    print( f"{peer_username}: joined {cmds.pop( 0 ).decode( 'utf-8' )}." )
            # print(f"NODE_MSG CONT: {cmds}")
    n.stop()

# Function: get_channel
# ---------------------
# Get ready to rumble, create a new channel for the node and group
#
# Parameters:
#   node (Pyre): The Pyre node, our trusty chat sidekick
#   group (str): The group name, where the party's at
#
# Returns:
#   zmq.Socket: The created channel socket, let the chatting begin
def get_channel(node, group):  # get_channel
    ctx = zmq.Context()
    return zhelper.zthread_fork(ctx, chat_task, n=node, group=group)