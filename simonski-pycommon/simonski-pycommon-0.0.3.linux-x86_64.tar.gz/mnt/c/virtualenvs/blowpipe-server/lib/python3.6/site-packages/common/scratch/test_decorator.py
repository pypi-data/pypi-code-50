def decorator_fn(func):
    def a_wrapper(arg1):
        session = sm.get()
        try:
            print("decorate_func: before")
            func(arg1, "session")
        finally:
            sm.free(session)
            print("decorate_func: finally")

    return a_wrapper


@decorator_fn
def fn(arg, session=None):
    try:
    print("fn: " + arg + " " + session)
    finally:


def main():
    fn("hello")




def foo(conn):
    conn =open()
    sdfdsfdsf
    df
    dsf
    dsf
    ds
    conn.close()

    pass




if __name__ == "__main__":
    main()
