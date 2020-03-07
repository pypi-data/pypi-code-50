# -*- coding: utf-8 -*-

import nwae.utils.Log as lg
from inspect import getframeinfo, currentframe
import mex.MatchExpression as mexpr
import  nwae.utils.UnitTest as ut
import nwae.utils.Profiling as prf


class UnitTestMex:

    TESTS = [
        {
            # Trailing '/' in '...вес / 重 /' should be removed automatically
            'mex': 'm, float, mass / 무게 / вес / 重 / ;  d, datetime, ',
            'lang': None,
            'sentences': [
                ('My mass is 68.5kg on 2019-09-08', {'m': 68.5, 'd': '2019-09-08'}),
                # float type should also work if entered integer
                ('My mass is 68kg on 2019-09-08', {'m': 68.0, 'd': '2019-09-08'}),
            ]
        },
        {
            # Trailing '/' in '...вес / 重 /' should be removed automatically
            'mex': 'm, float, dollar / dollars / $ / ^  ;   y, int, year / yr / - / ',
            'lang': None,
            'sentences': [
                # Common dollar sign '$' should be correctly bracketed in our regex
                ('My salary in year 2019 is $8888.99.', {'m': 8888.99, 'y': 2019}),
                # Common dollar sign '$' should be correctly bracketed in our regex
                ('My salary in year 2019 is $8888.99 man...', {'m': 8888.99, 'y': 2019}),
                # Another special character '^' should be correctly bracketed in our regex
                ('My salary in year 2019 is ^ 8888.99 man...', {'m': 8888.99, 'y': 2019}),
                # Another special character '-' should be correctly work also
                ('My salary in - 2019 is $ 8888.99 man...', {'m': 8888.99, 'y': 2019})
            ]
        },
        {
            # We also use the words 'test&escape' and ';' (clashes with var separator
            # but works because we escape the word using '\\;')
            # to detect diameter.
            # Need to escape special mex characters like ; if used as expression
            'mex': 'r, float, radius & r  ;'
                   + 'd, float, diameter / d / test\\/escape / \\; / + / * /\\/ / \\&   ;   ',
            'lang': 'en',
            # Sentence & Expected Result
            'sentences': [
                ('What is the volume of a sphere of radius 5.88?', {'r': 5.88, 'd': None}),
                # Ending '.' should not affect result
                ('What is the volume of a sphere of radius 5.88.', {'r': 5.88, 'd': None}),
                ('What is the volume of a sphere of radius 5.88 and 4.9 diameter?', {'r': 5.88, 'd': 4.9}),
                ('What is the volume of a sphere of radius 5.88 and 33.88 test&escape?', {'r': 5.88, 'd': 33.88}),
                ('What is the volume of a sphere of radius 5.88, 33.88;?', {'r': 5.88, 'd': 33.88}),
                # When stupid user uses '+' to detect a param, should also work, but not recommended
                ('What is the volume of a sphere of radius 5.88, +33.88?', {'r': 5.88, 'd': 33.88}),
                # Using '*' to detect diameter
                ('What is the volume of a sphere of radius 5.88, 33.88*?', {'r': 5.88, 'd': 33.88}),
                # Using '/' to detect diameter
                ('What is the volume of a sphere of radius 5.88, 33.88/?', {'r': 5.88, 'd': 33.88}),
                # Should not detect diameter because we say to look for 'd', not any word ending 'd'
                # But because we have to handle languages like Chinese/Thai where there is no word
                # separator, we allow this and the diameter will be detected
                ('What is the volume of a sphere of radius 5.88 and 33.88?', {'r': 5.88, 'd': 33.88}),
                # Should not be able to detect now diameter, return d=5.88 due to left priority
                ('What is the volume of a sphere of radius 5.88 / 33.88?', {'r': 5.88, 'd': 5.88}),
                # Test the unusual keyword 'test/escape'
                ('What is the volume of a sphere of radius 5.88, test/escape 33.88?', {'r': 5.88, 'd': 33.88}),
                # Test the unusual keyword '&'
                ('What is the volume of a sphere of radius 5.88, & 33.88?', {'r': 5.88, 'd': 33.88})
            ]
        },
        {
            'mex': 'dt,datetime,   ;   email,email,   ;   inc, float, inc / inch / inches',
            'lang': 'en',
            'sentences': [
                ('What is -2.6 inches? 20190322 05:15 send to me@abc.com.',
                 {'dt': '20190322 05:15', 'email': 'me@abc.com', 'inc': -2.6}),
                ('What is +1.2 inches? 2019-03-22 05:15 you@email.ua ?',
                 {'dt': '2019-03-22 05:15', 'email': 'you@email.ua', 'inc': 1.2}),
                ('2019-03-22: u_ser-name.me@gmail.com is my email',
                 {'dt': '2019-03-22', 'email': 'u_ser-name.me@gmail.com', 'inc': None}),
                ('이멜은u_ser-name.me@gmail.com',
                 {'dt': None, 'email': 'u_ser-name.me@gmail.com', 'inc': None} ),
                ('u_ser-name.me@gmail.invalid is my email',
                 {'dt': None, 'email': 'u_ser-name.me@gmail.invalid', 'inc': None}),
                ('ok. 888_very.geng.mahk_mahk.123@gmail.invalid is my email',
                 {'dt': None, 'email': '888_very.geng.mahk_mahk.123@gmail.invalid', 'inc': None}),
            ]
        },
        {
            'mex': 'dt, datetime,   ;   acc, number, 계정 / 번호   ;   '
                   + 'm, int, 월   ;   d, int, 일   ;   t, time, 에   ;'
                   + 'am, float, 원   ;   bl, float, 잔액   ;'
                   + 'name, str-zh-cn, 】 ',
            'lang': 'ko',
            'sentences': [
                ('2020-01-01: 번호 0011 계정은 9 월 23 일 10:12 에 1305.67 원, 잔액 9999.77.',
                 {'dt': '2020-01-01', 'acc': '0011', 'm': 9, 'd': 23, 't': '10:12', 'am': 1305.67, 'bl': 9999.77, 'name': None}),
                ('20200101 xxx: 번호 0011 계정은 8 월 24 일 10:12 에 원 1305.67, 9999.77 잔액.',
                 {'dt': '20200101', 'acc': '0011', 'm': 8, 'd': 24, 't': '10:12', 'am': 1305.67, 'bl': 9999.77, 'name': None}),
                ('AAA 2020-01-01 11:52:22: 번호 0022 계정은 7 월 25 일 10:15:55 에 1405.78 원, 잔액 8888.77.',
                 {'dt': '2020-01-01 11:52:22', 'acc': '0022', 'm': 7, 'd': 25, 't': '10:15:55', 'am': 1405.78, 'bl': 8888.77, 'name': None}),
                ('2020-01-01: 번호 0033 계정은 6 월 26 일 完成23:24 에 1505.89 원, 잔액 7777.77.',
                 {'dt': '2020-01-01', 'acc': '0033', 'm': 6, 'd': 26, 't': '23:24', 'am': 1505.89, 'bl': 7777.77, 'name': None}),
                ('2020-01-01: 번호 0044 계정은 5 월 27 일 完成23:24:55 에 5501.99 원, 잔액 6666.77.',
                 {'dt': '2020-01-01', 'acc': '0044', 'm': 5, 'd': 27, 't': '23:24:55', 'am': 5501.99, 'bl': 6666.77, 'name': None}),
                ('2020-01-01: 번호0055계정은4월28일11:37에1111.22원，잔액5555.77.',
                 {'dt': '2020-01-01', 'acc': '0055', 'm': 4, 'd': 28, 't': '11:37', 'am': 1111.22, 'bl': 5555.77, 'name': None}),
                ('2020-01-01: 번호0066계정은3월29일11:37:55에2222.33원，잔액4444.77',
                 {'dt': '2020-01-01', 'acc': '0066', 'm': 3, 'd': 29, 't': '11:37:55', 'am': 2222.33, 'bl': 4444.77, 'name': None}),
                ('2020-01-01: 번호0777계정은30일 11:38:55에3333.44원',
                 {'dt': '2020-01-01', 'acc': '0777', 'm': None, 'd': 30, 't': '11:38:55', 'am': 3333.44, 'bl': None, 'name': None}),
                ('【은행】 陈豪贤于.',
                 {'dt': None, 'acc': None, 'm': None, 'd': None, 't': None, 'am': None, 'bl': None, 'name': '陈豪贤于'}),
                ('xxx 陈豪贤 】 于.',
                 {'dt': None, 'acc': None, 'm': None, 'd': None, 't': None, 'am': None, 'bl': None, 'name': '陈豪贤'}),
                ('陈豪贤 】 于.',
                 {'dt': None, 'acc': None, 'm': None, 'd': None, 't': None, 'am': None, 'bl': None, 'name': '陈豪贤'}),
            ]
        },
        {
            'mex': 'acc, account_number, 번호',
            'lang': 'ko',
            'sentences': [
                # Normal number should work for account_number
                ('2020-01-01: 번호 001122 계정은 9 월 23 일 10:12 에 1305.67 원, 잔액 9999.77.',
                 {'acc': '001122'}),
                # Standard test of some '-' characters
                ('2020-01-01: 번호 11-22-33 계정은 9 월 23 일 10:12 에 1305.67 원, 잔액 9999.77.',
                 {'acc': '11-22-33'}),
                # Trailing '-' should be removed by end user, to simplify our regex
                ('2020-01-01: 번호 22-33-44- 계정은 9 월 23 일 10:12 에 1305.67 원, 잔액 9999.77.',
                 {'acc': '22-33-44-'}),
                ('2020-01-01: 번호 33-44-55 계정은 9 월 23 일 10:12 에 1305.67 원, 잔액 9999.77.',
                 {'acc': '33-44-55'}),
                # Account number cannot start with '-'
                ('2020-01-01: 번호 -333-444-555 계정은 9 월 23 일 10:12 에 1305.67 원, 잔액 9999.77.',
                 {'acc': None}),
                # Should capture account number, not the float number
                ('2020-01-01: 44-55-66 번호 1305.67 원, 잔액 9999.77.',
                 {'acc': '44-55-66'}),
                # Should capture account number, trailing '-' is user problem
                ('2020-01-01: 55-66-77- 번호 1305.67 원, 잔액 9999.77.',
                 {'acc': '55-66-77-'}),
            ]
        },
        {
            # Longer names come first
            # If we had put instead "이름 / 이름은", instead of detecting "김미소", it would return "은" instead
            # But because we do internal sorting already, this won't happen
            'mex': 'kotext, str-ko, 이름 / 이름은 , 3  ;'
                   + 'thtext, str-th, ชื่อ   ;'
                   + 'vitext, str-vi, tên   ;'
                   + 'cntext, str-zh-cn, 名字 / 名 / 叫 / 我叫 , 2-3, right',
            'lang': None,
            'sentences': [
                ('이름은 김미소 ชื่อ กุ้ง tên yêu ... 我叫是习近平。',
                 {'kotext': '김미소', 'thtext': 'กุ้ง', 'vitext': 'yêu', 'cntext': '习近平'} ),
                # '习近平近平' should be truncated to '习近平', '김미소미소' should be truncated to '김미소'
                ('이름은 김미소미소 ชื่อ กุ้งกุ้ง tên yêu yêu ... 我叫是习近平近平。',
                 {'kotext': '김미소', 'thtext': 'กุ้งกุ้ง', 'vitext': 'yêu', 'cntext': '习近平'})
            ],
            'priority_direction': [
                'right'
            ]
        },
        {
            'mex': 'url, uri,   ;   x, float, x',
            'lang': None,
            'sentences': [
                ('이름은 김미소 https://www.geeksforgeeks.org/python-check-url-string/ ok。 x = 1.1?',
                 {'x': 1.1, 'url': 'https://www.geeksforgeeks.org/python-check-url-string/'}),
                ('이름은 김미소미소 ชื่อ กุ้งกุ้ง https://docs.google.com/document/d/1_fox_6_o/edit... 我叫是习近平近平。 x=2.2 !',
                 {'x': 2.2, 'url': 'https://docs.google.com/document/d/1_fox_6_o/edit'}),
                # Capital in URL will be lower cased. TODO Should be have option to return without to lower?
                # Also x should be 3.3 but there is a 'x1' string inside the url,
                # which will cause left priority to be returned as 3.3 and not 1.0
                ('이름은 김미소미소 ชื่อ กุ้งกุ้ง http://docs.google.com/document/d/x1jmtu0PPLV8f9qkm_6_o/edit... 我叫是习近平近平。 x=3.3;;',
                 {'x': 3.3, 'url': 'http://docs.google.com/document/d/x1jmtu0pplv8f9qkm_6_o/edit'}),
                ('이름은 김미소미소 ชื่อ กุ้งกุ้ง file://docs.google.com/file/?param=iii_%20%60... 我叫是习近平近平。x=4.4.',
                 {'x': 4.4, 'url': 'file://docs.google.com/file/?param=iii_%20%60'}),
            ]
        },
        {
            # TODO This is super slow up to 5s WHY???
            'mex': 'x, uri, url / uri / ==   ;   v, float, time / speed',
            'lang': 'en',
            'sentences': [
                # TODO This is super slow up to 5s WHY???
                #('speed 5.3s == https://staging-bot.com/all/?accid=4&txt=%E4%BB%80%E4%B9%88%20is%205kg%20in%20pounds? -',
                # {'x': 'https://staging-bot.com/all/?accid=4&txt=%e4%bb%80%e4%b9%88%20is%205kg%20in%20pounds?', 'v': 5.3})
            ]
        },
        {
            'mex': 'u, username, 用户名   ;   d, datetime, ',
            'lang': 'en',
            'sentences': [
                ('用户名nwae_c0d3_xx*. 2019-01-01',
                 {'u': 'nwae_c0d3_xx', 'd': '2019-01-01'}),
                # Should ignore all disallowed punctuations behind a username
                ('用户名=nwae_c0d3_xx$?*. 2019-01-01',
                 {'u': 'nwae_c0d3_xx', 'd': '2019-01-01'}),
                # Should ignore all disallowed punctuations behind a username
                ('用户名 nwae_c0d3_xx___!$?*. 2019-01-01',
                 {'u': 'nwae_c0d3_xx___', 'd': '2019-01-01'}),
                # Username not allowed to start with '_'
                ('用户名 _nwae_c0d3_xx___!$?*. 2019-01-01',
                 {'u': None, 'd': '2019-01-01'}),
                # Should ignore full stop
                ('wo nwae_c0d3_xx___888. 用户名 2019-01-01',
                 {'u': 'nwae_c0d3_xx___888', 'd': '2019-01-01'}),
                # Should ignore brackets
                ('나는[nwae_c0d3_xx___888] 用户名 2019-01-01',
                 {'u': 'nwae_c0d3_xx___888', 'd': '2019-01-01'}),
                # Should ignore quotes
                ('나는 "nwae_c0d3_xx___888"!?   用户名    2019-01-01',
                 {'u': 'nwae_c0d3_xx___888', 'd': '2019-01-01'}),
                # Simple username
                ('나는 "nwae"!?   用户名    2019-01-01',
                 {'u': 'nwae', 'd': '2019-01-01'}),
                ('用户名 my_username。',
                 {'u': 'my_username', 'd': None}),
                # Not a username with '.' in front
                ('用户名 .my_username。',
                 {'u': None, 'd': None}),
                ('用户名 my_user-name。',
                 {'u': 'my_user-name', 'd': None}),
                ('用户名 my_user.name-ok。',
                 {'u': 'my_user.name-ok', 'd': None}),
                ('用户名 my_user.name-ok-1-2-3.o_k。',
                 {'u': 'my_user.name-ok-1-2-3.o_k', 'd': None}),
                # Chinese dot should not be included
                ('用户名geng.mahk_mahk123。',
                 {'u': 'geng.mahk_mahk123', 'd': None}),
                # 2 dots
                ('用户名geng.mahk_mahk.123。',
                 {'u': 'geng.mahk_mahk.123', 'd': None}),
                # 888_very.geng.mahk_mahk.123
                ('用户名 888_very.geng.mahk_mahk.123。',
                 {'u': '888_very.geng.mahk_mahk.123', 'd': None}),
                ('用户名 li88jin_99.000__f8。',
                 {'u': 'li88jin_99.000__f8', 'd': None}),
            ]
        },
        {
            'mex': 'u, username_nonword, 用户名   ;   d, datetime, ',
            'lang': 'en',
            'sentences': [
                # Not a username_nonword
                ('나는 "nwae"!?   用户名..    2019-01-01',
                 {'u': None, 'd': '2019-01-01'}),
                # Not a username_nonword
                ('나는 notusername.',
                 {'u': None, 'd': None}),
                ('用户名nwae_c0d3_xx*. 2019-01-01',
                 {'u': 'nwae_c0d3_xx', 'd': '2019-01-01'}),
                # Should ignore all disallowed punctuations behind a username
                ('用户名=nwae_c0d3_xx$?*. 2019-01-01',
                 {'u': 'nwae_c0d3_xx', 'd': '2019-01-01'}),
                # Should ignore all disallowed punctuations behind a username
                ('用户名 nwae_c0d3_xx___!$?*. 2019-01-01',
                 {'u': 'nwae_c0d3_xx___', 'd': '2019-01-01'}),
                # Username not allowed to start with '_'
                ('用户名 _nwae_c0d3_xx___!$?*. 2019-01-01',
                 {'u': None, 'd': '2019-01-01'}),
                # Should ignore full stop
                ('wo nwae_c0d3_xx___888. 用户名 2019-01-01',
                 {'u': 'nwae_c0d3_xx___888', 'd': '2019-01-01'}),
                # Should ignore brackets
                ('나는[nwae_c0d3_xx___888] 用户名 2019-01-01',
                 {'u': 'nwae_c0d3_xx___888', 'd': '2019-01-01'}),
                # Should ignore quotes
                ('나는 "nwae_c0d3_xx___888"!?   用户名    2019-01-01',
                 {'u': 'nwae_c0d3_xx___888', 'd': '2019-01-01'}),
                ('用户名 my_username。',
                 {'u': 'my_username', 'd': None}),
                # Not a username with '.' in front
                ('用户名 .my_username。',
                 {'u': None, 'd': None}),
                ('用户名 my_user-name。',
                 {'u': 'my_user-name', 'd': None}),
                ('用户名 my_user.name-ok。',
                 {'u': 'my_user.name-ok', 'd': None}),
                ('用户名 my_user.name-ok-1-2-3.o_k。',
                 {'u': 'my_user.name-ok-1-2-3.o_k', 'd': None}),
                # Chinese dot should not be included
                ('用户名geng.mahk_mahk123。',
                 {'u': 'geng.mahk_mahk123', 'd': None}),
                # 2 dots
                ('用户名geng.mahk_mahk.123。',
                 {'u': 'geng.mahk_mahk.123', 'd': None}),
                # 888_very.geng.mahk_mahk.123
                ('用户名 888_very.geng.mahk_mahk.123。',
                 {'u': '888_very.geng.mahk_mahk.123', 'd': None}),
                ('用户名 li88jin_99.000__f8。',
                 {'u': 'li88jin_99.000__f8', 'd': None}),
            ]
        },
    ]

    def __init__(self, config):
        return

    def run_unit_test(
            self
    ):
        res_final = ut.ResultObj(count_ok=0, count_fail=0)
        total_time = 0

        for test in UnitTestMex.TESTS:
            pattern = test['mex']
            lang = test['lang']
            sentences = test['sentences']
            return_value_priorities = [mexpr.MatchExpression.TERM_LEFT] * len(sentences)
            if 'priority_direction' in test.keys():
                return_value_priority = test['priority_direction']

            for i in range(len(sentences)):
                sent = sentences[i][0]
                expected_result = None
                if len(sentences[i]) > 1:
                    expected_result = sentences[i][1]

                a = prf.Profiling.start()
                cmobj = mexpr.MatchExpression(
                    pattern=pattern,
                    lang=lang
                )
                # a = prf.Profiling.start()
                params = cmobj.get_params(
                    sentence=sent,
                    return_one_value=True
                )
                res_final.update_bool(res_bool=ut.UnitTest.assert_true(
                    observed = params,
                    expected = expected_result,
                    test_comment = 'test "' + str(sent) + '"'
                ))
                interval_secs = prf.Profiling.get_time_dif(start=a, stop=prf.Profiling.stop(), decimals=5)
                total_time += interval_secs
                lg.Log.info('Took ' + str(interval_secs))

        lg.Log.important('*** TEST PASS ' + str(res_final.count_ok) + ', FAIL ' + str(res_final.count_fail) + ' ***')
        rps = round((res_final.count_ok+res_final.count_fail)/total_time, 2)
        time_per_request = round(1000/rps, 2)
        lg.Log.important('Result: ' + str(rps) + ' rps (requests per second), or ' + str(time_per_request) + 'ms per request')

        return res_final


if __name__ == '__main__':
    lg.Log.DEBUG_PRINT_ALL_TO_SCREEN = True
    lg.Log.LOGLEVEL = lg.Log.LOG_LEVEL_IMPORTANT
    UnitTestMex(config=None).run_unit_test()
    exit (0)

    lg.Log.LOGLEVEL = lg.Log.LOG_LEVEL_DEBUG_2
    print(mexpr.MatchExpression(
        lang = 'en',
        # pattern = 'm, float, ma-ss / 무게 / вес / 重 / ;  d, datetime, '
        # pattern = 'x, uri, url / uri / ==   ;   v, float, time / speed',
        pattern = 'url, uri,   ;   x, float, x',
        do_profiling = True
    ).get_params(
        # sentence = 'My ma-ss is 68.5kg on 2019-09-08',
        # This is super slow up to 5s WHY??? re.match() will take very long because of our sentence.
        # sentence = 'speed 5.3s == https://staging-bot.com/all/?accid=4&txt=%E4%BB%80%E4%B9%88%20is%205kg%20in%20pounds? -',
        sentence = '이름은 김미소 https://www.geeksforgeeks.org/python-check-url-string/ ok。 x = 1.1?',
        return_one_value = True
    ))

