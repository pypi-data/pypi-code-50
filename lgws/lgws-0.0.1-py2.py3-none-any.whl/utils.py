import click


class AliasedGroup(click.Group):
    "Group with command aliases, allows l for listen and so on.."

    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx) if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail("Too many matches: %s" % ", ".join(sorted(matches)))


KEYMAP = {
    'esc': ('ic', 'exit'),
    'enter': ('ic', 'enter'),
    'backspace': ('ic', 'back'),
    '=': ('ic', 'volume_up'),
    '-': ('ic', 'volume_down'),
    'i': ('ic', 'info'),
    'h': ('ic', 'home'),
    'm': ('mc', 'mute'),
}
