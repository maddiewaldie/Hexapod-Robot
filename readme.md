# Hexapod Robot

## Overview

This project involves the creation of a hexapod robot with six legs, each having three joints (distal, mid, and proximal). The robot's movement and coordination are managed through a custom Python program running on a Pimoroni microcontroller.

### Hardware Components

* **Microcontroller:** This project uses the [Pimoroni Servo 2040](https://shop.pimoroni.com/products/servo-2040?variant=39800591679571) microcontroller.
* **Servos:** The robot uses 18 [MG996R 55g Metal Gear Torque Digital Servo Motors](https://www.amazon.com/dp/B07MFK266B?ref=ppx_pop_mob_ap_share&th=1).
* **3D Printed Model:** The hexapod structure is based on [SimpleRobotics' 3D printed model available on MakerWorld](https://makerworld.com/en/models/523424#profileId-440772).

### Software Components

* **MicroPython:** The project utilizes [MicroPython](https://micropython.org) for controlling the hardware.
* **Servo Library:** [Pimoroni Servo Library](https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/servo#servo-2040) is used for managing servo operations.

## Project Structure

### Files

* **constants.py:** Contains constants used throughout the project.
* **hexapod.py:** Defines the Hexapod class, which manages the overall robot operations.
* **leg.py:** Defines the Leg class, which manages individual leg operations.
* **servoWrapper.py:** Provides a unified interface to handle both regular servos and servo clusters seamlessly.
* **main.py:** The main script to initialize and run the hexapod robot.
