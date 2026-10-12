FROM osrf/ros:humble-desktop-full

ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL=/bin/bash

# Install core build and developer tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    git \
    curl \
    nano \
    tmux \
    wget \
    net-tools \
    iputils-ping \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    mesa-utils \
    ros-humble-joint-state-publisher-gui \
    ros-humble-xacro \
    ros-humble-tf2-tools \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-cv-bridge \
    ros-humble-vision-msgs \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-robot-localization \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies for perception and testing
RUN pip3 install --no-cache-dir \
    numpy \
    opencv-python \
    scipy \
    matplotlib

# Setup ROS 2 workspace environment
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

WORKDIR /workspace

CMD ["/bin/bash"]
