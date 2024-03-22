# gonow
is it still open or not?


# install

On the pi:

1. generate key:  `ssh-keygen -o -t ed25519 -f ~/.ssh/id_ed25519 -C "gonow.local" -P ""` 
2. create Installation directory `sudo mkdir /opt/gonow && sudo chown -c pi /opt/gonow`
3. install git: `sudo apt install -y git`

Your Machine:

1. navigate into to the repository directory: `cd gonow`
2. copy the public key from the raspberry: `scp gonow:~/.ssh/id_ed25519.pub .`
3. give the key read rights: `gh repo deploy-key add id_ed25519.pub`
4. clean up: `rm id_ed25519.pub`

Finally, on the pi again:

1. `git clone https://github.com/blemli/gonow.git /opt/gonow`
2. install: `cd /opt/gonow && chmod +x setup/*.sh && setup/setup.sh`