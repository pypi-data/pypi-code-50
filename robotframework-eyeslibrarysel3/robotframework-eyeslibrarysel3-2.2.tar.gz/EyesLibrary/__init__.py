#!/usr/bin/env python

from .keywords import SessionKeywords, CheckKeywords, TargetKeywords
from .resources import variables
from .version import __version__


class EyesLibrary(SessionKeywords, CheckKeywords, TargetKeywords):
    """
    EyesLibrary is a visual verification library for [http://robotframework.org/|Robot Framework] that leverages
    [https://applitools.com/docs/api/eyes-sdk/index-gen/classindex-selenium-python.html|Applitools Eyes Python SDK] and
    [http://robotframework.org/SeleniumLibrary/SeleniumLibrary.html|SeleniumLibrary] / 
    [http://serhatbolsu.github.io/robotframework-appiumlibrary/AppiumLibrary.html|AppiumLibrary].

    = Table of contents =
    - `Before running tests`
    - `Writing tests`
    - > `Test case example`
    - > `Open vs Check keyword arguments`
    - > `Check keywords`
    - > `Using selectors`
    - > `Defining Ignore and Floating regions`
    - > `Group tests into batches`
    - `Analysing the test results`
    - `Importing`
    - `Shortcuts`
    - `Keywords`

    = Before running tests =

    In order to run EyesLibrary, you have to create a [https://applitools.com/sign-up/|free account] with Applitools, to retrieve your API key.
    After signing up, you can get it from the [https://eyes.applitools.com/app/test-results/|Applitools Eyes Test Manager] (on user menu, click "My API Key").
        
    You may want to read [https://applitools.com/docs|Applitools documentation] in order to better understand how Eyes works.
    
    Prior to running tests, EyesLibrary must be imported into your Robot test suite.

    Example:
        | Library | EyesLibrary | 

    You may define the following arguments when importing the library (You may also define them on `Open Eyes Session`):
    - API Key (apikey)
    - Application Name (appname)
    - Test Name (testname)
    - Library - SeleniumLibrary or AppiumLibrary (library)
    - Match Level - Strict, Exact, Content or Layout (matchlevel)
    - Enable Eyes Logs (enable_eyes_log)
    - OS Name (osname)
    - Browser Name (browsername)
    - Server URL (serverurl)
    - Match Timeout (matchtimeout)     
    - Save New Tests (save_new_tests)        

    Example:
        | Library | EyesLibrary | ApiKey | AppName | TestName | SeleniumLibrary | layout | ${true} | Windows | Firefox | https://myserver.com | 5000 | ${false} |
        
    = Writing tests =

    When writing the tests, the following structure must be adopted:
    
    1. *Open Eyes Session* 

    A browser or application must be running when opening the session. 
    To open a browser/application, consult the documentation for [http://robotframework.org/SeleniumLibrary/SeleniumLibrary.html|SeleniumLibrary] 
    and/or [http://serhatbolsu.github.io/robotframework-appiumlibrary/AppiumLibrary.html|AppiumLibrary].
    
    Afterwards, the session may be opened. See `Open Eyes Session`.                                                                                                      

    2. *Visual Checks* 

    Between opening and closing the session, you can run your visual checks.
    
    See `Check Eyes Region`, `Check Eyes Region By Element`, `Check Eyes Region By Selector`, `Check Eyes Region In Frame By Selector` and `Check Eyes Window`.
    
    You can also verify if there's an open session with `Eyes Session Is Open`.
    
    3. *Close Eyes Session*

    See `Close Eyes Session`.
    	
    == Test case example ==

    Above, we consider the *structure of a test*. For each test (=session), there may be as many checkpoints as you want. Here's a test case example:

        | =Keywords=         | =Parameters=       |
        | Open Browser       | http://google.com/ | gc      |                       
        | Open Eyes Session  | YourApplitoolsKey  | AppName | TestName |
        | Check Eyes Window  | Google Homepage    |                              
        | Close Eyes Session | 

    == Open vs Check keyword arguments ==

    Some arguments may be defined either on `Open Eyes Session` or on `Check keywords`.

    When defining an argument on Open Eyes Session, it will be aplied to _all the checks of that session_.

    On the other hand, when an argument is defined on a Check keyword, it will determine the behaviour _specific to that checkpoint_, not to the other checks of the session.

    When an argument is defined both on Open and Check keywords during the same test, the latter will be used for that specific checkpoint.

    == Check keywords ==

    These are the available Check keywords:
    - `Check Eyes Window`
    - `Check Eyes Region`
    - `Check Eyes Region By Element`
    - `Check Eyes Region By Selector`
    - `Check Eyes Region In Frame By Selector`

    == Using selectors ==

    Using the keywords `Check Eyes Region By Selector`, `Check Eyes Region In Frame By Selector`, `Ignore Region By Selector`, or `Floating Region By Selector`.
    The following strategies are supported:

    | =Strategy=        | =Example=                                                                                                   | =Description=                                |
    | CSS SELECTOR      | Check Eyes Region By Selector `|` .first.expanded.dropdown `|` CssElement             `|` CSS SELECTOR      | Matches by CSS Selector                      |
    | XPATH             | Check Eyes Region By Selector `|` //div[@id='my_element']  `|` XpathElement           `|` XPATH             | Matches with arbitrary XPath expression      |
    | ID                | Check Eyes Region By Selector `|` my_element               `|` IdElement              `|` ID                | Matches by @id attribute                     |
    | CLASS NAME        | Check Eyes Region By Selector `|` element-search           `|` ClassElement           `|` CLASS NAME        | Matches by @class attribute                  |
    | LINK TEXT         | Check Eyes Region By Selector `|` My Link                  `|` LinkTextElement        `|` LINK TEXT         | Matches anchor elements by their link text   |
    | PARTIAL LINK TEXT | Check Eyes Region By Selector `|` My Li                    `|` PartialLinkTextElement `|` PARTIAL LINK TEXT | Matches anchor elements by partial link text |
    | NAME              | Check Eyes Region By Selector `|` my_element               `|` NameElement            `|` NAME              | Matches by @name attribute                   |
    | TAG NAME          | Check Eyes Region By Selector `|` div                      `|` TagNameElement         `|` TAG NAME          | Matches by HTML tag name                     |
    
    == Defining Ignore and Floating regions ==

    A *Ignore Region* defines a region to be ignored on the checks, ie, to always be considered matching.

    A *Floating Region* defines an inner region to be matched and outer bounds in which the inner region can move and still be considered matching.

    To get more details, consult [https://applitools.com/docs/api/eyes-sdk/index-gen/classindex-selenium-python.html|Eyes Selenium SDK Documentation].

    These regions may be defined using the following keywords:
    - `Ignore Region By Coordinates`
    - `Ignore Region By Element`
    - `Ignore Region By Selector`
    - `Ignore Caret`
    - `Floating Region By Coordinates`
    - `Floating Region By Element`
    - `Floating Region By Selector`

    All of these keywords return a Target object, that must be passed as an argument of the chosen Check keyword.
    
    For example, when using `Check Eyes Window` and defining `Ignore Region By Coordinates` and `Floating Region By Selector`:
 
        | {target}=         | Ignore Region By Coordinates | 20                      | 100   | 200 | 100 |
        | {target}=         | Floating Region By Selector  | //div[@id='my_element'] | xpath | 20  | 10  | 10 | 20 | {target} |
        | Check Eyes Window | Google Homepage              | target={target}         |          
    
    == Group tests into batches ==

    You can group your tests into batches, as shown in this [https://help.applitools.com/hc/en-us/articles/360006914772-Batching|article].
    
    The standard way to batch tests together is to run them together in the same execution run (See `Same Execution Run`).
    However, sometimes you may need to batch them together even if running separately (See `Tests Executed Separately`).
    
    === Same Execution Run ===

    You'll need to pass the desired batch as argument of `Open Eyes Session`.
    You can do it by passing a string with the desired batch name, or by passing a batch object, created through `Create Eyes Batch` keyword.
    
    - String with name

    Choose the desired batch name and define it on `Open Eyes Session` of the tests you want to group, through the batch argument.

    _Example_:

        | Open Eyes Session | YourApplitoolsKey | AppName | TestName | batch=BatchName |

    - Batch object

    If you want more control over the batch, you can create a BatchInfo object through `Create Eyes Batch`.
    You can define the batch name, start time, or none of them if you want the default values.

    On `Open Eyes Session` of the tests you want to group, pass this object as batch argument.
    This object may be created on: Test Suite Setup or Test Case.
    
    If this object is created on each Test Case execution, make sure it has the same name and start time, in order to identify the correct batch, given that the object instance is different.
        
    _Example_:

        | ${batch}=         | Create Eyes Batch | BatchName | 2019-01-01 10:00:00 |
        | Open Eyes Session | YourApplitoolsKey | AppName   | TestName            | batch=${batch} |

    For more information, read this [https://applitools.com/docs/topics/working-with-test-batches/how-to-group-tests-into-batches.html|document].

    === Tests Executed Separately ===

    In order to group tests into the same batch when running in different executions, the batch ID has to be the same amongst them.

    A batch object has to be created through `Create Eyes Batch`, with a given batch ID.
    Then, you must pass the batch object into `Open Eyes Session`.
    On subsequent runs, create batches with the same ID to group them together.

    It is recommended that the name is the same, however, the ID still binds them together.

    _Example_:

        | ${batch}=         | Create Eyes Batch | BatchName | batch_id=UniqueId |
        | Open Eyes Session | YourApplitoolsKey | AppName   | TestName          | batch=${batch} |

    For more information, read this [https://applitools.com/docs/topics/working-with-test-batches/batching-tests-in-a-distributed-environment.html|document].
    
    = Analysing the test results =

    In order to review and analyse the test results, you have to access the  [https://eyes.applitools.com/app/test-results/|Test Manager].

    For more information on it, read the [https://applitools.com/docs/topics/test-manager/tm-overview.html|Test Manager Documentation].
    
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(
        self,
        apikey=None,
        appname=None,
        testname=None,
        library="SeleniumLibrary",
        matchlevel=None,
        enable_eyes_log=False,
        osname=None,
        browsername=None,
        serverurl=None,
        matchtimeout=None,
        save_new_tests=True,
    ):
        """
        EyesLibrary can be imported with optional arguments. These may also be defined in `Open Eyes Session`.
        
        - ``apikey``: Applitools API key
        - ``appname``: Application name
        - ``testname``: Test name
        - ``library``: Library used to open browser/application (SeleniumLibrary or AppiumLibrary)
        - ``matchlevel``: Match level used for the comparation of screenshots
        - ``enable_eyes_log``: Activation of Applitools Eyes SDK trace logs         
        - ``osname``: Overridden OS name
        - ``browsername``: Overridden Browser name
        - ``serverurl``: The URL of the Eyes server
        - ``matchtimeout``: Time until Eyes stops retrying the matching (milliseconds)
        - ``save_new_tests``: Automatically accepting new tests
        """

        self.library_arguments = {
            "apikey": apikey,
            "appname": appname,
            "testname": testname,
            "library": library,
            "matchlevel": matchlevel,
            "enable_eyes_log": enable_eyes_log,
            "osname": osname,
            "browsername": browsername,
            "serverurl": serverurl,
            "matchtimeout": matchtimeout,
            "save_new_tests": save_new_tests,
        }

        variables.init()

