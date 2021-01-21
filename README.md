> This repository compiles part of my experiences simulating and visualizing robots and their environments, and integrating reinforcement learning algorithms using **[NVIDIA Isaac Sim](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/overview.html) (2020.2.2 Early Access)**

<hr>

### Table of Contents

[**Create a derivative docker image for internal use for test and development**](#deployment-top)
- [Login into NGC](#deployment-ngc)
- [Download and run the Isaac Sim container](#deployment-download)
- [Enable ssh access](#deployment-ssh)
- [Commit the modified container to a docker image](#deployment-commit)
- [Run the derivative container and detach form it](#deployment-run)
- [Execute the derivative container](#deployment-exec)

[**Create a Nucleus docker image if the Nucleus Deployment could not be done**](#deployment-nucleus-top)
- [Download and run an Ubuntu 18.04 container](#deployment-nucleus-ubuntu)
- [Copy the Nucleus Linux Installer into the container](#deployment-nucleus-copy-to-docker)
- [Execute the container and install Nucleus](#deployment-nucleus-install)
- [Commit the modified container to a docker image](#deployment-nucleus-commit)
- [Run the container and start services (server & web)](#deployment-nucleus-run)

[**Useful commands and tips**](#tips-top)
- [Run Isaac Sim headless](#tips-runheadless)
- [Install python packages to be used with Isaac Sim](#tips-python)
- [Install ROS melodic to be used with Isaac Sim](#tips-ros)

[**Setup this repository**](#setup-top)
- [Add custom assets](#setup-assets)
- [Install python dependencies](#setup-python)
- [Install and configure RLlib library for reinforcement learning](#setup-rllib)
- [Copy/clone, enable and run this repository](#setup-run)

<hr>

<a name="deployment-top"></a>
## Create a derivative docker image for internal use for test and development

The next steps create a derivative docker image based on the [Remote Workstation Deployment](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/setup.html#remote-workstation-deployment) documentation

<a name="deployment-ngc"></a>
### Login into NGC before downloading the Isaac Sim container

Get the NGC API Key by clicking Generate API Key at [https://ngc.nvidia.com/setup/api-key](https://ngc.nvidia.com/setup/api-key)

```
docker login nvcr.io
```

<a name="deployment-download"></a>
### Download and run the Isaac Sim container

```
docker pull nvcr.io/nvidia/isaac-sim:2020.2.2_ea
```

Edit GPU devices before running the docker image according to the computer specifications

- Use ```--gpus all``` to select all GPUs or ```--gpus "device=GPU_ID"``` or ```--gpus device=0,2``` to select a specific GPU. Check your GPUs capabilities with the command line utility ```nvidia-smi```

```
docker run --gpus all -e "ACCEPT_EULA=Y" --name isaac-sim-template-base-2020.2.2_ea --interactive --entrypoint /bin/bash --detach nvcr.io/nvidia/isaac-sim:2020.2.2_ea
```

Run the detached container

```
docker exec -it isaac-sim-template-base-2020.2.2_ea bash
```

<a name="deployment-ssh"></a>
### Enable ssh access

Set a memorable password for root (like 'root')

```
passwd root
```

Install shh service

```
apt update
apt install ssh
service ssh restart
```

Edit the ssh configuration file to allow root login. Uncomment **PermitRootLogin prohibit-password** and replace by **PermitRootLogin yes**

````
apt install nano
nano /etc/ssh/sshd_config
````

Restart the ssh service

````
service ssh restart
````

<a name="deployment-commit"></a>
### Commit the modified container to a docker image

Detach from the docker container using the key sequence <kbd>Ctrl</kbd> + <kbd>P</kbd> <kbd>Ctrl</kbd> + <kbd>Q</kbd> and commit the changes

```
docker commit isaac-sim-template-base-2020.2.2_ea isaac-sim-template-2020.2.2_ea
```

To see the committed image (isaac-sim-template-2020.2.2_ea) use the command ```docker images```.
Also, the running container could be removed (isaac-sim-template-base-2020.2.2_ea)

```
docker stop isaac-sim-template-base-2020.2.2_ea
docker container rm isaac-sim-template-base-2020.2.2_ea
```

<a name="deployment-run"></a>
### Run the derivative container and detach form it

- Export ssh port to 12222: ```-p 12222:22```

- Export [Robot Engine Bridge](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/robot_engine_bridge.html) (Isaac SDK integration with Omniverse Isaac Sim) port: ```-p 55000-55001:55000-55001```

- Also, export some general-purpose ports for future usage: ```-p 55002-55010:55002-55010```

```
docker run -it --gpus all -e "ACCEPT_EULA=Y" --name isaac-sim-sample-2020.2.2_ea --entrypoint /bin/bash -p 47995-48012:47995-48012/udp -p 47995-48012:47995-48012/tcp -p 49000-49007:49000-49007/tcp -p 49000-49007:49000-49007/udp -p 12222:22 -p 55000-55001:55000-55001 -p 55002-55010:55002-55010 isaac-sim-template-2020.2.2_ea
```

Detach from the docker container using the key sequence <kbd>Ctrl</kbd> + <kbd>P</kbd> <kbd>Ctrl</kbd> + <kbd>Q</kbd>

<a name="deployment-exec"></a>
### Execute the derivative container

```
docker exec -it isaac-sim-sample-2020.2.2_ea bash
```

<a name="deployment-nucleus-top"></a>
## Create a Nucleus docker image if the [Nucleus Deployment](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/setup.html#nucleus-deployment) could not be done

<a name="deployment-nucleus-ubuntu"></a>
### Download and run an [Ubuntu 18.04](https://hub.docker.com/_/ubuntu) container

```
docker pull ubuntu:18.04
docker run --name omniverse-nucleus-template-base --interactive --entrypoint /bin/bash --detach ubuntu:18.04
```

<a name="deployment-nucleus-copy-to-docker"></a>
### Copy the [Nucleus Linux Installer](https://developer.nvidia.com/isaac-sim/downloads/nucleus-linux64) into the container

Upload the Linux installer to the remote workstation and copy it into the container 

```
docker cp omniverse-nucleus-2019.3A.2282-1-linux-installer.run omniverse-nucleus-template-base:/home
```

<a name="deployment-nucleus-install"></a>
### Execute the container and install Nucleus

```
docker exec -it omniverse-nucleus-template-base bash
```

##### Install dependencies

```
apt update
apt install libpython2.7
apt install tmux
apt install sudo
```

##### Install Nucleus

```
cd /home
sudo chmod +x omniverse-nucleus-2019.3A.2282-1-linux-installer.run
sudo ./omniverse-nucleus-2019.3A.2282-1-linux-installer.run
rm omniverse-nucleus-2019.3A.2282-1-linux-installer.run
```

<a name="deployment-nucleus-commit"></a>
### Commit the modified container to a docker image

Detach from the docker container using the key sequence <kbd>Ctrl</kbd> + <kbd>P</kbd> <kbd>Ctrl</kbd> + <kbd>Q</kbd> and commit the changes

```
docker commit omniverse-nucleus-template-base omniverse-nucleus-template
```

To see the committed image (omniverse-nucleus-template) use the command ```docker images```.
Also, the running container could be removed (omniverse-nucleus-template-base)

```
docker stop omniverse-nucleus-template-base
docker rm omniverse-nucleus-template-base
```

<a name="deployment-nucleus-run"></a>
### Run the container and start services (server & web)

```
docker run -it --name omniverse-nucleus-sample --entrypoint /bin/bash -p 2000-2001:2000-2001 -p 3020:3020 -p 3030:3030 -p 3100:3100 -p 3120:3120 -p 3180:3180 -p 3333:3333 -p 3400:3400 -p 9500:9500 -p 3007-3009:3007-3009 -p 8080:8080 omniverse-nucleus-template
```

##### Start service: server

```
tmux new -s server
cd /var/lib/omniverse/server
/opt/nvidia/omniverse/server/omni.server.app -input false
```

Detach current tmux session using <kbd>Ctrl</kbd> + <kbd>b</kbd> <kbd>d</kbd>. Note: if there is a nested tmux session use <kbd>Ctrl</kbd> + <kbd>b</kbd> <kbd>Ctrl</kbd> + <kbd>b</kbd> <kbd>d</kbd>

##### Start service: web

```
tmux new -s web
cd /var/lib/omniverse/web
/opt/nvidia/omniverse/web/OmniverseWeb
```

Detach current tmux session using <kbd>Ctrl</kbd> + <kbd>b</kbd> <kbd>d</kbd>. Note: if there is a nested tmux session use <kbd>Ctrl</kbd> + <kbd>b</kbd> <kbd>Ctrl</kbd> + <kbd>b</kbd> <kbd>d</kbd>

<a name="tips-top"></a>
## Useful commands and tips

<a name="tips-runheadless"></a>
### Run Isaac Sim headless

```
/bin/sh -c /isaac-sim/runheadless.sh
```

<a name="tips-python"></a>
### Install python packages to be used with Isaac Sim

Isaac Sim uses its own Python 3 interpreter

```
cd /isaac-sim/_build/target-deps/kit_sdk_release/_build/target-deps/python
bin/python3 -m pip install <PACKAGE>
```

<a name="tips-ros"></a>
### Install [ROS melodic](http://wiki.ros.org/melodic/Installation/Ubuntu) to be used with Isaac Sim

Install lsb-release (tool to help identify the Linux distribution)

```
apt install lsb-release
```

Setup the sources.list and keys

```
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

Install the ROS package, build, and communication libraries (without GUI tools)

```
apt update
apt install ros-melodic-ros-base
```

Continue with the environment setup, and the dependencies for building packages [here](http://wiki.ros.org/melodic/Installation/Ubuntu) 

##### Install [rosbridge_suite](http://wiki.ros.org/rosbridge_suite) and [roslibpy](https://roslibpy.readthedocs.io/en/latest/)

```
apt install ros-melodic-rosbridge-suite
```

```
cd /isaac-sim/_build/target-deps/kit_sdk_release/_build/target-deps/python

bin/python3 -m pip install roslibpy
```

- To launch rosbridge and its packages run:

```
roslaunch rosbridge_server rosbridge_websocket.launch
```

<a name="setup-top"></a>
## Setup this repository

This repository includes two custom approach (at the moment) about how to simulate robotics scenarios:

**Robots**:
- Kuka LBR iiwa 14
- Willow Garage PR2

**Projects**:
- Sample: Just a simple picking scenario
- Reinforcement Learning (locally): reinforcement learning scenario using [Gym environments](https://gym.openai.com/docs/) and the [RlLib](https://docs.ray.io/en/latest/rllib.html) library (at the moment only Kuka LBR iiwa 14)

<a name="setup-assets"></a>
### Add custom assets

Download the custom assets according to the Nucleus server status using the next link: [https://drive.google.com/drive/folders/1ASg78TqJOM8bFx3jHWAwBqVKvyOQmLB8?usp=sharing](https://drive.google.com/drive/folders/1ASg78TqJOM8bFx3jHWAwBqVKvyOQmLB8?usp=sharing). The downloaded file must be unzipped inside the ```Isaac``` folder (without removing the existing files) in both cases

Note: If the [Nucleus](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/setup.html#nucleus-deployment) server cannot be installed, it is possible to add the assets into the folder ```/isaac-sim/art_assets/Isaac``` inside the container

<a name="setup-python"></a>
### Install python dependencies

```
cd /isaac-sim/_build/target-deps/kit_sdk_release/_build/target-deps/python

bin/python3 -m pip install --upgrade pip
bin/python3 -m pip install ikpy
```

<a name="setup-rllib"></a>
### Install and configure [RLlib](https://docs.ray.io/en/latest/rllib.html) library for reinforcement learning

##### Install RLlib

- Uninstall the previous version of tensorflow if exists

```
cd /isaac-sim/_build/target-deps/kit_sdk_release/_build/target-deps/python
bin/python3 -m pip uninstall tensorflow
```

- Install python packages

```
cd /isaac-sim/_build/target-deps/kit_sdk_release/_build/target-deps/python

bin/python3 -m pip install gym
bin/python3 -m pip install tensorflow
# bin/python3 -m pip install ray[rllib] ray[debug]
bin/python3 -m pip install ray[rllib]==1.0.0 ray[debug]==1.0.0
```

##### Configure Isaac Sim to work with RLlib

- Edit the python bindings for Isaac Sim extension init file to [configure](https://docs.ray.io/en/latest/configure.html) and start Ray cluster once (add the code at the end of the file). Also, change ```num_cpus``` and ```num_gpus``` parameters according to the computer specifications

```
nano /isaac-sim/_build/target-deps/kit_sdk_release/_build/linux-x86_64/release/plugins/bindings-python/omni/ext/__init__.py
```

```
try:
    print("")
    print("+++++++++++++++++++++++++++")
    print("[RAY][TRY] ray.init...")
    import ray
    ray.init(num_cpus=1,
             num_gpus=1,
             local_mode=True,
             include_dashboard=True,
             configure_logging=True,
             _temp_dir="/isaac-sim/ray")
    print("[RAY][DONE] ray")
except Exception as e:
    import traceback
    print("[RAY][ERROR] traceback:", traceback.format_exc())
print("---------------------------")
print("")
``` 

- Comment ```config["use_state_preprocessor"] = True``` inside the function ```def validate_config(config):``` around line 158 in the file ```ray/rllib/agents/ddpg/ddpg.py``` to allow custom DDPG model with non-arbitrary ```num_outputs = 256``` (defined in ```ray/rllib/agents/ddpg/ddpg_tf_policy.py```)

```
nano /isaac-sim/_build/target-deps/kit_sdk_release/_build/target-deps/python/lib/python3.6/site-packages/ray/rllib/agents/ddpg/ddpg.py
```

##### Launch Tensorboard results (optionally)

- Use ```--bind_all``` to expose Tensorboard to the network if it is not possible to access remotely
- The ```PATH_TO_ray_results_DIRECTORY``` is ```/root/ray_results/``` typically

```
/isaac-sim/_build/target-deps/kit_sdk_release/_build/target-deps/python/bin/python3 -m tensorboard.main --bind_all --port 55002 --logdir=PATH_TO_ray_results_DIRECTORY
```

or, it is previously installed apart from Isaac Sim

```
tensorboard --port 55002 --logdir PATH_TO_ray_results_DIRECTORY
```

<a name="setup-run"></a>
### Copy/clone, enable and run this repository

Copy or clone this repository (keeping the name ```isaac.sim.project```) to the path ```/isaac-sim/_build/linux-x86_64/release/exts```


```
apt install git
cd /isaac-sim/_build/linux-x86_64/release/exts
git clone https://github.com/Toni-SM/isaac.sim.project.git
```

Then, enable this extension in the menu *Window > Extension Manager* under the same name. This will enable the samples menu under *Projects*

**Note:** The Reinforcement Learning [README](scripts/reinforcement_learning_locally) provides more info about how to run it