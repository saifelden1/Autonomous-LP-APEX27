FROM osrf/ros:jazzy-desktop-full

ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL=/bin/bash

# Install core build, network, GUI, and robotics developer tools
RUN apt-get update && apt-get install -y --no-install-recommends \
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
    ros-jazzy-joint-state-publisher-gui \
    ros-jazzy-xacro \
    ros-jazzy-tf2-tools \
    ros-jazzy-ros-gz \
    ros-jazzy-cv-bridge \
    ros-jazzy-vision-msgs \
    ros-jazzy-navigation2 \
    ros-jazzy-nav2-bringup \
    ros-jazzy-robot-localization \
    python3-opencv \
    python3-numpy \
    python3-scipy \
    python3-matplotlib \
    && rm -rf /var/lib/apt/lists/*

# Setup ROS 2 workspace environment in bashrc
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc

WORKDIR /workspace

CMD ["/bin/bash"]
