# whatsapp-automated-messenger
Features: - Schedule messages to be sent at a specific time. - Customize the recipient's phone number and message content. - Learn the basics of using PyWhatKit for WhatsApp automation.


```markdown
# WhatsApp Message Sender using Python and PyWhatKit

This repository contains a simple Python script that demonstrates how to use the PyWhatKit library to automate sending WhatsApp messages. The script showcases the ability to schedule messages to be sent at specific times to designated contacts on WhatsApp.

![WhatsApp Message Sender](sample-image.png)

## Features

- Schedule messages to be sent at a specific time.
- Customize the recipient's phone number and message content.
- Learn the basics of using PyWhatKit for WhatsApp automation.

## Getting Started

Follow these steps to get started with the WhatsApp Message Sender:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/abijithka678/whatsapp-message-sender-python.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd whatsapp-message-sender-python
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install pywhatkit
   ```

4. Open the `whatsapp_message_sender.py` script and update the `phone_number` and `message` variables with the recipient's phone number and the desired message.

5. Run the script:

   ```bash
   python whatsapp_message_sender.py
   ```

6. Scan the QR code with your WhatsApp app to establish a connection with WhatsApp Web.

7. The script will schedule the message to be sent after a specified time (adjust the scheduled time in the script).

## Example Usage

```python
import pywhatkit as kit
from datetime import datetime

# Replace these values with your recipient's information
phone_number = "+1234567890"  # Include the country code
message = "Hello, this is a test message."

# Get the current time
now = datetime.now()
hours = now.hour
minutes = now.minute

# Schedule the message to be sent after 1 minute (adjust as needed)
scheduled_time = (hours, minutes + 1)

# Send the message
kit.sendwhatmsg(phone_number, message, *scheduled_time)
```

## Contributing

Contributions are welcome! If you find a bug or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer:** This project is for educational purposes only. Use it responsibly and in compliance with WhatsApp's terms of service.
```
