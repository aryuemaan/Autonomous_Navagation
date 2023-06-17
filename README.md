# Autonomous Navigation Car


This repository contains the code and resources for an autonomous navigation car. The car is designed to navigate and maneuver through an environment using various sensors and algorithms. It provides a platform for developing and testing autonomous navigation algorithms and systems.

## Features

- **Sensor Integration**: The car is equipped with various sensors such as cameras, LiDAR, and ultrasonic sensors to perceive the environment.

- **Perception**: The perception module processes sensor data to understand the surroundings, detect obstacles, and estimate the car's position.

- **Mapping**: The mapping module generates a map of the environment based on sensor data and the car's movement.

- **Path Planning**: The path planning module generates a safe and optimal path for the car to navigate from the starting point to the desired destination.

- **Control**: The control module uses the generated path to control the car's actuators, such as steering, throttle, and braking, to execute the planned path.

- **Simulation**: The repository provides a simulation environment to test and validate the autonomous navigation algorithms before deploying them on a physical car.

## Prerequisites

- Python 3.7 or above
- NVIDIA GPU (optional, for accelerated computation)
- ROS (Robot Operating System) [Link to installation guide](https://www.ros.org/install/)
- OpenCV [Link to installation guide](https://docs.opencv.org/4.5.2/d7/d9f/tutorial_linux_install.html)
- TensorFlow [Link to installation guide](https://www.tensorflow.org/install)
- PyTorch [Link to installation guide](https://pytorch.org/get-started/locally/)
- CUDA (optional, for GPU acceleration with TensorFlow and PyTorch)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aryuemaan/autonomous_navigation.git
   ```

2. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Build the project:

   ```bash
   cd autonomous-navigation-car
   mkdir build && cd build
   cmake ..
   make
   ```

4. Download additional resources (e.g., pre-trained models, sample datasets) if required.

## Usage

1. Launch the simulation environment:

   ```bash
   roslaunch autonomous_navigation_car simulation.launch
   ```

2. Run the main control script:

   ```bash
   python main.py
   ```

   Note: Customize the script according to your specific requirements, such as sensor configurations, path planning algorithms, etc.

3. Monitor the car's behavior and navigation through the simulation environment or visualize the output on a separate interface.

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request. Make sure to follow the project's code of conduct.

## License

This project is licensed under the [GNU-General-Public-License-v3.0/LICENSE](LICENSE).

## Acknowledgments

- [ROS](https://www.ros.org/) - Robot Operating System
- [OpenCV](https://opencv.org/) - Computer Vision Library
- [TensorFlow](https://www.tensorflow.org/) - Machine Learning Framework
- [PyTorch](https://pytorch.org/) - Deep Learning Library

## Contact

For any questions or inquiries, please contact the project maintainer:aryucho@gmail.com
