from commander import Commander

# The function to execute
def foo(bar, baz):
    return str(bar) + str(baz)

# Function to generate list of arguments to try
def foo_args(bar_range, baz_range):
    for bar in bar_range:
        for baz in baz_range:
            yield { 'bar': bar, 'baz': baz }

if __name__ == '__main__':
    # Create a commander (doesn't connect yet)
    cmdr = Commander([
        # Lieutenants can be hostnames, domains, IPs
        ('localhost', 3333)
    ])

    # Connect to lieutenants, run all the functions, and get results
    results = cmdr.run(foo, list(foo_args(range(10), range(10))), ['test.py'])
    print(results)