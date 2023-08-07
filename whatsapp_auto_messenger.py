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
