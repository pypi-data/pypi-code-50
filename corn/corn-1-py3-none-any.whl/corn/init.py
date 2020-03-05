def __init__(hub):
    # Remember not to start your app in the __init__ function
    # This function should just be used to set up the plugin subsystem
    # Add another function to call from your run.py to start the app
    pass


def cli(hub):
    hub.pop.conf.integrate(["corn"], cli="corn", roots=True, loader="yaml")
    print("corn works!")
