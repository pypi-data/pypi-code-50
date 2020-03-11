def init_body(spider, step: int = 1):
    spider.run_action_file("25", step=step)


def creeping(spider, step: int = 1):
    spider.run_action_file('0', step=step, msg="匍匐")


def creeping_forward(spider, step: int = 1):
    spider.run_action_file('1', step=step, msg="匍匐前进")


def creeping_backward(spider, step: int = 1):
    spider.run_action_file('2', step=step, msg="匍匐后退")


def creeping_left(spider, step: int = 1):
    spider.run_action_file('3', step=step, msg="匍匐左转")


def creeping_right(spider, step: int = 1):
    spider.run_action_file('4', step=step, msg="匍匐右转")


# -----------------------------------------------------------------

def stand(spider, step: int = 1):
    spider.run_action_file('25', step=step, msg="站立")


def forward(spider, step: int = 1):
    spider.run_action_file('26', step=step, msg="前进")


def backward(spider, step: int = 1):
    spider.run_action_file('27', step=step, msg="后退")


def left(spider, step: int = 1):
    spider.run_action_file('28', step=step, msg="左转")


def right(spider, step: int = 1):
    spider.run_action_file('29', step=step, msg="右转")


# -----------------------------------------------------------------

def towering(spider, step: int = 1):
    spider.run_action_file('34', step=step, msg="耸立")


def towering_forward(spider, step: int = 1):
    spider.run_action_file('35', step=step, msg="耸立前进")


def towering_backward(spider, step: int = 1):
    spider.run_action_file('36', step=step, msg="耸立后退")


def towering_left(spider, step: int = 1):
    spider.run_action_file('37', step=step, msg="耸立左转")


def towering_right(spider, step: int = 1):
    spider.run_action_file('38', step=step, msg="耸立右转")


# -----------------------------------------------------------------

def forward_flutter(spider, step: int = 1):
    spider.run_action_file('5', step=step, msg="前扑")


def backward_flutter(spider, step: int = 1):
    spider.run_action_file('6', step=step, msg="后扑")


def left_shift(spider, step: int = 1):
    spider.run_action_file('7', step=step, msg="左移")


def right_shift(spider, step: int = 1):
    spider.run_action_file('8', step=step, msg="右移")


def twisting(spider, step: int = 1):
    spider.run_action_file('9', step=step, msg="扭身")


def fighting(spider, step: int = 1):
    spider.run_action_file('10', step=step, msg="战斗")


def break_forward(spider, step: int = 1):
    spider.run_action_file('41', step=step, msg="碎步前进")


def minor_steering(spider, step: int = 1):
    spider.run_action_file('40', step=step, msg="小转向(右)")
