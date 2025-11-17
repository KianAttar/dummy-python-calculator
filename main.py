"""Main entry point for the calculator application."""

import sys
import argparse


def main():
    """Main function to launch the calculator."""
    parser = argparse.ArgumentParser(description='Python Calculator')
    parser.add_argument('--cli', action='store_true', help='Use CLI mode')
    parser.add_argument('--gui', action='store_true', help='Use GUI mode (default)')
    
    args = parser.parse_args()
    
    if args.cli:
        print("CLI mode - Coming soon...")
    else:
        print("GUI mode - Coming soon...")


if __name__ == "__main__":
    main()
