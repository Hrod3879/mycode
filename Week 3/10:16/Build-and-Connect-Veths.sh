# Connects phost to the pbridge (1)
sudo ip link add phost2pbrg type veth peer name pbrg2phost
sudo ip link set phost2pbrg netns phost
sudo ip link set dev pbrg2phost master pbridge
sudo ip link set dev pbrg2phost up

# Connects prouter to the pbridge (2)
sudo ip link add prout2pbrg type veth peer name pbrg2prout
sudo ip link set prout2pbrg netns prouter
sudo ip link set dev pbrg2prout master pbridge
sudo ip link set dev pbrg2prout up

# Connects yhost to the ybridge (3)
sudo ip link add yhost2ybrg type veth peer name ybrg2yhost
sudo ip link set yhost2ybrg netns yhost
sudo ip link set dev ybrg2yhost master ybridge
sudo ip link set dev ybrg2yhost up

# Connects yrouter to the ybridge (4)
sudo ip link add yrout2ybrg type veth peer name ybrg2yrout
sudo ip link set yrout2ybrg netns yrouter
sudo ip link set dev ybrg2yrout master ybridge
sudo ip link set dev ybrg2yrout up

# Connects whost to the wbridge (5)
sudo ip link add whost2wbrg type veth peer name wbrg2whost
sudo ip link set whost2wbrg netns whost
sudo ip link set dev wbrg2whost master wbridge
sudo ip link set dev wbrg2whost up

# Connects wrouter to the wbridge (6)
sudo ip link add wrout2wbrg type veth peer name wbrg2wrout
sudo ip link set wrout2wbrg netns wrouter
sudo ip link set dev wbrg2wrout master wbridge
sudo ip link set dev wbrg2wrout up

# Connects ohost to the obridge (7)
sudo ip link add ohost2obrg type veth peer name obrg2ohost
sudo ip link set ohost2obrg netns ohost
sudo ip link set dev obrg2ohost master obridge
sudo ip link set dev obrg2ohost up

# Connects orouter to the obridge (8)
sudo ip link add orout2obrg type veth peer name obrg2orout
sudo ip link set orout2obrg netns orouter
sudo ip link set dev obrg2orout master obridge
sudo ip link set dev obrg2orout up

# Connects prouter to crouter (9)
sudo ip link add crout2prout type veth peer name prout2crout
sudo ip link set crout2prout netns crouter
sudo ip link set prout2crout netns prouter

# Connects yrouter to crouter (10)
sudo ip link add crout2yrout type veth peer name yrout2crout
sudo ip link set crout2yrout netns crouter
sudo ip link set yrout2crout netns yrouter

# Connects wrouter to crouter (11)
sudo ip link add crout2wrout type veth peer name wrout2crout
sudo ip link set crout2wrout netns crouter
sudo ip link set wrout2crout netns wrouter
   
# Connects orouter to crouter (12)
sudo ip link add crout2orout type veth peer name orout2crout
sudo ip link set crout2orout netns crouter
sudo ip link set orout2crout netns orouter

# Connects crouter to nat
# Connects nat to crouter (13)
sudo ip link add crout2nat type veth peer name nat2crout
sudo ip link set crout2nat netns crouter
#Leave the other end of the veth DANGLE in the root namespace. 

# Verify Veth are presnet
sudo ip netns exec phost ip link | grep -A 2 phost
sudo ip netns exec yhost ip link | grep -A 2 yhost
sudo ip netns exec whost ip link | grep -A 2 whost
sudo ip netns exec ohost ip link | grep -A 2 ohost
sudo ip netns exec crouter ip link | grep -A 5 crout
sudo ip netns exec prouter ip link | grep -A 2 prout
sudo ip netns exec yrouter ip link | grep -A 2 yrout
sudo ip netns exec wrouter ip link | grep -A 2 wrout
sudo ip netns exec orouter ip link | grep -A 2 orout

#Leave the other end of the veth DANGLE in the root namespace.

#Verification
ip link

