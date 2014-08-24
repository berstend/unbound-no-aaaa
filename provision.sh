sudo apt-get update
sudo apt-get install -o Dpkg::Options::="--force-confold" --force-yes -y unbound
sudo apt-get install -o Dpkg::Options::="--force-confold" --force-yes -y python-unbound
sudo apt-get install vim -y
#echo nameserver 127.0.0.1 | sudo tee /etc/resolv.conf
sudo service unbound stop
