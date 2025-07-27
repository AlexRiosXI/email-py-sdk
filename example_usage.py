#!/usr/bin/env python3
"""
Ejemplo de uso del SDK de Email
"""

from sierra_madre_core import Email, EmailConfig

def example_basic_usage():
    """Ejemplo básico de uso"""
    
    # Configurar el cliente de email
    config = EmailConfig(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        email_address="tu-email@gmail.com",
        email_password="tu-password-app",  # Usar contraseña de aplicación
        tls=True
    )
    
    # Crear instancia de email
    email = Email(config)
    
    # Configurar destinatarios
    email.add_bcc_address("destinatario1@example.com")
    email.add_bcc_address("destinatario2@example.com")
    email.add_bcc_address("destinatario3@example.com")
    
    # O agregar múltiples de una vez
    # email.add_addresses(["dest1@example.com", "dest2@example.com"], "bcc")
    
    # Configurar contenido
    email.add_subject("Prueba de SDK de Email")
    email.add_content("<h1>Hola!</h1><p>Este es un email de prueba.</p>")
    
    # Enviar con CCO (recomendado)
    failed_sends = email.send_email(use_bcc=True)
    
    if failed_sends:
        print(f"Errores al enviar: {failed_sends}")
    else:
        print("Email enviado exitosamente!")

def example_with_template():
    """Ejemplo usando plantilla HTML"""
    
    config = EmailConfig(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        email_address="tu-email@gmail.com",
        email_password="tu-password-app",
        tls=True
    )
    
    email = Email(config)
    
    # Agregar destinatarios
    email.add_addresses([
        "usuario1@example.com",
        "usuario2@example.com",
        "usuario3@example.com"
    ], "bcc")
    
    # Usar plantilla HTML con placeholders
    placeholders = {
        "{{nombre}}": "Juan Pérez",
        "{{empresa}}": "Mi Empresa",
        "{{fecha}}": "2024-01-15"
    }
    
    email.decode_html_template("templates/welcome.html", placeholders)
    email.add_subject("Bienvenido a {{empresa}}")
    
    # Enviar
    failed_sends = email.send_email(use_bcc=True)
    print(f"Enviados exitosamente. Fallidos: {failed_sends}")

def example_with_attachments():
    """Ejemplo con archivos adjuntos"""
    
    config = EmailConfig(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        email_address="tu-email@gmail.com",
        email_password="tu-password-app",
        tls=True
    )
    
    email = Email(config)
    
    # Destinatarios
    email.add_bcc_address("cliente@example.com")
    
    # Contenido
    email.add_subject("Documentos adjuntos")
    email.add_content("<h1>Hola!</h1><p>Adjunto los documentos solicitados.</p>")
    
    # Adjuntos
    email.add_attachment("documentos/factura.pdf")
    email.add_attachment("documentos/contrato.docx")
    
    # Enviar
    failed_sends = email.send_email(use_bcc=True)
    print(f"Email con adjuntos enviado. Fallidos: {failed_sends}")

def example_visible_recipients():
    """Ejemplo con destinatarios visibles (no CCO)"""
    
    config = EmailConfig(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        email_address="tu-email@gmail.com",
        email_password="tu-password-app",
        tls=True
    )
    
    email = Email(config)
    
    # Destinatarios visibles
    email.add_to_address("principal@example.com")
    email.add_cc_address("copia@example.com")
    email.add_cc_address("otro@example.com")
    
    email.add_subject("Reunión de equipo")
    email.add_content("<h1>Agenda de reunión</h1><p>Puntos a discutir...</p>")
    
    # Enviar sin CCO (destinatarios visibles)
    failed_sends = email.send_email(use_bcc=False)
    print(f"Email enviado. Fallidos: {failed_sends}")

if __name__ == "__main__":
    print("Ejemplos de uso del SDK de Email:")
    print("1. Uso básico")
    print("2. Con plantilla HTML")
    print("3. Con adjuntos")
    print("4. Destinatarios visibles")
    
    # Descomenta el ejemplo que quieras probar:
    # example_basic_usage()
    # example_with_template()
    # example_with_attachments()
    # example_visible_recipients() 