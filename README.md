# Sierra Madre Email

A comprehensive email SDK for Python applications that provides easy-to-use email functionality with support for HTML templates, attachments, and multiple sending modes.

## Features

- **Multiple Sending Modes**: Support for direct emails and BCC (blind carbon copy)
- **HTML Content**: Rich HTML email content with template support
- **File Attachments**: Add multiple file attachments to emails
- **Template System**: HTML template support with placeholder replacement
- **SMTP Configuration**: Flexible SMTP server configuration
- **Error Handling**: Comprehensive error handling and failed send tracking
- **Multiple Recipients**: Support for multiple email addresses
- **TLS Support**: Secure email transmission with TLS encryption

## Installation

```bash
pip install sierra-madre-email
```

## Quick Start

### Basic Configuration

```python
from sierra_madre_email import Email, EmailConfig

# Configure email settings
config = EmailConfig(
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    email_address="your-email@gmail.com",
    email_password="your-app-password",  # Use app password for Gmail
    tls=True
)

# Create email instance
email = Email(config)
```

### Simple Email Example

```python
from sierra_madre_email import Email, EmailConfig

# Setup configuration
config = EmailConfig(
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    email_address="your-email@gmail.com",
    email_password="your-app-password",
    tls=True
)

# Create email
email = Email(config)

# Add recipients
email.add_address("recipient@example.com")
email.add_addresses(["user1@example.com", "user2@example.com"])

# Set content
email.add_subject("Welcome to our service!")
email.add_content("<h1>Hello!</h1><p>This is a test email.</p>")

# Send email
email.send_email()
```

## Advanced Usage

### Using HTML Templates

```python
from sierra_madre_email import Email, EmailConfig

config = EmailConfig(
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    email_address="your-email@gmail.com",
    email_password="your-app-password",
    tls=True
)

email = Email(config)

# Add recipients
email.add_addresses([
    "user1@example.com",
    "user2@example.com",
    "user3@example.com"
])

# Load HTML template with placeholders
email.add_html_content("templates/welcome.html")

# Replace placeholders
placeholders = {
    "{{name}}": "John Doe",
    "{{company}}": "My Company",
    "{{date}}": "2024-01-15"
}
email.update_placeholders(placeholders)

email.add_subject("Welcome to {{company}}")
email.send_email()
```

### Email with Attachments

```python
from sierra_madre_email import Email, EmailConfig

config = EmailConfig(
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    email_address="your-email@gmail.com",
    email_password="your-app-password",
    tls=True
)

email = Email(config)

# Add recipient
email.add_address("client@example.com")

# Set content
email.add_subject("Documents attached")
email.add_content("<h1>Hello!</h1><p>Please find the requested documents attached.</p>")

# Add attachments
email.add_attachment("documents/invoice.pdf")
email.add_attachment("documents/contract.docx")

# Add multiple attachments at once
email.add_attachments([
    "documents/report.pdf",
    "documents/presentation.pptx"
])

email.send_email()
```

### BCC Email (Blind Carbon Copy)

```python
from sierra_madre_email import Email, EmailConfig

config = EmailConfig(
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    email_address="your-email@gmail.com",
    email_password="your-app-password",
    tls=True
)

email = Email(config)

# Add BCC recipients (recipients won't see each other)
email.add_addresses([
    "customer1@example.com",
    "customer2@example.com",
    "customer3@example.com"
])

email.add_subject("Newsletter - January 2024")
email.add_content("<h1>Monthly Newsletter</h1><p>Here's what's new...</p>")

# Send as BCC
email.send_bcc_email()
```

## Configuration

### EmailConfig Parameters

```python
config = EmailConfig(
    smtp_server="smtp.gmail.com",      # SMTP server address
    smtp_port=587,                      # SMTP port (587 for TLS, 465 for SSL)
    email_address="your-email@gmail.com", # Your email address
    email_password="your-app-password",   # Your email password or app password
    tls=True                            # Enable TLS encryption (recommended)
)
```

### Common SMTP Settings

| Provider | SMTP Server | Port | TLS |
|----------|-------------|------|-----|
| Gmail | smtp.gmail.com | 587 | True |
| Outlook | smtp-mail.outlook.com | 587 | True |
| Yahoo | smtp.mail.yahoo.com | 587 | True |
| Custom | your-smtp-server.com | 587 | True |

## Email Class Methods

### Recipient Management

```python
email = Email(config)

# Add single recipient
email.add_address("user@example.com")

# Add multiple recipients
email.add_addresses(["user1@example.com", "user2@example.com"])
```

### Content Management

```python
# Add plain text or HTML content
email.add_content("<h1>Hello World</h1>")

# Load HTML template
email.add_html_content("templates/email.html")

# Update placeholders in content
placeholders = {"{{name}}": "John", "{{company}}": "Acme Corp"}
email.update_placeholders(placeholders)
```

### Attachment Management

```python
# Add single attachment
email.add_attachment("path/to/file.pdf")

# Add multiple attachments
email.add_attachments(["file1.pdf", "file2.docx", "file3.jpg"])
```

### Sending Methods

```python
# Send regular email (recipients visible to each other)
email.send_email()

# Send BCC email (recipients hidden from each other)
email.send_bcc_email()
```

## Error Handling

The SDK provides comprehensive error handling:

```python
try:
    email.send_email()
except EmailError as e:
    print(f"Email error: {e}")

# Check for failed sends
if email.failed_sent:
    print(f"Failed to send to: {email.failed_sent}")
```

## HTML Template Example

Create a template file `templates/welcome.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>Welcome {{name}}!</h1>
    <p>Thank you for joining {{company}}.</p>
    <p>Your registration date: {{date}}</p>
    <p>Best regards,<br>The {{company}} Team</p>
</body>
</html>
```

## Security Best Practices

1. **Use App Passwords**: For Gmail, use app passwords instead of your main password
2. **Enable TLS**: Always use TLS encryption for secure transmission
3. **Environment Variables**: Store sensitive credentials in environment variables
4. **Validate Inputs**: Always validate email addresses and content

```python
import os
from dotenv import load_dotenv

load_dotenv()

config = EmailConfig(
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    email_address=os.getenv("EMAIL_ADDRESS"),
    email_password=os.getenv("EMAIL_PASSWORD"),
    tls=True
)
```

## Dependencies

- `smtplib`: Built-in Python SMTP library
- `email`: Built-in Python email handling
- `sierra-madre-core`: Core functionality (if applicable)

## Environment Variables

Set the following environment variables:

```bash
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

## License

This project is licensed under the MIT License.
