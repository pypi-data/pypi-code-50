# ------------------------------------------------------------------------
#
#  This file is part of the Chirp Python SDK.
#  For full information on usage and licensing, see https://chirp.io/
#
#  Copyright (c) 2011-2019, Asio Ltd.
#  All rights reserved.
#
# ------------------------------------------------------------------------

import argparse
import sys
import time

from chirpsdk import ChirpSDK, CallbackSet, CHIRP_SDK_STATE


class Callbacks(CallbackSet):

    def on_state_changed(self, previous_state, current_state):
        """ Called when the SDK's state has changed """
        print('State changed from {} to {}'.format(
            CHIRP_SDK_STATE.get(previous_state),
            CHIRP_SDK_STATE.get(current_state)))

    def on_sending(self, payload, channel):
        """ Called when a chirp has started to be transmitted """
        print('Sending: {data} [ch{ch}]'.format(
            data=list(payload), ch=channel))

    def on_sent(self, payload, channel):
        """ Called when the entire chirp has been sent """
        print('Sent: {data} [ch{ch}]'.format(
            data=list(payload), ch=channel))

    def on_receiving(self, channel):
        """ Called when a chirp frontdoor is detected """
        print('Receiving data [ch{ch}]'.format(ch=channel))

    def on_received(self, payload, channel):
        """
        Called when an entire chirp has been received.
        Note: A length of 0 indicates a failed decode.
        """
        if payload is None:
            print('Decode failed!')
        else:
            print('Received: {data} [ch{ch}]'.format(
                data=list(payload), ch=channel))


def main(block_name, input_device, output_device,
         block_size, sample_rate, channel):

    # Initialise Chirp SDK
    sdk = ChirpSDK(block=block_name)
    print(str(sdk))
    print('Protocol: {protocol} [v{version}]'.format(
        protocol=sdk.protocol_name,
        version=sdk.protocol_version))
    print(sdk.audio.query_devices())

    # Configure audio
    sdk.audio.input_device = input_device
    sdk.audio.output_device = output_device
    sdk.audio.block_size = block_size
    sdk.input_sample_rate = sample_rate
    sdk.output_sample_rate = sample_rate

    # Set callback functions
    sdk.set_callbacks(Callbacks())

    # Set transmission channel for multichannel protocols
    if args.channel is not None:
        if args.channel >= sdk.channel_count:
            raise ValueError('Channel %d is not available' % args.channel)
        print('Writing to channel %d' % args.channel)
        sdk.transmission_channel = args.channel

    # Generate random payload and send
    payload = sdk.random_payload()
    sdk.start(send=True, receive=True)
    sdk.send(payload)

    try:
        # Process audio streams
        while True:
            time.sleep(0.1)
            sys.stdout.write('.')
            sys.stdout.flush()
    except KeyboardInterrupt:
        print('Exiting')

    sdk.stop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='ChirpSDK Demo',
        epilog='Sends a random chirp payload, then continuously listens for chirps'
    )
    parser.add_argument('-c', '--channel', type=int, help='The channel to output data on')
    parser.add_argument('-i', '--input-device', type=int, default=None, help='Input device index (optional)')
    parser.add_argument('-o', '--output-device', type=int, default=None, help='Output device index (optional)')
    parser.add_argument('-b', '--block-size', type=int, default=0, help='Block size (optional)')
    parser.add_argument('-s', '--sample-rate', type=int, default=44100, help='Sample rate (optional)')
    parser.add_argument('--config', type=str, help='The configuration block [name] in your ~/.chirprc file (optional)')
    parser.add_argument('--network-config', action='store_true', help='Optionally download a config from the network')
    args = parser.parse_args()

    main(args.config, args.input_device, args.output_device, args.block_size, args.sample_rate, args.channel)
