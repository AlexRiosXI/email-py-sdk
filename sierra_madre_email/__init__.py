import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from config import EmailConfig

class EmailError(Exception):
    pass


class Email():
    def __init__(self, email_config: EmailConfig):
        self.email_config = email_config
        self.addresses = []
        self.subject = ""
        self.content = ""
        self.attachments = []
        self.failed_sent = []

    def add_address(self, address: str):
        self.addresses.append(address)

    def add_addresses(self, addresses: list):
        for address in addresses:
            self.add_address(address)
    
    def add_subject(self, subject: str):
        self.subject = subject
    
    def add_content(self, content: str):
        self.content = content
    def add_html_content(self,template_path):
        try:
            with open(template_path, 'r',encoding='iso-8859-1') as file:
                template_html = file.read()
            template_html = template_html.encode("iso-8859-1").decode("utf-8")
            string_html=str(template_html)
            self.content = string_html
        except Exception as e:
            raise EmailError(f"Error al decodificar plantilla del correo en el servidor: {e}")

    def add_attachment(self, attachment: str):
        self.attachments.append(attachment)

    def add_attachments(self, attachments: list):
        for attachment in attachments:
            self.add_attachment(attachment)
    def update_placeholders(self,placeholders:dict):
        for key, value in placeholders.items():
            self.content = self.content.replace(key, value)
    

    def send_email(self):
        if self.content == "":
            raise EmailError("You must add content to the email")
        if self.subject == "":
            raise EmailError("You must add a subject to the email")        
            
        smtp = get_smtp_instance(self.email_config)
        
        for recipient in self.addresses:
            message = MIMEMultipart()
            message['From'] = self.email_config.email_address
            message['To'] = recipient
            message['Subject'] = self.subject

            # Add the message content
            body = MIMEText(self.content,"html")
            message.attach(body)

            if self.attachments:
                for attachment in self.attachments:
                    filename = attachment.split("/")[-1]
                    with open(attachment, 'rb') as attachment:
                        attachment = MIMEApplication(attachment.read(), Name=filename)
                    attachment['Content-Disposition'] = f'attachment; filename={filename}'
                    message.attach(attachment)
            try:
                sent = smtp.sendmail(self.email_config.email_address, self.addresses, message.as_string())
            except Exception as e:
                self.failed_sent.append(recipient)
            if sent:
                self.failed_sent.append(recipient)
        smtp.quit()
        
    def send_bcc_email(self):
        if self.content == "":
            raise EmailError("You must add content to the email")
        if self.subject == "":
            raise EmailError("You must add a subject to the email")        
            
        smtp = get_smtp_instance(self.email_config)
        
        message = MIMEMultipart()
        message['From'] = self.email_config.email_address
        message['Bcc'] = self.addresses
        message['To'] = "Undisclosed recipients"
        message['Subject'] = self.subject

        # Add the message content
        body = MIMEText(self.content,"html")
        message.attach(body)

        if self.attachments:
            for attachment in self.attachments:
                filename = attachment.split("/")[-1]
                with open(attachment, 'rb') as attachment:
                    attachment = MIMEApplication(attachment.read(), Name=filename)
                attachment['Content-Disposition'] = f'attachment; filename={filename}'
                message.attach(attachment)
        try:
            sent = smtp.sendmail(self.email_config.email_address, self.addresses, message.as_string())
        except Exception as e:
            raise EmailError("There was an error sending the email, please check that the email is correct")
        if sent:
            self.failed_sent.append(sent)
        smtp.quit()


def get_smtp_instance(email_config: EmailConfig):
    smtp = smtplib.SMTP(email_config.smtp_server, email_config.smtp_port)
    if email_config.tls:
        smtp.starttls()  
    # Login to the email account
    smtp.login(email_config.email_address, email_config.email_password)
    return smtp

