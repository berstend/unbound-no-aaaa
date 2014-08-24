sudo apt-get update
sudo apt-get install unbound -y
sudo apt-get install python-unbound -y
sudo apt-get install vim -y
#echo nameserver 127.0.0.1 | sudo tee /etc/resolv.conf
sudo service unbound stop
