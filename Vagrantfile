# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--name", "unbound-no-aaaa", "--memory", "512"]
  end

  # Shared folder from the host machine to the guest machine. Uncomment the line
  # below to enable it.
  config.vm.synced_folder "etc/unbound/", "/etc/unbound"
  config.vm.provision "shell", path: "provision.sh"
end
