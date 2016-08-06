# Ansible 
## checks

verify that you can ping your server via ssh

    ansible all --user=root --private-key=<SSH_KEY> --inventory-file='<IP>,' -m ping

    192.168.1.100 | SUCCESS => {
        "changed": false,
        "ping": "pong"
    }

## modify personal information
secrets information

    ansible-vault edit secrets.yml


## setup your server

now run bootstrap.yml file

    ansible-playbook --user=root --private-key=<SSH_KEY> --ask-become-pass  --ask-vault-pass --inventory-file='<IP>,' bootstrap.yml

    
## install docker on it

    ansible-playbook --user=admin --private-key=<SSH_KEY> --ask-become-pass --inventory-file='<IP>,' docker.yml


Add admin user to docker group.

    sudo usermod -aG docker admin

Log out and log back in.

## install compose

become sudo

    sudo -i

install docker
    
    curl -L https://github.com/docker/compose/releases/download/1.7.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose

make compose executable

    chmod +x /usr/local/bin/docker-compose
