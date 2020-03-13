import time
import functools
import traceback


class MaxRetryExceeds(Exception):
    def __repr__(self):
        return "MaxRetryExceedsException"


class StopRetry(Exception):
    def __repr__(self):
        return "StopRetryException"


def exception_wrapper(*pargs):
    def wrapper(f):
        if pargs:
            (handler, li) = pargs
            t = [(ex, handler)
                 for ex in li]
            t.reverse()
        else:
            t = [(Exception, None)]

        def newfunc(t, *args, **kwargs):
            ex, handler = t[0]

            try:
                if len(t) == 1:
                    f(*args, **kwargs)
                else:
                    newfunc(t[1:], *args, **kwargs)
            except Exception as e:
                if handler:
                    handler(e)
                else:
                    print(e.__class__.__name__, ':', e)

        return functools.partial(newfunc, t)

    return wrapper


def retry_wrapper(n, verbose=False):
    def _retry_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            max_try = n
            while max_try:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    max_try -= 1
                    if max_try <= 0:
                        raise MaxRetryExceeds
                    if verbose:
                        traceback.print_exc()
                    print(e)

        return wrapper

    return _retry_wrapper


def retry_exception_wrapper(f=None, max_retries: int = 5, delay: (int, float) = 1, step: (int, float) = 0,
                            exceptions: (BaseException, tuple, list) = BaseException, sleep=time.sleep,
                            process=None, validate=None, callback=None, default=None):
    """
    函数执行出现异常时自动重试的简单装饰器
    :param f: function 执行的函数。
    :param max_retries: int 最多重试次数。
    :param delay: int/float 每次重试的延迟，单位秒。
    :param step: int/float 每次重试后延迟递增，单位秒。
    :param exceptions: BaseException/tuple/list 触发重试的异常类型，单个异常直接传入异常类型，多个异常以tuple或list传入。
    :param sleep: 实现延迟的方法，默认为time.sleep。
    在一些异步框架，如tornado中，使用time.sleep会导致阻塞，可以传入自定义的方法来实现延迟。
    自定义方法函数签名应与time.sleep相同，接收一个参数，为延迟执行的时间。
    :param process: 处理函数，函数签名应接收一个参数，每次出现异常时，会将异常对象传入。
    可用于记录异常日志，中断重试等。
    如处理函数正常执行，并返回True，则表示告知重试装饰器异常已经处理，重试装饰器终止重试，并且不会抛出任何异常。
    如处理函数正常执行，没有返回值或返回除True以外的结果，则继续重试。
    如处理函数抛出异常，则终止重试，并将处理函数的异常抛出。
    :param validate: 验证函数，用于验证执行结果，并确认是否继续重试。
    函数签名应接收一个参数，每次被装饰的函数完成且未抛出任何异常时，调用验证函数，将执行的结果传入。
    如验证函数正常执行，且返回False，则继续重试，即使被装饰的函数完成且未抛出任何异常。
    如验证函数正常执行，没有返回值或返回除False以外的结果，则终止重试，并将函数执行结果返回。
    如验证函数抛出异常，且异常属于被重试装饰器捕获的类型，则继续重试。
    如验证函数抛出异常，且异常不属于被重试装饰器捕获的类型，则将验证函数的异常抛出。
    :param callback: 回调函数，函数签名应接收一个参数，异常无法处理时，会将异常对象传入。
    可用于记录异常日志，发送异常日志等。
    :param default: 默认值/默认值生成函数
    :return: 被装饰函数的执行结果。
    """

    # 带参数的装饰器
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # nonlocal delay, step, max_retries
            i = 0
            func_exc, exc_traceback = StopRetry, None
            while i < max_retries:
                try:
                    result = func(*args, **kwargs)
                    # 验证函数返回False时，表示告知装饰器验证不通过，继续重试
                    if callable(validate) and validate(result) is False:
                        continue
                    else:
                        return result
                except exceptions as ex:
                    func_exc, exc_traceback = ex, traceback.format_exc()
                    # 处理函数返回True时，表示告知装饰器异常已经处理，终止重试
                    if callable(process):
                        try:
                            if process(ex) is True:
                                return default() if callable(default) else default
                        except Exception as e:
                            func_exc, exc_traceback = e, traceback.format_exc()
                            break
                finally:
                    i += 1
                    sleep(delay + step * i)
            else:
                # 回调函数，处理自动无法处理的异常
                if callable(callback):
                    callback(func_exc, exc_traceback)
                return default() if callable(default) else default
            pass

        return wrapper

    if callable(f):
        return decorator(f)
    return decorator


if __name__ == "__main__":
    def myhandler(e):
        print('Caught exception!', e)


    @exception_wrapper(None, (AttributeError, ValueError))
    @exception_wrapper(myhandler, (ZeroDivisionError,))
    def f1():
        print(1 / 0)


    @exception_wrapper()
    def f3(*pargs):
        l = pargs
        return l.index(10)


    f1()
    f3()
