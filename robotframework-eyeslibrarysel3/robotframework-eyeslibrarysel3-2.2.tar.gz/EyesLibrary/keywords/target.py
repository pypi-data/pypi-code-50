#!/usr/bin/env python

from __future__ import absolute_import
from applitools.geometry import Region
from applitools.selenium.target import (
    Target,
    IgnoreRegionByElement,
    IgnoreRegionBySelector,
    FloatingRegion,
    FloatingRegionByElement,
    FloatingRegionBySelector,
    FloatingBounds,
)
from EyesLibrary.resources import utils


class TargetKeywords:
    def ignore_region_by_coordinates(self, left, top, width, height, target=None):
        """
        Returns a Target object that ignores the region specified in the arguments.
        See `Defining Ignore and Floating Regions`.

            | =Arguments=     | =Description=                                                                                    |
            | Left (float)    | *Mandatory* - The left coordinate of the region to ignore e.g. 100                               |
            | Top (float)     | *Mandatory* - The top coordinate of the region to ignore e.g. 150                                |
            | Width (float)   | *Mandatory* - The width of the region to ignore e.g. 500                                         |
            | Height (float)  | *Mandatory* - The height of the region to ignore e.g. 120                                        |
            | Target (Target) | The previously existent Target, to be used if a ignore region or floating region was already set |
                
        *Example:*
            | ${target}=        | Ignore Region By Coordinates | 10               | 20 | 100 | 100 |
            | Check Eyes Window | Google Homepage              | target=${target} |

        """

        if target is None:
            target = Target()

        ignore_region = Region(float(left), float(top), float(width), float(height))
        target.ignore(ignore_region)

        return target

    def ignore_region_by_element(self, element, target=None):
        """
        Returns a Target object that ignores the region of the element specified in the arguments.
        See `Defining Ignore and Floating Regions`.

            | =Arguments=          | =Description=                                                                                    |
            | Element (WebElement) | *Mandatory* - The WebElement to ignore                                                           |
            | Target (Target)      | The previously existent Target, to be used if a ignore region or floating region was already set |
                
        *Example:*
            | ${element}=       | Get Webelement           | //*[@id="hplogo"] |
            | ${target}=        | Ignore Region By Element | ${element}        | 
            | Check Eyes Window | Google Homepage          | target=${target}  |
        """

        if target is None:
            target = Target()

        ignore_region = IgnoreRegionByElement(element)
        target.ignore(ignore_region)

        return target

    def ignore_region_by_selector(self, value, selector="id", target=None):
        """
        Returns a Target object that ignores the region of the element specified in the arguments by selector and value.
        See `Defining Ignore and Floating Regions` and `Using Selectors`

            | =Arguments=     | =Description=                                                                                                |
            | Value (str)     | *Mandatory* - The specific value of the selector. e.g. a CSS SELECTOR value .first.expanded.dropdown         |
            | Selector (str)  | *Mandatory* - The strategy to locate the element. The supported selectors are specified in `Using Selectors` |
            | Target (Target) | The previously existent Target, to be used if a ignore region or floating region was already set             |
                
        *Example:*
            | ${target}=        | Ignore Region By Selector | .first.expanded.dropdown | css selector |
            | Check Eyes Window | Google Homepage           | target=${target}         |
        """

        if target is None:
            target = Target()

        selector_strategy = utils.get_selector_strategy(selector)
        ignore_region = IgnoreRegionBySelector(selector_strategy, value)
        target.ignore(ignore_region)

        return target

    def floating_region_by_coordinates(
        self,
        left,
        top,
        width,
        height,
        max_left_offset=0,
        max_top_offset=0,
        max_right_offset=0,
        max_down_offset=0,
        target=None,
    ):
        """
        Returns a Target object that includes the floating region specified in the arguments.
        See `Defining Ignore and Floating Regions`

            | =Arguments=            | =Description=                                                                                    |
            | Left (float)           | *Mandatory* - The left coordinate of the floating region e.g. 100                                |
            | Top (float)            | *Mandatory* - The top coordinate of the floating region e.g. 150                                 |
            | Width (float)          | *Mandatory* - The width of the floating region e.g. 500                                          |
            | Height (float)         | *Mandatory* - The height of the floating region e.g. 120                                         |
            | Max Left Offset (int)  | The amount the floating region may move to the left. e.g. 10                                     |
            | Max Top Offset (int)   | The amount the floating region may moveupwards. e.g. 20                                          |
            | Max Right Offset (int) | The amount the floating region may move to the right. e.g. 10                                    |
            | Max Down Offset (int)  | The amount the floating region may move downwards. e.g. 50                                       |
            | Target (Target)        | The previously existent Target, to be used if a ignore region or floating region was already set |
                
        *Example:*
            | ${target}=    Floating Region By Coordinates |  10              | 10               | 200 | 150 | 10 | 0 | 50 | 50 | 
            | Check Eyes Window                            |  Google Homepage | target=${target} |
        """

        if target is None:
            target = Target()

        region = Region(float(left), float(top), float(width), float(height))
        floating_bounds = FloatingBounds(
            int(max_left_offset),
            int(max_top_offset),
            int(max_right_offset),
            int(max_down_offset),
        )
        floating_region = FloatingRegion(region, floating_bounds)
        target.floating(floating_region)

        return target

    def floating_region_by_element(
        self,
        element,
        max_left_offset=0,
        max_top_offset=0,
        max_right_offset=0,
        max_down_offset=0,
        target=None,
    ):
        """
        Returns a Target object that includes the floating region containing the element specified in the arguments.
        See `Defining Ignore and Floating Regions`.

            | =Arguments=            | =Description=                                                                                    |
            | Element (WebElement)   | *Mandatory* - The WebElement that determines the floating region                                 |
            | Max Left Offset (int)  | The amount the floating region may move to the left. e.g. 10                                     |
            | Max Top Offset (int)   | The amount the floating region may moveupwards. e.g. 20                                          |
            | Max Right Offset (int) | The amount the floating region may move to the right. e.g. 10                                    |
            | Max Down Offset (int)  | The amount the floating region may move downwards. e.g. 50                                       |
            | Target (Target)        | The previously existent Target, to be used if a ignore region or floating region was already set |
                
        *Example:*
            | ${element}=       | Get Element                | //*[@id="hplogo"] |
            | ${target}=        | Floating Region By Element | ${element}        | 10 | 20 | 0 | 10 |
            | Check Eyes Window | Google Homepage            | target={target}   |
        """

        if target is None:
            target = Target()

        floating_bounds = FloatingBounds(
            int(max_left_offset),
            int(max_top_offset),
            int(max_right_offset),
            int(max_down_offset),
        )
        floating_region = FloatingRegionByElement(element, floating_bounds)
        target.floating(floating_region)

        return target

    def floating_region_by_selector(
        self,
        value,
        selector="id",
        max_left_offset=0,
        max_top_offset=0,
        max_right_offset=0,
        max_down_offset=0,
        target=None,
    ):
        """
        Returns a Target object that includes the floating region containing the element specified in the arguments by selector and value.
        See `Defining Ignore and Floating Regions` and `Using Selectors`.

            | =Arguments=            | =Description=                                                                                                |
            | Value (str)            | *Mandatory* - The specific value of the selector. e.g. a CSS SELECTOR value .first.expanded.dropdown         |
            | Selector (str)         | *Mandatory* - The strategy to locate the element. The supported selectors are specified in `Using Selectors` |
            | Max Left Offset (int)  | The amount the floating region may move to the left. e.g. 10                                                 |
            | Max Top Offset (int)   | The amount the floating region may moveupwards. e.g. 20                                                      |
            | Max Right Offset (int) | The amount the floating region may move to the right. e.g. 10                                                |
            | Max Down Offset (int)  | The amount the floating region may move downwards. e.g. 50                                                   |
            | Target (Target)        | The previously existent Target, to be used if a ignore region or floating region was already set             |
                
        *Example:*
            | ${target}=        | Floating Region By Selector | .first.expanded.dropdown | css selector | 20 | 10 | 20 | 10 |
            | Check Eyes Window | Google Homepage             | target=${target}         |
        """

        if target is None:
            target = Target()

        selector_strategy = utils.get_selector_strategy(selector)
        floating_bounds = FloatingBounds(
            int(max_left_offset),
            int(max_top_offset),
            int(max_right_offset),
            int(max_down_offset),
        )
        floating_region = FloatingRegionBySelector(
            selector_strategy, value, floating_bounds
        )
        target.floating(floating_region)

        return target

    def ignore_caret(self, ignore=True, target=None):
        """
        Returns a Target object that determines whether a blinking cursor should be ignored or not.
        See `Defining Ignore and Floating Regions`.

            | =Arguments=            | =Description=                                                                                                |
            | Ignore (bool)          | If true, Eyes should detect mismatch artifacts caused by a blinking cursor and not report them as mismatches |
            | Target (Target)        | The previously existent Target, to be used if a ignore region or floating region was already set             |
                
        *Example:*
            | ${target}=        | Ignore Caret    | ${false}         |
            | Check Eyes Window | Google Homepage | target=${target} |
        """

        if target is None:
            target = Target()

        target.ignore_caret(ignore)
        return target
