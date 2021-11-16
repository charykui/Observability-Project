# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  # Use any version between 15.2.31.300 and 15.2.31.570
  config.vm.box = "opensuse/Leap-15.2.x86_64"
 

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 9090, host: 9090
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  #config.vm.network "forwarded_port", guest: 8888, host: 8080 
  config.vm.network "forwarded_port", guest: 9090, host: 8888
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  config.vm.network "forwarded_port", guest: 3030, host: 3030
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 16686, host: 8088
  #config.vm.network "forwarded_port", guest: 8000, host: 8888
  config.vm.network "forwarded_port", guest: 8888, host: 8888
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:clear

    vb.memory = "4096"
    #vb.memory = "2048"
    vb.name = "k3ss"
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
	  echo "******** Step 1: Installing dependencies ********"
      sudo zypper refresh
      
      sudo zypper --non-interactive install apparmor-parser
    
      echo -e "******** Begin installing k3s ********\n"
      curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644
      mkdir -p /home/vagrant/.kube
      /usr/local/bin/kubectl config view --raw >/home/vagrant/.kube/config
      echo -e "******** End installing k3s ********\n\n"
      echo -e "******** Step 2: Setting up Observability ********\n\n"
      echo -e "******** Begin installing Helm ********\n"
      export PATH=$PATH:/usr/loca/bin
      curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
      chmod 700 get_helm.sh
      ./get_helm.sh
      echo -e "******** End installing Helm ********\n\n"
      echo -e "******** Begin installing Grafana and Prometheus ********\n"
	  /usr/local/bin/kubectl create namespace monitoring
      /usr/local/bin/helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
      /usr/local/bin/helm repo add stable https://charts.helm.sh/stable
      /usr/local/bin/helm repo update
      #/usr/local/bin/helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --kubeconfig /etc/rancher/k3s/k3s.yaml
      echo -e "******** End installing Grafana and Prometheus ********\n\n"
      echo -e "******** Begin installing Jaeger ********\n"
	  /usr/local/bin/kubectl create namespace observability
      /usr/local/bin/kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/crds/jaegertracing.io_jaegers_crd.yaml
      /usr/local/bin/kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/service_account.yaml
      /usr/local/bin/kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/role.yaml
      /usr/local/bin/kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/role_binding.yaml
      /usr/local/bin/kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/operator.yaml
      echo -e "******** End installing Jaeger ********\n\n"
      echo "******** Verify helm is installed ********"
      /usr/local/bin/helm ls --kubeconfig /etc/rancher/k3s/k3s.yaml --namespace=monitoring
	  echo "******** Verify prometheus grafana is running ********"
      /usr/local/bin/kubectl get pods --namespace=monitoring
      echo "******** Verify jaeger is running ********"
      /usr/local/bin/kubectl get pods --namespace=observability
    SHELL
end
