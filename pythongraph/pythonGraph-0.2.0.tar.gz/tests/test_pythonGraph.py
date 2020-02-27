import mock
import pygame

import pythonGraph


def _get_window_title():
    title, icontitle = pygame.display.get_caption()
    return title


def setup_function(function):
    set_mode = pygame.display.set_mode

    def mock_set_mode(size):
        # enable transparency (https://stackoverflow.com/questions/14948711/)
        return set_mode(size, flags=0, depth=32)

    with mock.patch('pygame.mixer.init') as mock_mixer_init, \
            mock.patch('pygame.display.set_mode',
                       wraps=mock_set_mode) as mock_display_set_mode:
        pythonGraph.open_window(400, 300)

        mock_mixer_init.assert_called_once_with()
        mock_display_set_mode.assert_called_once()


def teardown_function(function):
    pythonGraph.close_window()


def test_open_window():
    assert pygame.display.get_surface() is not None
    assert 'pythonGraph' == _get_window_title()


def test_set_window_title():
    pythonGraph.set_window_title('fake-title')
    assert 'fake-title' == _get_window_title()


def test_close_window():
    assert pygame.display.get_surface() is not None

    pythonGraph.close_window()
    assert pygame.display.get_surface() is None


def test_window_closed():
    assert not pythonGraph.window_closed()

    pythonGraph.close_window()
    assert pythonGraph.window_closed()


def test_window_not_closed():
    assert pythonGraph.window_not_closed()

    pythonGraph.close_window()
    assert not pythonGraph.window_not_closed()


@mock.patch('random.randint')
def test_create_random_color(mock_random):
    pythonGraph.create_random_color()
    mock_random.assert_has_calls([
        mock.call(0, 255),
        mock.call(0, 255),
        mock.call(0, 255),
    ])


def test__get_rectangle():
    rectangle = pythonGraph.pythonGraph._get_rectangle(100, 100, 200, 200)
    assert rectangle.topleft == (100, 100)
    assert rectangle.topright == (201, 100)
    assert rectangle.bottomleft == (100, 201)
    assert rectangle.bottomright == (201, 201)

    rectangle = pythonGraph.pythonGraph._get_rectangle(200, 200, 100, 100)
    assert rectangle.topleft == (100, 100)
    assert rectangle.topright == (201, 100)
    assert rectangle.bottomleft == (100, 201)
    assert rectangle.bottomright == (201, 201)


def test_draw_arc():
    pythonGraph.draw_arc(100, 100, 199, 199,
                         150, 199, 199, 150,
                         pythonGraph.colors.RED)

    radius = int(round(50 / 2**0.5))
    assert pythonGraph.colors.RED == pythonGraph.get_color(150, 199)
    assert pythonGraph.colors.RED == pythonGraph.get_color(199, 150 + 1)
    assert pythonGraph.colors.RED == pythonGraph.get_color(150 + radius - 1,
                                                           150 + radius)

    assert pythonGraph.colors.WHITE == pythonGraph.get_color(150 - radius - 1,
                                                             150 + radius)
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(150 + radius - 1,
                                                             150 - radius)
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(150 - radius - 1,
                                                             150 - radius)

    pythonGraph.draw_arc(100, 100, 199, 199,
                         150, 199, 150, 100,
                         pythonGraph.colors.RED)

    radius = int(round(50 / 2**0.5))
    assert pythonGraph.colors.RED == pythonGraph.get_color(150, 199)
    assert pythonGraph.colors.RED == pythonGraph.get_color(150 + 2, 100)
    assert pythonGraph.colors.RED == pythonGraph.get_color(199, 150)
    assert pythonGraph.colors.RED == pythonGraph.get_color(150 + radius - 1,
                                                           150 + radius)
    assert pythonGraph.colors.RED == pythonGraph.get_color(150 + radius - 1,
                                                           150 - radius)

    assert pythonGraph.colors.WHITE == pythonGraph.get_color(150 - radius - 1,
                                                             150 + radius)
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(150 - radius - 1,
                                                             150 - radius)


def _test_draw_circle(filled):
    pythonGraph.draw_circle(200, 150, 50, pythonGraph.colors.RED, filled)

    # NOTE: The following coordinates are wonky -- not the same as an ellipse
    # that is centered inside the same bounding box. Not sure exactly what's
    # going on here...possibly an off-by-one error in how the coordinates are
    # interpreted for the shapes.
    for x in [151, 249]:
        assert pythonGraph.colors.RED == pythonGraph.get_color(x, 150)
    for y in [101, 199]:
        assert pythonGraph.colors.RED == pythonGraph.get_color(200, y)

    # point outside the circle
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(255, 155)


def test_draw_cirlce_filled():
    _test_draw_circle(True)

    # point inside the circle
    assert pythonGraph.colors.RED == pythonGraph.get_color(200, 150)


def test_draw_cirlce_not_filled():
    _test_draw_circle(False)

    # point inside the circle
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(200, 150)


def _test_draw_ellipse(filled):
    pythonGraph.draw_ellipse(150, 100, 250, 200, pythonGraph.colors.RED,
                             filled)

    # NOTE: The following coordinates are wonky -- not the same as a circle
    # that is centered inside the same bounding box. Not sure exactly what's
    # going on here...possibly an off-by-one error in how the coordinates are
    # interpreted for the shapes.
    for x in [150, 250]:
        assert pythonGraph.colors.RED == pythonGraph.get_color(x, 150)
    for y in [100, 200]:
        assert pythonGraph.colors.RED == pythonGraph.get_color(200, y)

    # point outside the ellipse
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(255, 155)


def test_draw_ellipse_filled():
    _test_draw_ellipse(True)

    # point inside the ellipse
    assert pythonGraph.colors.RED == pythonGraph.get_color(200, 150)


def test_draw_ellipse_not_filled():
    _test_draw_ellipse(False)

    # point inside the ellipse
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(200, 150)


def test_draw_image():
    pythonGraph.draw_image('pythonGraph/examples/media/test.png',
                           0, 0, 300, 300)

    assert pythonGraph.colors.WHITE == pythonGraph.get_color(1, 1)
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(100, 100)
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(200, 200)

    assert pythonGraph.create_color(215, 11, 11) == \
        pythonGraph.get_color(35, 35)
    assert pythonGraph.create_color(51, 11, 215) == \
        pythonGraph.get_color(60, 60)
    assert pythonGraph.create_color(255, 242, 20) == \
        pythonGraph.get_color(170, 125)
    assert pythonGraph.create_color(52, 157, 20) == \
        pythonGraph.get_color(110, 200)


def test_draw_image_transparent():
    pythonGraph.clear_window(pythonGraph.colors.BLACK)
    pythonGraph.draw_image('pythonGraph/examples/media/test.png',
                           0, 0, 300, 300)

    assert pythonGraph.colors.BLACK == pythonGraph.get_color(1, 1)
    assert pythonGraph.colors.BLACK == pythonGraph.get_color(100, 100)
    assert pythonGraph.colors.BLACK == pythonGraph.get_color(200, 200)

    assert pythonGraph.create_color(215, 11, 11) == \
        pythonGraph.get_color(35, 35)
    assert pythonGraph.create_color(52, 157, 20) == \
        pythonGraph.get_color(110, 200)
    assert pythonGraph.create_color(255, 242, 20) == \
        pythonGraph.get_color(170, 125)
    assert pythonGraph.create_color(52, 157, 20) == \
        pythonGraph.get_color(110, 200)


def test_draw_line():
    pythonGraph.draw_line(150, 150, 250, 150, pythonGraph.colors.RED)

    assert pythonGraph.colors.RED == pythonGraph.get_color(150, 150)
    assert pythonGraph.colors.RED == pythonGraph.get_color(250, 150)

    assert pythonGraph.colors.RED == pythonGraph.get_color(200, 150)

    assert pythonGraph.colors.WHITE == pythonGraph.get_color(149, 150)
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(251, 150)


def test_draw_pixel():
    pythonGraph.draw_pixel(2, 2, pythonGraph.colors.RED)

    assert pythonGraph.colors.RED == pythonGraph.get_color(2, 2)

    assert pythonGraph.colors.WHITE == pythonGraph.get_color(1, 1)
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(3, 3)


def test_draw_rectangle_filled():
    pythonGraph.draw_rectangle(150, 150, 250, 200, pythonGraph.colors.RED,
                               True)

    # points inside recntangle
    assert pythonGraph.colors.RED == pythonGraph.get_color(150, 150)
    assert pythonGraph.colors.RED == pythonGraph.get_color(250, 150)
    assert pythonGraph.colors.RED == pythonGraph.get_color(150, 200)
    assert pythonGraph.colors.RED == pythonGraph.get_color(250, 200)
    assert pythonGraph.colors.RED == pythonGraph.get_color(200, 175)

    # points outside rectangle
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(149, 149)
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(251, 201)


def test_draw_rectangle_not_filled():
    pythonGraph.draw_rectangle(150, 150, 250, 200, pythonGraph.colors.RED,
                               False)

    # points on recntangle's circumference
    assert pythonGraph.colors.RED == pythonGraph.get_color(150, 150)
    assert pythonGraph.colors.RED == pythonGraph.get_color(250, 150)
    assert pythonGraph.colors.RED == pythonGraph.get_color(150, 200)
    assert pythonGraph.colors.RED == pythonGraph.get_color(250, 200)

    # point inside rectangle
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(200, 175)

    # points outside rectangle
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(149, 149)
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(251, 201)


def test_draw_text():
    # FIXME: Reuse same test case as write_text
    #   Not sure what's happenning here: When invoking the same code as
    # test_write_text, Python crashes on macOS Mojave (10.14.6) with Python
    # 2.7.17, but each test case executes okay in isolation (i.e., when the
    # other is removed).
    """
    pythonGraph.draw_text('Hello, World!', 1, 1, pythonGraph.colors.BLACK, 64)

    assert pythonGraph.colors.BLACK == pythonGraph.get_color(5, 5)

    assert pythonGraph.colors.WHITE == pythonGraph.get_color(1, 1)
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(100, 100)
    """
    with mock.patch('pythonGraph.write_text') as mock_write_text:
        pythonGraph.write_text('Hello, World!', 1, 1,
                               pythonGraph.colors.BLACK, 64)

        mock_write_text.assert_called_once_with('Hello, World!', 1, 1,
                                                pythonGraph.colors.BLACK, 64)


def test_write_text():
    pythonGraph.write_text('Hello, World!', 1, 1, pythonGraph.colors.BLACK, 64)

    assert pythonGraph.colors.BLACK == pythonGraph.get_color(5, 5)

    assert pythonGraph.colors.WHITE == pythonGraph.get_color(1, 1)
    assert pythonGraph.colors.WHITE == pythonGraph.get_color(100, 100)


def test_get_window_height():
    assert 300 == pythonGraph.get_window_height()


def test_get_window_width():
    assert 400 == pythonGraph.get_window_width()


@mock.patch('pygame.time.delay')
@mock.patch('pygame.display.update')
@mock.patch('pygame.event.pump')
def test_update_window(mock_pump, mock_update, mock_delay):
    pythonGraph.update_window()

    mock_pump.assert_called_once_with()
    mock_update.assert_called_once_with()
    mock_delay.assert_called_once()
