# main.py
# deploy this for everyone and other apps!
import traceback

import fifteenrock

tb = None
app_tb = None
all_error_trace = []
try:
    import fifteenrock_project_main
except ImportError:
    pass
except Exception as e:
    print(e)
    tb = traceback.format_exc()
    all_error_trace.append('Global Error:')
    all_error_trace.append(tb)
    traceback.print_exc()
    pass

try:
    from . import fifteenrock_project_main
except ImportError:
    pass
except Exception as e:
    print(e)
    tb = traceback.format_exc()
    all_error_trace.append('Global Error:')
    all_error_trace.append(tb)
    traceback.print_exc()
    pass


def main(context, event):
    try:
        result = fifteenrock_project_main.main(event)
    except Exception as e:
        app_tb = traceback.format_exc()
        context.logger.info(app_tb)
        print(app_tb)
        all_error_trace.append('Application Error:')
        all_error_trace.append(app_tb)
        result = '\n'.join(all_error_trace)
        pass

    return context.Response(body=result,
                            headers={},
                            content_type='text/json',
                            status_code=200)
