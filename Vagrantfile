# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.hostname = "photolab"

    config.vm.network "forwarded_port", guest: 80, host: 8000

    config.vm.provider "virtualbox" do |vbx|
        vbx.name = "photolab"
        vbx.memory = 512
        vbx.cpus = 1
    end

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "provision.yml"
        ansible.extra_vars = { ansible_ssh_user: 'vagrant' }
    end
end
