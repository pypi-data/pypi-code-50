import casadi.casadi as cs
import opengen as og
import matplotlib.pyplot as plt
import numpy as np
import logging as lg
from mpl_toolkits import mplot3d

from opengen.config import BuildConfiguration
from scipy.optimize import minimize, Bounds, NonlinearConstraint
from ttictoc import TicToc

# =====================================================
# 3D 4 link RRRR elbow manipulator, moving obstacle. Passing OpEn obstacle centre
#
# based on:
# BICYCLE MODEL + Obstacle avoidance by Pantelis Sopasakis <p.sopasakis@qub.ac.uk>
#
# Author: Shane Trimble, Feb 2020
# =====================================================


# System dynamics
# --------------------------------------

length_1 = 0.35  # set link 1 length
length_2 = 0.35  # set link 2 length
length_3 = 0.35
length_4 = 0.35

sampling_time = 0.05    # set sampling time
nx = 4  # state variables:  x = (theta_1,theta_2, theta_3)
nu = 4  # control variables:  u = (omega_1, omega_2, omega_3)

# 90 degree turn from start
x_ref = 1.049
y_ref = 0
z_ref = 0.35

# Obstacle
# ---------------------------------------
xcc = 1.2
ycc = 0
zcc = 0.3
radius = 0.3
safety_margin = 10  # percent
safety_radius = radius + (radius/safety_margin)

# Input constraints
# --------------------------------------
controller_min = -.5
controller_max = .5

# Controller parameters
# --------------------------------------
N = 20  # less around 15

(q_x4diff, q_y4diff, q_x4diff) = (20, 20, 20) # weird behaviour on theta_2 when (200,200,200)
(q_x4diffn, q_y4diffn, q_z4diffn) = (200, 200, 200)

q_delta_omega1 = 10  #
q_delta_omega2 = 10  #
q_delta_omega3 = 10  #
q_delta_omega4 = 10  #


# Simulation options
# --------------------------------------

simulation_steps = 10

# function to convert angles to positions

def RRRR_Forward_Kinematics(theta_1, theta_2, theta_3, theta_4):
    x_1 = 0
    y_1 = 0
    z_1 = length_1

    x_2 = length_2 * cs.cos(theta_2) * cs.sin(theta_1)
    y_2 = length_2 * cs.cos(theta_2) * cs.cos(theta_1)
    z_2 = z_1 + length_2 * cs.sin(theta_2)

    x_3 = x_2 + length_3 * cs.cos(theta_2 + theta_3) * cs.sin(theta_1)
    y_3 = y_2 + length_3 * cs.cos(theta_2 + theta_3) * cs.cos(theta_1)
    z_3 = z_2 + length_3 * cs.sin(theta_2 + theta_3)

    x_4 = x_3 + length_4 * cs.cos(theta_2 + theta_3 + theta_4) * cs.sin(theta_1)
    y_4 = y_3 + length_4 * cs.cos(theta_2 + theta_3 + theta_4) * cs.cos(theta_1)
    z_4 = z_3 + length_4 * cs.sin(theta_2 + theta_3 + theta_4)

    return [x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3, x_4, y_4, z_4]

# distance from end-effector to target
def distance2ref(x4, y4, z4):
    distance_to_ref = cs.sqrt((x4-x_ref)**2+(y4 - y_ref)**2 + (z4 - y_ref)**2)
    return distance_to_ref

# state variables:  x = (theta_1, theta_2, theta_3, theta_4)
# controller inputs:  u = (omega_1, omega_2, omega_3, omega_4)
def dynamics_ct(xt, ut):
    omega_1 = ut[0]
    omega_2 = ut[1]
    omega_3 = ut[2]
    omega_4 = ut[3]
    theta_1 = xt[0]
    theta_2 = xt[1]
    theta_3 = xt[2]
    theta_4 = xt[3]
    return [omega_1, omega_2, omega_3, omega_4, theta_1, theta_2, theta_3, theta_4]

def dynamics_dt(xt, ut):
    dx = dynamics_ct(xt, ut)
    return [xt[idx] + sampling_time * dx[idx] for idx in range(nx)]

def stage_cost(xt, ut):
    current_x4 = RRRR_Forward_Kinematics(xt[0], xt[1], xt[2], xt[3])[9]
    current_y4 = RRRR_Forward_Kinematics(xt[0], xt[1], xt[2], xt[3])[10]
    current_z4 = RRRR_Forward_Kinematics(xt[0], xt[1], xt[2], xt[3])[11]

    cost = 0.1 * ut[0] ** 2 + 0.1 * ut[1] ** 2 + 0.1 * ut[2] ** 2 + 0.1 * ut[3] ** 2 \
           + q_x4diff * ((current_x4 - x_ref) ** 2) \
           + q_x4diff * ((current_y4 - y_ref) ** 2) \
           + q_y4diff * ((current_z4 - z_ref) ** 2)
    return cost

def terminal_cost(x_term):
    current_x4 = RRRR_Forward_Kinematics(x_term[0], x_term[1], x_term[2], x_term[2])[9]
    current_y4 = RRRR_Forward_Kinematics(x_term[0], x_term[1], x_term[2], x_term[2])[10]
    current_z4 = RRRR_Forward_Kinematics(x_term[0], x_term[1], x_term[2], x_term[2])[11]

    cost = q_x4diffn * ((current_x4 - x_ref) ** 2) \
           + q_y4diffn * ((current_y4 - y_ref) ** 2) \
           + q_z4diffn * ((current_z4 - z_ref) ** 2)

    return cost

# distance from end-effector to obstacle centre
def distance_cc(x4 , y4, z4, obstacle_coord):
    distance_to_obstacle = cs.sqrt((x4 - obstacle_coord[0])**2 + (y4 - obstacle_coord[1])**2 + (z4 - obstacle_coord[2])**2)
    return distance_to_obstacle

# obstacle cost function
def obstacle_f(xpos, ypos, zpos, obstacle_coord):
    obs = safety_radius**2 - distance_cc(xpos, ypos, zpos, obstacle_coord)**2
    return obs

def obstacle(xpos, ypos, zpos, obstacle_coord):
    # Penalty function for the avoidance of a ball
    obs = cs.fmax(0, obstacle_f(xpos, ypos, zpos, obstacle_coord))
    return obs

# --------------------------------------
u_seq = cs.SX.sym("u", nu * N)  # sequence of all u's
x0 = cs.SX.sym("x0", nx)  # initial state
u_prev = cs.SX.sym("uprev", nu)
obstacle_coord = cs.SX.sym("centre_of_circle", 3)
obstacle_vel = cs.SX.sym("vel_of_circle", 3)

x_t = x0
total_cost = 0
total_cost += q_delta_omega1 * (u_seq[0] - u_prev[0]) ** 2 \
              + q_delta_omega2 * (u_seq[1] - u_prev[1]) ** 2 \
              + q_delta_omega3 * (u_seq[2] - u_prev[2]) ** 2 \
              + q_delta_omega4 * (u_seq[3] - u_prev[3]) ** 2

u_predicted_previous = u_prev
f2 = []
f1 = []
future_obstacle_pos = obstacle_coord


for t in range(0, N):
    u_t = u_seq[nu * t:nu * t + 4]
    print(u_t)
    total_cost += stage_cost(x_t, u_t)  # update cost
    # Additional cost on input rate
    if t >= 1:
        delta_u_t = u_t - u_predicted_previous
        total_cost += q_delta_omega1 * delta_u_t[0] ** 2 \
                      + q_delta_omega2 * delta_u_t[1] ** 2 \
                      + q_delta_omega3 * delta_u_t[2] ** 2 \
                      + q_delta_omega4 * delta_u_t[3] ** 2

    x_t = dynamics_dt(x_t, u_t)  # update state
    u_predicted_previous = u_t

    x4_current = RRRR_Forward_Kinematics(x_t[0], x_t[1], x_t[2], x_t[3])[9]
    y4_current = RRRR_Forward_Kinematics(x_t[0], x_t[1], x_t[2], x_t[3])[10]
    z4_current = RRRR_Forward_Kinematics(x_t[0], x_t[1], x_t[2], x_t[3])[11]

    f2 = cs.vertcat(f2, obstacle(x4_current, y4_current, z4_current, future_obstacle_pos))
    #f2 = cs.vertcat(f2, distance_cc(x4_current, y4_current, z4_current, future_obstacle_pos)**2 - safety_radius**2)
    f1 = cs.vertcat(f1, safety_radius**2 - distance_cc(x4_current, y4_current, z4_current, future_obstacle_pos)**2)
    future_obstacle_pos += obstacle_vel * sampling_time

total_cost += terminal_cost(x_t)  # terminal cost
param = cs.vertcat(x0, u_prev, obstacle_coord, obstacle_vel)

u_seq_min = [controller_min, controller_min, controller_min, controller_min] * N
u_seq_max = [controller_max, controller_max, controller_max, controller_max] * N
U = og.constraints.Rectangle(u_seq_min, u_seq_max)

# Pass problem to OpEn
# --------------------------------------
f1cset = og.constraints.Rectangle(None, [0.0] * N)
problem = og.builder.Problem(u_seq, param, total_cost) \
    .with_constraints(U) \
    .with_aug_lagrangian_constraints(f1, f1cset)
    #.with_penalty_constraints(f2)
    #


build_config = og.config.BuildConfiguration()\
    .with_build_directory("my_optimizers") \
    .with_build_mode("release") \
    .with_tcp_interface_config() \
    .with_open_version(local_path="/home/chung/NetBeansProjects/RUST/optimization-engine")

meta = og.config.OptimizerMeta().with_optimizer_name("ukacc_shanes_version")

solver_config = og.config.SolverConfiguration() \
    .with_tolerance(1e-4) \
    .with_max_inner_iterations(500) \
    .with_max_outer_iterations(8) \
    .with_initial_tolerance(1e-4) \
    .with_lbfgs_memory(40) \
    .with_cbfgs_parameters(1.0, 1e-10, 1e-10)\
    .with_delta_tolerance(1e-3) \
    .with_initial_penalty(2000) \
    .with_penalty_weight_update_factor(2)

builder = og.builder.OpEnOptimizerBuilder(problem,
                                          meta,
                                          build_config,
                                          solver_config)
builder.build()

# -------------------------------------------------------------------------
# Simulations
# -------------------------------------------------------------------------
mng = og.tcp.OptimizerTcpManager("my_optimizers/ukacc_shanes_version")
mng.start()

# x_state_0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]       # state variables:  x = (x_1,y_1,x_2,y_2,omega_1,omega_2)
# does this need some kinematics to make sense?
theta1_s = 0
theta2_s = 0
theta3_s = 0
theta4_s = 0

x_state_0 = [0, 0, 0, 0]
u_prev = [0, 0, 0, 0]  # control variables:  u = (omega_1, omega_2)
xcc_array = []
ycc_array = []
zcc_array = []
#obstacle_coord = [float(1), float(1), float(1)]
obstacle_vel = [-0.2, 0.2, 0] # in m^s
#obstacle_vel = [0, 0, 0] # in m^s

state_sequence = [x_state_0]
input_sequence = []
solver_time = []
x = x_state_0
initial_guess = None
obstacle_coord = [xcc, ycc, zcc]
obstacle_coord_array = []
x_obstacle_coord_array = []
y_obstacle_coord_array = []
z_obstacle_coord_array = []
f1_problem_infeasibility = []
inner_iters = []
outer_iters = []
norm_fpr = []
f2_norm = []
for k in range(simulation_steps):
    solver_response = mng.call(x + u_prev + obstacle_coord + obstacle_vel)

    # update obstacle position
    for idx in range(3):
        obstacle_coord[idx] += sampling_time * obstacle_vel[idx]
    x_obstacle_coord_array.append(obstacle_coord[0])
    y_obstacle_coord_array.append(obstacle_coord[1])
    z_obstacle_coord_array.append(obstacle_coord[2])

    print(k)
    # --- MOVE ON ---
    if solver_response.is_ok():
        solver_status = solver_response.get()

    print(solver_status.exit_status,
          " ::", solver_status.solve_time_ms,
          " :: iters = (", solver_status.num_inner_iterations, ",", solver_status.num_outer_iterations, ")",
          " :: f2 norm = ", solver_status.f2_norm)
    #f1_problem_infeasibility.append(solver_status.f1_infeasibility)
    inner_iters.append(solver_status.num_inner_iterations)
    outer_iters.append(solver_status.num_outer_iterations)
    norm_fpr.append(solver_status.last_problem_norm_fpr)
    f2_norm.append(solver_status.f2_norm)
    us = solver_status.solution
    u = us[0:nu]
    u_prev = u
    initial_guess = us[nu:] + [0] * nu

    x_next = dynamics_dt(x, u)
    state_sequence += [x_next]
    input_sequence += [u]
    solver_time += [solver_status.solve_time_ms]
    x = x_next

mng.kill()  # bye bye server!

print("obstacle coordinates are:  ", obstacle_coord_array)

# -------------------------------------------------------------------------
# MPC performance plots
# -------------------------------------------------------------------------
time = np.arange(0, sampling_time * (simulation_steps + 1), sampling_time)

plt.rcParams["font.size"] = "12"

# plt.subplot(121)
# for i in range(len(state_sequence[0])):
#     plt.plot(time, [pt[i] for pt in state_sequence], label='id %s' % i)
# plt.grid()
# plt.ylabel('state variables')
# plt.xlabel('Time')
# plt.legend(bbox_to_anchor=(0.7, 0.85), loc='upper left', borderaxespad=0.)

# plt.subplot(122)
# plt.plot(input_sequence, '-')
# plt.xlabel('Time')
# plt.ylabel('controller actions (delta)')
# plt.grid()
# plt.show()

plt.plot(solver_time, '-')
plt.xlabel('Time')
plt.ylabel('Solver time')
plt.grid()
plt.show()

# -------------------------------------------------------------------------
# 3D plots of robot motion
# -------------------------------------------------------------------------

theta1 = [item[0] for item in state_sequence]
theta2 = [item[1] for item in state_sequence]
theta3 = [item[2] for item in state_sequence]
theta4 = [item[3] for item in state_sequence]

omega1 = [item[0] for item in input_sequence]
omega2 = [item[1] for item in input_sequence]
omega3 = [item[2] for item in input_sequence]
omega4 = [item[3] for item in input_sequence]

obstacle_coord_x = [item[0] for item in state_sequence]
obstacle_coord_y = [item[1] for item in state_sequence]
obstacle_coord_z = [item[2] for item in state_sequence]

x1_array = []
y1_array = []
z1_array = []
x2_array = []
y2_array = []
z2_array = []
x3_array = []
y3_array = []
z3_array = []
x4_array = []
y4_array = []
z4_array = []

for i in range(len(theta1)):
    print("x,y,z position: ", i)
    x1_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[0])
    y1_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[1])
    z1_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[2])
    x2_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[3])
    y2_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[4])
    z2_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[5])
    x3_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[6])
    y3_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[7])
    z3_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[8])
    x4_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[9])
    y4_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[10])
    z4_array.append(RRRR_Forward_Kinematics(theta1[i], theta2[i], theta3[i], theta4[i])[11])

fig = plt.figure()
ax = plt.gca(projection="3d")

x1_points = x1_array
y1_points = y1_array
z1_points = z1_array
x2_points = x2_array
y2_points = y2_array
z2_points = z2_array
x3_points = x3_array
y3_points = y3_array
z3_points = z3_array
x4_points = x4_array
y4_points = y4_array
z4_points = z4_array

ax.scatter3D(x4_points, y4_points, z4_points, color = "green", linestyle = 'dashed', marker = '.');
ax.scatter3D(x3_points, y3_points, z3_points, color = "yellow", linestyle = 'dashed', marker = '.');
ax.scatter3D(x2_points, y2_points, z2_points, color = "blue", linestyle = 'dashed');
ax.scatter3D(x1_points, y1_points, z1_points, color = "black", linestyle = 'dashed');
ax.scatter3D(x_obstacle_coord_array, y_obstacle_coord_array, z_obstacle_coord_array, color = "red", linestyle = 'dashed');
ax.scatter3D(xcc, ycc, zcc,  s=2000);
ax.scatter3D(0, 0, 0, color = "black")
ax.scatter3D(x_ref, y_ref, z_ref, color = "red", marker = 'X')
ax.legend(['End effector', 'xyz_4', 'xyz_3', 'xyz_2', 'xyz_1', 'xyz_orig', 'xyz_ref'])

ax.set_xlim(-.1, 1.1)
ax.set_ylim(-.2, 1.6)
ax.set_zlim(-.6, 1.1)

ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("z-axis")
ax.set_title("3D 4-link RRRR robot MPC no obstacle, point to point")
# plt.show()

# -------------------------------------------------------------------------
# Print the data to console
# -------------------------------------------------------------------------

print("open_time = ", solver_time, ";")
print("The reference X, Y, Z = ", x_ref, y_ref, z_ref)

print("omega1 = ", omega1, ";")
print("omega2 = ", omega2, ";")
print("omega3 = ", omega3, ";")
print("omega4 = ", omega4, ";")
print("theta_1 = ", theta1, ";")
print("theta_2 = ", theta2, ";")
print("theta_3 = ", theta3, ";")
print("theta_4 = ", theta4, ";")
print("x4_array = ", x4_array)
print("y4_array = ", y4_array)
print("z4_array = ", z4_array)
print("x3_array = ", x3_array)
print("y3_array = ", y3_array)
print("z3_array = ", z3_array)
print("x2_array = ", x2_array)
print("y2_array = ", y2_array)
print("z2_array = ", z2_array)
print("x1_array = ", x1_array)
print("y1_array = ", y1_array)
print("z1_array = ", z1_array)
print("obstacle_coord_x = ", x_obstacle_coord_array, ";")
print("obstacle_coord_y = ", y_obstacle_coord_array, ";")
print("obstacle_coord_z = ", z_obstacle_coord_array, ";")

print("norm_fpr = ", norm_fpr)
print("f2_norm = ", f2_norm)

print("ii = ", inner_iters, ";")
print("oi = ", outer_iters, ";")
