import roslibpy

from alloy.ros import roslibpy as rlp

def main():
    ros = roslibpy.Ros(host='localhost', port=9090)
    listener = roslibpy.Topic(ros, '/cameras/left_hand_camera/image', 'sensor_msgs/Image')
    publisher = roslibpy.Topic(ros, '/image_output', 'sensor_msgs/Image')

    def start_listening():
        listener.subscribe(receive_message)

    def receive_message(message):
        data, header = rlp.image_to_numpy(message, 'bgr8')
        publisher.publish(rlp.numpy_to_image(data, header=header))

    ros.on_ready(start_listening)
    ros.run_forever()

if __name__ == "__main__":
    main()    
