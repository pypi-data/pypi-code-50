#!/usr/bin/env python3

import pkstl

def server_infos():
	# Create server sig keypair seed
	seed = pkstl.Seed32.random()
	
	# Create server secure layer config
	server_conf = pkstl.SecureLayerConfig.default()
	
	# Create server secure layer
	server_msl = pkstl.SecureLayer.create(server_conf, seed)
	
	# Get server sig pubkey
	server_pubkey = pkstl.Ed25519KeyPair.from_seed_unchecked(seed.bytes).pubkey
	
	return server_msl, server_pubkey

def client_infos(server_pubkey):
	# Create client secure layer config
	client_conf = pkstl.SecureLayerConfig.default()
	
	# Create client secure layer
	client_msl = pkstl.SecureLayer.create(client_conf, None, server_pubkey)
	
	return client_msl

def send_connect_msg(sender_msl, receiver_msl, custom_data):
	# Write `Connect` message with sender
	msg_out = sender_msl.write_connect_msg_bin(custom_data)
	
	# Read message with receiver
	msgs_in = receiver_msl.read_bin(msg_out)
	
	assert len(msgs_in) == 1 , "Received more or less than 1 message"
	assert msgs_in[0].msg_type == 1 , "Bad message type"
	
	# Get data
	msg_data = msgs_in[0].data
	assert msg_data[0] == bytes([5,1,1,5]) , "Bad custom data"
	
	return msg_data[1]

if __name__ == "__main__":
	server_msl, server_pubkey = server_infos()
	client_msl = client_infos(server_pubkey)
	assert send_connect_msg(server_msl, client_msl, bytes([5,1,1,5])) == server_pubkey , "Bad pubkey"
	
	msg_out = client_msl.write_ack_msg_bin(bytes([7,1,1,7]))
	msgs_in = server_msl.read_bin(msg_out)
	assert len(msgs_in) == 0 , "Server reads too early `Ack` message"
	
	msg_out = client_msl.write_connect_msg_bin(bytes([5,1,1,5]))
	msgs_in = server_msl.read_bin(msg_out)
	
	assert len(msgs_in) == 2 , "Received more or less than 2 messages"
	assert msgs_in[0].msg_type == 1 , "Bad message type (expected `Connect`)"
	assert msgs_in[1].msg_type == 2 , "Bad message type (expected `Connect`)"
	
	print("All tests OK!")
