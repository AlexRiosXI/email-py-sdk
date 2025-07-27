
class EmailConfig:
    def __init__(self, smtp_server, smtp_port, email_address, email_password, tls=True):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_address = email_address
        self.email_password = email_password
        self.tls = tls