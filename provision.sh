sudo apt-get update
sudo apt-get install -o Dpkg::Options::="--force-confold" --force-yes -y unbound
sudo apt-get install -o Dpkg::Options::="--force-confold" --force-yes -y python-unbound
#echo nameserver 127.0.0.1 | sudo tee /etc/resolv.conf
sudo service unbound stop
