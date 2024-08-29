# NetHammer

**NetHammer** is a powerful tool designed to simulate Distributed Denial of Service (DDoS) attacks for network stress testing and educational purposes.

## Features

- Customizable attack parameters (requests per second, attack duration)
- Bypasses SSL certificate verification for HTTPS targets
- Easy-to-use interface

## Installation

Follow the steps below to install and run NetHammer:

### Prerequisites

Ensure you have Python 3.x installed on your system. You'll also need to install a few Python libraries:

- `requests`
- `rich`
- `urllib3`

You can install these dependencies using `pip`.

### Step 1: Clone the Repository

First, clone the NetHammer repository from GitHub:

```bash
git clone https://github.com/rakibhakas/nethammer.git
cd nethammer
```

### Step 2: Install Required Python Packages

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is not included, you can manually install the required packages:

```bash
pip install requests rich urllib3
```

### Step 3: Run the Script

You’re now ready to run NetHammer. Execute the script with:

```bash
python nethammer.py
```

### Usage

When you run the script, you'll be prompted to enter the target website, the number of requests per second, and the duration of the attack. Here's an example:

```bash
Enter the target website: https://example.com
Enter the number of requests to send per second: 100
Enter the duration of the attack in seconds: 60
```

### Disclaimer

NetHammer is intended for educational purposes and network stress testing within legal environments only. Unauthorized use of this tool to conduct DDoS attacks is illegal and unethical. The author and contributors are not responsible for any misuse of this tool.

---

This `README.md` section provides clear instructions on how to install and run NetHammer, making it easier for others to use your tool responsibly.
