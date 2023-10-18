#!/bin/bash

# Create an OvS bridge called wario-land
sudo ovs-vsctl add-br wario-land

# Create a network namespace called wario
sudo ip netns add wario

# Create a bridge internal interface
sudo ovs-vsctl add-port wario-land wario -- set Interface wario type=internal

# Plug the OvS bridge's internal port into the wario namespace
sudo ip link set wario netns wario

# Bring the interface UP in the wario namespace
sudo ip netns exec wario ip link set dev wario up

# Add an IP address to the interface
sudo ip netns exec wario ip addr add 10.64.0.10/24 dev wario
