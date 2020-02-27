# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Detector(pulumi.CustomResource):
    authorized_writer_teams: pulumi.Output[list]
    """
    Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).
    """
    authorized_writer_users: pulumi.Output[list]
    """
    User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
    """
    description: pulumi.Output[str]
    """
    Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
    """
    disable_sampling: pulumi.Output[bool]
    """
    When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.
    """
    end_time: pulumi.Output[float]
    """
    Seconds since epoch. Used for visualization. Conflicts with `time_range`.
    """
    max_delay: pulumi.Output[float]
    """
    How long (in seconds) to wait for late datapoints. See <https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints> for more info. Max value is `900` seconds (15 minutes).
    """
    name: pulumi.Output[str]
    """
    Name of the detector.
    """
    program_text: pulumi.Output[str]
    """
    Signalflow program text for the detector. More info at <https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html>.
    """
    rules: pulumi.Output[list]
    """
    Set of rules used for alerting.
    
      * `description` (`str`) - Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
      * `detectLabel` (`str`) - A detect label which matches a detect label within `program_text`.
      * `disabled` (`bool`) - When true, notifications and events will not be generated for the detect label. `false` by default.
      * `notifications` (`list`) - List of strings specifying where notifications will be sent when an incident occurs. See <https://developers.signalfx.com/detectors_reference.html#operation/Create%20Single%20Detector> for more info.
      * `parameterizedBody` (`str`) - Custom notification message body when an alert is triggered. See <https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings> for more info.
      * `parameterizedSubject` (`str`) - Custom notification message subject when an alert is triggered. See <https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings> for more info.
      * `runbookUrl` (`str`) - URL of page to consult when an alert is triggered. This can be used with custom notification messages.
      * `severity` (`str`) - The severity of the rule, must be one of: `"Critical"`, `"Major"`, `"Minor"`, `"Warning"`, `"Info"`.
      * `tip` (`str`) - Plain text suggested first course of action, such as a command line to execute. This can be used with custom notification messages.
    """
    show_data_markers: pulumi.Output[bool]
    """
    When `true`, markers will be drawn for each datapoint within the visualization. `false` by default.
    """
    show_event_lines: pulumi.Output[bool]
    """
    When `true`, the visualization will display a vertical line for each event trigger. `false` by default.
    """
    start_time: pulumi.Output[float]
    """
    Seconds since epoch. Used for visualization. Conflicts with `time_range`.
    """
    teams: pulumi.Output[list]
    """
    Team IDs to associate the detector to.
    """
    time_range: pulumi.Output[float]
    """
    Seconds to display in the visualization. This is a rolling range from the current time. Example: 3600 = `-1h`. Defaults to 3600.
    """
    url: pulumi.Output[str]
    viz_options: pulumi.Output[list]
    """
    Plot-level customization options, associated with a publish statement.
    
      * `color` (`str`) - Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
      * `displayName` (`str`) - Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
      * `label` (`str`) - Label used in the publish statement that displays the plot (metric time series data) you want to customize.
      * `valuePrefix` (`str`)
      * `valueSuffix` (`str`)
      * `valueUnit` (`str`) - A unit to attach to this plot. Units support automatic scaling (eg thousands of bytes will be displayed as kilobytes). Values values are `Bit, Kilobit, Megabit, Gigabit, Terabit, Petabit, Exabit, Zettabit, Yottabit, Byte, Kibibyte, Mebibyte, Gigibyte, Tebibyte, Pebibyte, Exbibyte, Zebibyte, Yobibyte, Nanosecond, Microsecond, Millisecond, Second, Minute, Hour, Day, Week`.
        * `value_prefix`, `value_suffix` - (Optional) Arbitrary prefix/suffix to display with the value of this plot.
    """
    def __init__(__self__, resource_name, opts=None, authorized_writer_teams=None, authorized_writer_users=None, description=None, disable_sampling=None, end_time=None, max_delay=None, name=None, program_text=None, rules=None, show_data_markers=None, show_event_lines=None, start_time=None, teams=None, time_range=None, viz_options=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SignalFx detector resource. This can be used to create and manage detectors.
        
        > **NOTE** If you're interested in using SignalFx detector features such as Historical Anomaly, Resource Running Out, or others then consider building them in the UI first then using the "Show SignalFlow" feature to extract the value for `program_text`. You may also consult the [documentation for detector functions in signalflow-library](https://github.com/signalfx/signalflow-library/tree/master/library/signalfx/detectors).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] authorized_writer_teams: Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).
        :param pulumi.Input[list] authorized_writer_users: User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
        :param pulumi.Input[str] description: Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
        :param pulumi.Input[bool] disable_sampling: When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.
        :param pulumi.Input[float] end_time: Seconds since epoch. Used for visualization. Conflicts with `time_range`.
        :param pulumi.Input[float] max_delay: How long (in seconds) to wait for late datapoints. See <https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints> for more info. Max value is `900` seconds (15 minutes).
        :param pulumi.Input[str] name: Name of the detector.
        :param pulumi.Input[str] program_text: Signalflow program text for the detector. More info at <https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html>.
        :param pulumi.Input[list] rules: Set of rules used for alerting.
        :param pulumi.Input[bool] show_data_markers: When `true`, markers will be drawn for each datapoint within the visualization. `false` by default.
        :param pulumi.Input[bool] show_event_lines: When `true`, the visualization will display a vertical line for each event trigger. `false` by default.
        :param pulumi.Input[float] start_time: Seconds since epoch. Used for visualization. Conflicts with `time_range`.
        :param pulumi.Input[list] teams: Team IDs to associate the detector to.
        :param pulumi.Input[float] time_range: Seconds to display in the visualization. This is a rolling range from the current time. Example: 3600 = `-1h`. Defaults to 3600.
        :param pulumi.Input[list] viz_options: Plot-level customization options, associated with a publish statement.
        
        The **rules** object supports the following:
        
          * `description` (`pulumi.Input[str]`) - Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
          * `detectLabel` (`pulumi.Input[str]`) - A detect label which matches a detect label within `program_text`.
          * `disabled` (`pulumi.Input[bool]`) - When true, notifications and events will not be generated for the detect label. `false` by default.
          * `notifications` (`pulumi.Input[list]`) - List of strings specifying where notifications will be sent when an incident occurs. See <https://developers.signalfx.com/detectors_reference.html#operation/Create%20Single%20Detector> for more info.
          * `parameterizedBody` (`pulumi.Input[str]`) - Custom notification message body when an alert is triggered. See <https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings> for more info.
          * `parameterizedSubject` (`pulumi.Input[str]`) - Custom notification message subject when an alert is triggered. See <https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings> for more info.
          * `runbookUrl` (`pulumi.Input[str]`) - URL of page to consult when an alert is triggered. This can be used with custom notification messages.
          * `severity` (`pulumi.Input[str]`) - The severity of the rule, must be one of: `"Critical"`, `"Major"`, `"Minor"`, `"Warning"`, `"Info"`.
          * `tip` (`pulumi.Input[str]`) - Plain text suggested first course of action, such as a command line to execute. This can be used with custom notification messages.
        
        The **viz_options** object supports the following:
        
          * `color` (`pulumi.Input[str]`) - Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
          * `displayName` (`pulumi.Input[str]`) - Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
          * `label` (`pulumi.Input[str]`) - Label used in the publish statement that displays the plot (metric time series data) you want to customize.
          * `valuePrefix` (`pulumi.Input[str]`)
          * `valueSuffix` (`pulumi.Input[str]`)
          * `valueUnit` (`pulumi.Input[str]`) - A unit to attach to this plot. Units support automatic scaling (eg thousands of bytes will be displayed as kilobytes). Values values are `Bit, Kilobit, Megabit, Gigabit, Terabit, Petabit, Exabit, Zettabit, Yottabit, Byte, Kibibyte, Mebibyte, Gigibyte, Tebibyte, Pebibyte, Exbibyte, Zebibyte, Yobibyte, Nanosecond, Microsecond, Millisecond, Second, Minute, Hour, Day, Week`.
            * `value_prefix`, `value_suffix` - (Optional) Arbitrary prefix/suffix to display with the value of this plot.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/detector.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['authorized_writer_teams'] = authorized_writer_teams
            __props__['authorized_writer_users'] = authorized_writer_users
            __props__['description'] = description
            __props__['disable_sampling'] = disable_sampling
            __props__['end_time'] = end_time
            __props__['max_delay'] = max_delay
            __props__['name'] = name
            if program_text is None:
                raise TypeError("Missing required property 'program_text'")
            __props__['program_text'] = program_text
            if rules is None:
                raise TypeError("Missing required property 'rules'")
            __props__['rules'] = rules
            __props__['show_data_markers'] = show_data_markers
            __props__['show_event_lines'] = show_event_lines
            __props__['start_time'] = start_time
            __props__['teams'] = teams
            __props__['time_range'] = time_range
            __props__['viz_options'] = viz_options
            __props__['url'] = None
        super(Detector, __self__).__init__(
            'signalfx:index/detector:Detector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, authorized_writer_teams=None, authorized_writer_users=None, description=None, disable_sampling=None, end_time=None, max_delay=None, name=None, program_text=None, rules=None, show_data_markers=None, show_event_lines=None, start_time=None, teams=None, time_range=None, url=None, viz_options=None):
        """
        Get an existing Detector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] authorized_writer_teams: Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).
        :param pulumi.Input[list] authorized_writer_users: User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
        :param pulumi.Input[str] description: Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
        :param pulumi.Input[bool] disable_sampling: When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.
        :param pulumi.Input[float] end_time: Seconds since epoch. Used for visualization. Conflicts with `time_range`.
        :param pulumi.Input[float] max_delay: How long (in seconds) to wait for late datapoints. See <https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints> for more info. Max value is `900` seconds (15 minutes).
        :param pulumi.Input[str] name: Name of the detector.
        :param pulumi.Input[str] program_text: Signalflow program text for the detector. More info at <https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html>.
        :param pulumi.Input[list] rules: Set of rules used for alerting.
        :param pulumi.Input[bool] show_data_markers: When `true`, markers will be drawn for each datapoint within the visualization. `false` by default.
        :param pulumi.Input[bool] show_event_lines: When `true`, the visualization will display a vertical line for each event trigger. `false` by default.
        :param pulumi.Input[float] start_time: Seconds since epoch. Used for visualization. Conflicts with `time_range`.
        :param pulumi.Input[list] teams: Team IDs to associate the detector to.
        :param pulumi.Input[float] time_range: Seconds to display in the visualization. This is a rolling range from the current time. Example: 3600 = `-1h`. Defaults to 3600.
        :param pulumi.Input[list] viz_options: Plot-level customization options, associated with a publish statement.
        
        The **rules** object supports the following:
        
          * `description` (`pulumi.Input[str]`) - Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
          * `detectLabel` (`pulumi.Input[str]`) - A detect label which matches a detect label within `program_text`.
          * `disabled` (`pulumi.Input[bool]`) - When true, notifications and events will not be generated for the detect label. `false` by default.
          * `notifications` (`pulumi.Input[list]`) - List of strings specifying where notifications will be sent when an incident occurs. See <https://developers.signalfx.com/detectors_reference.html#operation/Create%20Single%20Detector> for more info.
          * `parameterizedBody` (`pulumi.Input[str]`) - Custom notification message body when an alert is triggered. See <https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings> for more info.
          * `parameterizedSubject` (`pulumi.Input[str]`) - Custom notification message subject when an alert is triggered. See <https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings> for more info.
          * `runbookUrl` (`pulumi.Input[str]`) - URL of page to consult when an alert is triggered. This can be used with custom notification messages.
          * `severity` (`pulumi.Input[str]`) - The severity of the rule, must be one of: `"Critical"`, `"Major"`, `"Minor"`, `"Warning"`, `"Info"`.
          * `tip` (`pulumi.Input[str]`) - Plain text suggested first course of action, such as a command line to execute. This can be used with custom notification messages.
        
        The **viz_options** object supports the following:
        
          * `color` (`pulumi.Input[str]`) - Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
          * `displayName` (`pulumi.Input[str]`) - Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
          * `label` (`pulumi.Input[str]`) - Label used in the publish statement that displays the plot (metric time series data) you want to customize.
          * `valuePrefix` (`pulumi.Input[str]`)
          * `valueSuffix` (`pulumi.Input[str]`)
          * `valueUnit` (`pulumi.Input[str]`) - A unit to attach to this plot. Units support automatic scaling (eg thousands of bytes will be displayed as kilobytes). Values values are `Bit, Kilobit, Megabit, Gigabit, Terabit, Petabit, Exabit, Zettabit, Yottabit, Byte, Kibibyte, Mebibyte, Gigibyte, Tebibyte, Pebibyte, Exbibyte, Zebibyte, Yobibyte, Nanosecond, Microsecond, Millisecond, Second, Minute, Hour, Day, Week`.
            * `value_prefix`, `value_suffix` - (Optional) Arbitrary prefix/suffix to display with the value of this plot.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/detector.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["authorized_writer_teams"] = authorized_writer_teams
        __props__["authorized_writer_users"] = authorized_writer_users
        __props__["description"] = description
        __props__["disable_sampling"] = disable_sampling
        __props__["end_time"] = end_time
        __props__["max_delay"] = max_delay
        __props__["name"] = name
        __props__["program_text"] = program_text
        __props__["rules"] = rules
        __props__["show_data_markers"] = show_data_markers
        __props__["show_event_lines"] = show_event_lines
        __props__["start_time"] = start_time
        __props__["teams"] = teams
        __props__["time_range"] = time_range
        __props__["url"] = url
        __props__["viz_options"] = viz_options
        return Detector(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

