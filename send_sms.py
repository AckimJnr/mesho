import africastalking
import os

# Initialize Africa's Talking
africastalking.initialize(
    username="edgedup",  # Replace with your Africa's Talking username
    api_key=os.getenv("AT_API_KEY")  # Load your API key from an environment variable
)

# Get the SMS service
sms = africastalking.SMS

class SMSHandler:
    def send_sms(self, recipients, message, sender=None):
        """
        Sends an SMS to the specified recipients using Africa's Talking.
        
        Args:
            recipients (list): A list of recipient phone numbers in international format.
            message (str): The message to send.
            sender (str): The sender ID or shortcode (optional).
        """
        try:
            # Send the message
            response = sms.send(message, recipients, sender_id=sender)
            print("SMS sent successfully. Response:")
            print(response)
        except Exception as e:
            print(f"An error occurred while sending SMS: {e}")

# Example usage
if __name__ == "__main__":
    handler = SMSHandler()
    # recipients = ["+265996406739", "+265992998262", "+265987598659"]  # Replace with actual recipient numbers
    recipients = ["+265984007917"]
    message = "Hey AT Ninja!, mesho v1 will be live soon. Stay tuned!"  # Replace with your message
    sender_id = "3067"  # Replace with your sender ID if needed
    handler.send_sms(recipients, message, sender=sender_id)
