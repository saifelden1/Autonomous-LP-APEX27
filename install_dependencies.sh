#!/usr/bin/env bash
# ==============================================================================
# APEX Racing Team — Autonomous Systems Environment Installer
# Target OS: Ubuntu 24.04 LTS (Noble Numbat)
# ROS 2 Distro: ROS 2 Jazzy Jalisco
# Simulation: Gazebo Harmonic / Gz Sim (ros_gz bridge)
# ==============================================================================

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}======================================================================${NC}"
echo -e "${GREEN}   APEX RACING TEAM — AUTONOMOUS SYSTEMS DEPENDENCY INSTALLER   ${NC}"
echo -e "${BLUE}   OS: Ubuntu 24.04 LTS | ROS: ROS 2 Jazzy | Sim: Gazebo Harmonic     ${NC}"
echo -e "${BLUE}======================================================================${NC}"
echo ""

# Verify OS is Ubuntu 24.04
if [ -f /etc/os-release ]; then
    . /etc/os-release
    if [ "$VERSION_CODENAME" != "noble" ]; then
        echo -e "${YELLOW}[WARNING] This script is tailored for Ubuntu 24.04 LTS (Noble). Detected: $PRETTY_NAME.${NC}"
        read -p "Do you want to continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${RED}Installation cancelled.${NC}"
            exit 1
        fi
    fi
fi

echo -e "${BLUE}[1/6] Updating APT repositories and base system tools...${NC}"
sudo apt update && sudo apt upgrade -y
sudo apt install -y \
    software-properties-common \
    curl \
    gnupg \
    lsb-release \
    build-essential \
    git \
    wget \
    terminator \
    nano

echo -e "${BLUE}[2/6] Configuring ROS 2 Jazzy Official GPG Key & Sources...${NC}"
sudo add-apt-repository universe -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update

echo -e "${BLUE}[3/6] Installing ROS 2 Jazzy Desktop & Colcon Build Tools...${NC}"
sudo apt install -y \
    ros-jazzy-desktop \
    ros-dev-tools \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool

echo -e "${BLUE}[4/6] Installing Gazebo Simulation & ROS 2 Bridge Integration...${NC}"
sudo apt install -y \
    ros-jazzy-ros-gz \
    ros-jazzy-joint-state-publisher-gui \
    ros-jazzy-xacro \
    ros-jazzy-tf2-tools \
    ros-jazzy-teleop-twist-keyboard \
    ros-jazzy-rqt* \
    ros-jazzy-cv-bridge \
    ros-jazzy-vision-msgs

echo -e "${BLUE}[5/6] Installing Python Computer Vision & Scientific Packages...${NC}"
sudo apt install -y \
    python3-numpy \
    python3-opencv \
    python3-scipy \
    python3-matplotlib

echo -e "${BLUE}[6/6] Initializing rosdep & Configuring Shell Sourcing...${NC}"
if [ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then
    sudo rosdep init
fi
rosdep update

# Add ROS 2 environment overlay to ~/.bashrc if not already present
if ! grep -q "source /opt/ros/jazzy/setup.bash" ~/.bashrc; then
    echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
    echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
    echo -e "${GREEN}[OK] Added ROS 2 Jazzy auto-sourcing to ~/.bashrc.${NC}"
fi

source /opt/ros/jazzy/setup.bash

echo ""
echo -e "${GREEN}======================================================================${NC}"
echo -e "${GREEN}✅ INSTALLATION COMPLETE!${NC}"
echo -e "• Active ROS Distro: ${YELLOW}$ROS_DISTRO${NC}"
echo -e "• Verify command:    ${BLUE}ros2 --help${NC}"
echo -e "• Check topics:      ${BLUE}ros2 topic list${NC}"
echo -e "${GREEN}======================================================================${NC}"
