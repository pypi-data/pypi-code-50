import sys
import argparse
from .build import build
from .watch import watch

def entry():
    parser = argparse.ArgumentParser(description='Build and watch website files')
    parser.add_argument('command', type=str, help='Either "watch" or "build"', default=None)
    parser.add_argument('paths', type=str, help='If watching, paths to watch. If building, paths to build', default=None, nargs='*')
    parser.add_argument('--src', type=str, help='Root directory containing source files', default='./src')
    parser.add_argument('--dist', type=str, help='Directory to produce output', default='./dist')
    parser.add_argument('--with-deps', action='store_true', help='Moves all required files from templates to the output directory too')
    parser.add_argument('--interval', type=float, help='How frequently to scan (in seconds)', default=0.5)
    parser.add_argument('--force-build', action='store_true', help='Forces the watcher to build all files on start')            
    args = parser.parse_args()

    if args.command == 'build':
        args = {
            'paths': args.paths,
            'src': args.src,
            'dist': args.dist,
            'with_deps': args.with_deps
        }
        build(**args)
    elif args.command == 'watch':
        args = {
            'paths': args.paths,
            'src': args.src,
            'dist': args.dist,
            'interval': args.interval,
            'force_build': args.force_build
        }
        watch(**args)
    else:
        sys.exit('Must supply either "build" or "watch"')
