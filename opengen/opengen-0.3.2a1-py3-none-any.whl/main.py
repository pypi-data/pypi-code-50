import opengen as og
import casadi.casadi as cs

# Build parametric optimizer
# ------------------------------------

# Step 1: define variables (decision vars + parameters)
u = cs.SX.sym("u", 5)   # decision variable (length: 5)
a = cs.SX.sym("a", 1)   # parameter a
b = cs.SX.sym("b", 1)   # parameter b
p = cs.vertcat(a, b)    # p = (a, b)

# Step 2: Simple constraints
r = 1.5
set_u = og.constraints.Ball2(None, r)

# Step 3A: Define cost function
phi = 0
nu = 5
for i in range(nu-1):
    phi += b * (u[i+1] - u[i]**2)**2 \
           + (a - u[i])**2

# Step 3B: Define F2
f2 = cs.vertcat(1.5*u[0] - u[1],
                cs.fmax(0, u[2] - u[3] + 0.1))

# Step 4: Define/construct optimisation problem
problem = og.builder.Problem(u, p, phi) \
    .with_constraints(set_u) \
    .with_penalty_constraints(f2)

# Step 5: Define configurations
build_config = og.config.BuildConfiguration() \
    .with_build_mode(og.config.BuildConfiguration.DEBUG_MODE)\
    .with_build_directory("my_optimizers")\
    .with_tcp_interface_config()\
    .with_build_c_bindings()\
    .with_open_version(local_path="/home/chung/NetBeansProjects/RUST/optimization-engine")

meta = og.config.OptimizerMeta() \
    .with_authors(["Aditi Mishra", "Pantelis Sopasakis"])\
    .with_licence("GPL") \
    .with_optimizer_name("rosenbrock_optimizer")

solver_config = og.config.SolverConfiguration()\
    .with_tolerance(1e-4)\
    .with_max_duration_micros(1e3 * 50)\
    .with_delta_tolerance(1e-6)\
    .with_initial_penalty(1000)\
    .with_max_outer_iterations(12)\
    .with_penalty_weight_update_factor(1.5)

# Step 6: make builder
builder = og.builder.OpEnOptimizerBuilder(problem, meta,
                                          build_config,
                                          solver_config)
# Step 7: build!
builder.build()

# Step 8: Establish connection to solver over TCP
solver_connection_manager = og.tcp.OptimizerTcpManager("my_optimizers/rosenbrock_optimizer")
solver_connection_manager.start()

solver_response = solver_connection_manager.call(p=[5.0, 20.0])
if solver_response.is_ok():
    solution_details = solver_response.get()
    print(solution_details.solution)
    print(solution_details.solve_time_ms)
    print(solution_details.num_inner_iterations)

# Kill the solver
solver_connection_manager.kill()
