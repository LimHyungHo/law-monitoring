import smtplib
import os
from email.message import EmailMessage
from email.policy import SMTP
from app.config.settings import settings


class MailService:

    def send_mail_with_attachments(self, subject, body, file_paths, recipient_email=None):
        recipient = (recipient_email or settings.MAIL_TO or "").strip()
        if not recipient:
            raise ValueError("메일 수신자가 설정되지 않았습니다.")
        if not settings.MAIL_USER or not settings.MAIL_PASSWORD:
            raise ValueError("메일 발송 계정이 설정되지 않았습니다.")

        msg = EmailMessage(policy=SMTP)
        msg["Subject"] = subject
        msg["From"] = settings.MAIL_USER
        msg["To"] = recipient
        msg.set_content(body, subtype="plain", charset="utf-8")

        # 🔥 여러 파일 첨부
        for file_path in file_paths:
            with open(file_path, "rb") as f:
                filename = os.path.basename(file_path)
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="pdf",
                    filename=filename,
                )

        # SMTP
        with smtplib.SMTP_SSL(settings.MAIL_HOST, settings.MAIL_PORT) as smtp:
            smtp.login(settings.MAIL_USER, settings.MAIL_PASSWORD)
            smtp.send_message(msg)

        print("📧 다중 첨부 메일 발송 완료")
