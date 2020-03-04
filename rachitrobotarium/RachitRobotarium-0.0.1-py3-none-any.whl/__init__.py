from rps.robotarium_abc import RobotariumABC
from RachitRobotarium.utils import mode_messages
import numpy as np
import random
import matplotlib.patches as patches
import math
import time
from typing import Tuple, List


class Obstacle:
    def __init__(self, x, y, width, height):
        """
        :param x: x-coordinates of the bottom-left corner of the obstacle
        :param y: y-coordinates of the bottom-left corner of the obstacle
        :param width: width of the obstacle
        :param height: height of the obstacle
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class RachitRobotarium(RobotariumABC):
    def __init__(self, number_of_robots=-1, show_figure=True, sim_in_real_time=True,
                 initial_coordinates=np.array([]), modes=np.array([]), obstacles=[], objective=(0, 0)):
        initial_coordinates_x = [coord[0] for coord in initial_coordinates]
        initial_coordinates_y = [coord[1] for coord in initial_coordinates]
        initial_coordinates_h = [0.0 for _ in initial_coordinates]
        number_of_robots = modes.shape[0]
        np_initial_coordinates = np.array([initial_coordinates_x, initial_coordinates_y, initial_coordinates_h])
        super().__init__(number_of_robots, show_figure, sim_in_real_time, np_initial_coordinates)

        #Initialize some rendering variables
        self.previous_render_time = time.time()
        self.sim_in_real_time = sim_in_real_time

        #Initialize checks for step and get poses calls
        self._called_step_already = True
        self._checked_poses_already = False

        #Initialization of error collection.
        self._errors = {}

        #Initialize steps
        self._iterations = 0

        self.obstacles = obstacles
        self.objective = objective

        if modes.shape[0] == 0:
            self.modes = np.array([random.randint(0, 2) for _ in range(number_of_robots)])
        else:
            self.modes = modes

        self._colors = {0: 'FFD700',
                        1: '74d2b3',
                        2: 'bd23e3'}

        self._speeds = {0: 0.20,
                        1: 0.10,
                        2: 0.05}  # speed tracker

        self._distances = {0: 0.25,
                           1: 0.25,
                           2: 0.75}

        self.obstacle_patches = []
        self.sense_radius_patches = []
        self.ravine_patches = []
        self.robots = []

        for i in range(number_of_robots):
            color = self._colors[self.modes[i]]
            self.chassis_patches[i].set_facecolor(f"#{color}")
            sr = patches.Circle(self.poses[:2, i], self._distances[self.modes[i]], fill=False)
            self.sense_radius_patches.append(sr)
            self.axes.add_patch(sr)
            self.robots.append(Robot(self.chassis_patches[i], self))

        for curr_obstacle in obstacles:
            obs = patches.Rectangle((curr_obstacle.x, curr_obstacle.y), curr_obstacle.width, curr_obstacle.height)
            self.obstacle_patches.append(obs)
            self.axes.add_patch(obs)

    def set_velocities(self, ids, velocities):
        # Threshold linear velocities
        idxs = np.where(np.abs(velocities[0, :]) > np.array([self._speeds[curr_mode] for curr_mode in self.modes]))
        velocities[0, idxs] = np.array([self._speeds[self.modes[curr_id]] for curr_id in idxs[0]]) * np.sign(velocities[0, idxs])

        # Threshold angular velocities
        idxs = np.where(np.abs(velocities[1, :]) > self.max_angular_velocity)
        velocities[1, idxs] = self.max_angular_velocity*np.sign(velocities[1, idxs])
        self.velocities = velocities

    def get_poses(self):
        """Returns the states of the agents.

        -> 3xN numpy array (of robot poses)
        """

        assert(not self._checked_poses_already), "Can only call get_poses() once per call of step()."
        # Allow step() to be called again.
        self._called_step_already = False
        self._checked_poses_already = True

        return self.poses

    def call_at_scripts_end(self):
        """Call this function at the end of scripts to display potentail errors.
        Even if you don't want to print the errors, calling this function at the
        end of your script will enable execution on the Robotarium testbed.
        """
        print('##### DEBUG OUTPUT #####')
        print('Your simulation will take approximately {0} real seconds when deployed on the Robotarium. \n'.format(math.ceil(self._iterations*0.033)))

        if bool(self._errors):
            if "boundary" in self._errors:
                print('\t Simulation had {0} {1}\n'.format(self._errors["boundary"], self._errors["boundary_string"]))
            if "collision" in self._errors:
                print('\t Simulation had {0} {1}\n'.format(self._errors["collision"], self._errors["collision_string"]))
            if "actuator" in self._errors:
                print('\t Simulation had {0} {1}'.format(self._errors["actuator"], self._errors["actuator_string"]))
        else:
            print('No errors in your simulation! Acceptance of your experiment is likely!')

        return

    def step(self):
        assert(not self._called_step_already), "Make sure to call get_poses before calling step() again."

        # Allow get_poses function to be called again.
        self._called_step_already = True
        self._checked_poses_already = False

        # Validate before thresholding velocities
        self._errors = self._validate()
        self._iterations += 1

        new_poses = self.poses[:, :]

        # Update dynamics of agents
        new_poses[0, :] = self.poses[0, :] + self.time_step*np.cos(self.poses[2,:])*self.velocities[0, :]
        new_poses[1, :] = self.poses[1, :] + self.time_step*np.sin(self.poses[2,:])*self.velocities[0, :]
        new_poses[2, :] = self.poses[2, :] + self.time_step*self.velocities[1, :]
        # Ensure angles are wrapped
        new_poses[2, :] = np.arctan2(np.sin(new_poses[2, :]), np.cos(new_poses[2, :]))

        for curr_robot_num in range(new_poses.shape[1]):
            curr_pose = new_poses[:, curr_robot_num]
            curr_mode = self.modes[curr_robot_num]
            if curr_mode == 0:
                for curr_obs in self.obstacles:
                    if curr_pose[0] + self.robot_radius > curr_obs.x and curr_pose[1] + self.robot_radius > curr_obs.y and curr_pose[0] - self.robot_radius < curr_obs.x + curr_obs.width and curr_pose[1] - self.robot_radius < curr_obs.y + curr_obs.height:
                        print(f"Obstacle hit! Cannot phase robot {curr_robot_num} through the obstacle - stopping...")
                        self.poses[2, curr_robot_num] = curr_pose[2]
                        self.velocities[0, curr_robot_num] = 0
                        continue
            self.poses[:, curr_robot_num] = curr_pose

        for curr_robot_num in range(new_poses.shape[1]):
            curr_pose = new_poses[:, curr_robot_num]
            curr_mode = self.modes[curr_robot_num]
            if curr_mode == 1:
                for curr_rav in self.ravine_patches:
                    if curr_rav.contains_point(curr_pose[0]) and curr_rav.contains_point(curr_pose[1]):
                        print(f"Ravine hit! Robot {curr_robot_num} incapable of swimming - stopping...")
                        self.poses[2, curr_robot_num] = curr_pose[2]
                        self.velocities[0, curr_robot_num] = 0
                        continue
            self.poses[:, curr_robot_num] = curr_pose

        # Update graphics
        if(self.show_figure):
            if(self.sim_in_real_time):
                t = time.time()
                while(t - self.previous_render_time < self.time_step):
                    t = time.time()
                self.previous_render_time = t

            for i in range(self.number_of_robots):
                self.chassis_patches[i].center = self.poses[:2, i]
                self.chassis_patches[i].orientation = self.poses[2, i] + math.pi/4

                self.right_wheel_patches[i].center = self.poses[:2, i]+self.robot_radius*np.array((np.cos(self.poses[2, i]+math.pi/2), np.sin(self.poses[2, i]+math.pi/2)))+\
                                        0.04*np.array((-np.sin(self.poses[2, i]+math.pi/2), np.cos(self.poses[2, i]+math.pi/2)))
                self.right_wheel_patches[i].orientation = self.poses[2, i] + math.pi/4

                self.left_wheel_patches[i].center = self.poses[:2, i]+self.robot_radius*np.array((np.cos(self.poses[2, i]-math.pi/2), np.sin(self.poses[2, i]-math.pi/2)))+\
                                        0.04*np.array((-np.sin(self.poses[2, i]+math.pi/2), np.cos(self.poses[2, i]+math.pi/2)))
                self.left_wheel_patches[i].orientation = self.poses[2,i] + math.pi/4

                self.right_led_patches[i].center = self.poses[:2, i]+0.75*self.robot_radius*np.array((np.cos(self.poses[2,i]), np.sin(self.poses[2,i])))-\
                                0.04*np.array((-np.sin(self.poses[2, i]), np.cos(self.poses[2, i])))
                self.left_led_patches[i].center = self.poses[:2, i]+0.75*self.robot_radius*np.array((np.cos(self.poses[2,i]), np.sin(self.poses[2,i])))-\
                                0.015*np.array((-np.sin(self.poses[2, i]), np.cos(self.poses[2, i])))
                self.sense_radius_patches[i].center = self.poses[:2, i]

            self.figure.canvas.draw_idle()
            self.figure.canvas.flush_events()

    def get_robot_mode(self, robot_num: int):
        if robot_num >= len(self.modes):
            raise IndexError("Number of robots available is lesser than the index requested. Remember that indexing " +
                             "starts from 0.")
        return self.modes[robot_num], mode_messages[self.modes[robot_num]]

    def sense_from_robot(self, robot_num: int):
        if robot_num >= len(self.modes):
            raise IndexError("Number of robots available is lesser than the index requested. Remember that indexing " +
                             "starts from 0.")
        robot_pose = self.poses[:, robot_num]
        robot_dist_cap = self._distances[self.modes[robot_num]]
        sense = []
        for curr_robot_num in range(len(self.modes)):
            if robot_num == curr_robot_num:
                continue
            curr_robot_pose = self.poses[:, curr_robot_num]
            distance = math.sqrt((robot_pose[0] - curr_robot_pose[0]) ** 2 + (robot_pose[1] - curr_robot_pose[1]) ** 2)
            if distance <= robot_dist_cap:
                sense.append([curr_robot_num, curr_robot_pose])
        return sense

    def move_robot(self, robot_nums: list, suggested_vel: list):
        vels = [[0.0 for _ in range(len(self.modes))], [0.0 for _ in range(len(self.modes))]]
        # vels = []
        for index, curr_robot in enumerate(robot_nums):
            if curr_robot >= len(self.modes):
                raise IndexError("Number of robots available is lesser than the index requested. Remember that " +
                                 "indexing starts from 0.")
            print(vels[curr_robot])
            vels[0][curr_robot], vels[1][curr_robot] = suggested_vel[index][0], suggested_vel[index][1]
            # vels.append(suggested_vel[index])
        print(vels)
        self.set_velocities(np.arange(len(self.modes)), np.array(vels))

    def add_ravine(self, ravine_type):
        # Possible ravine types: [P]ond, [L]ake, [T]ouch
        if ravine_type == 'P':
            r_patch = patches.Rectangle((-0.25, -0.25), 0.5, 0.5)
        elif ravine_type == 'L':
            r_patch = patches.Rectangle((-1, -2), 0.5, 4)
        elif ravine_type == 'T':
            r_patch_1 = patches.Rectangle((-1.1, 0.3), 0.2, 1)
            r_patch_2 = patches.Rectangle((-1.1, 0.3), -1, 0.2)
            self.ravine_patches.append(r_patch_1)
            self.ravine_patches.append(r_patch_2)
            self.axes.add_patch(r_patch_1)
            self.axes.add_patch(r_patch_2)
            return None
        else:
            return None
        self.ravine_patches.append(r_patch)
        self.axes.add_patch(r_patch)
        return None

    def get_robots(self):
        return self.robots

    def has_reached_objective(self):
        for curr_robot in self.robots:
            if curr_robot.is_point_inside(self.objective):
                return True
        return False


class Robot:
    def __init__(self, robot_patch: patches.Patch, robotarium: RobotariumABC):
        self.curr_robot_patch = robot_patch
        self.robotarium = robotarium

    def is_point_inside(self, coordinates: Tuple[float, float]) -> bool:
        return self.curr_robot_patch.contains_point(coordinates)

    def get_robotarium_instance(self) -> RobotariumABC:
        return self.robotarium

    def get_curr_coordinates(self) -> List[float]:
        return self.curr_robot_patch.get_verts()[:-1, :].mean(axis=0).tolist()
