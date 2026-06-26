#!/usr/bin/env python3
"""Simple requirements checker.

Reads requirements.txt and reports missing or incompatible installed packages.
"""
import sys
from pkg_resources import Requirement, get_distribution, DistributionNotFound


def read_requirements(path="requirements.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f if l.strip() and not l.strip().startswith("#")]
        return lines
    except FileNotFoundError:
        print(f"requirements file not found: {path}")
        return []


def check_line(line):
    try:
        req = Requirement.parse(line)
        dist = get_distribution(req.name)
        if dist not in req:
            return False, f"installed {dist.version} does not satisfy {req.specifier}"
        return True, f"installed {dist.version} OK"
    except DistributionNotFound:
        return False, "not installed"
    except Exception as e:
        return False, f"error: {e}"


def main():
    reqs = read_requirements()
    if not reqs:
        print("No requirements found in requirements.txt")
        return 0

    all_ok = True
    print("Checking requirements:\n")
    for r in reqs:
        ok, msg = check_line(r)
        status = "OK" if ok else "MISSING/INCOMPATIBLE"
        print(f"{r:60s} : {status}  -- {msg}")
        if not ok:
            all_ok = False

    if all_ok:
        print("\nAll requirements satisfied.")
        return 0
    else:
        print("\nSome requirements are missing or incompatible. Consider running:\n    pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())
