"""Write one funny out-of-office auto-reply line to /output/entry.txt.

Entry for make.fun's "The Funniest Out-of-Office" bounty
(u-kreutzx-the-funniest-out-of-office-054815cf).

Standard library only.
"""

import os

ENTRY = (
    "I'm away until Monday \u2014 my auto-reply has taken over my inbox. "
    "It answers faster than I ever did, so HR is interviewing it for my job."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
