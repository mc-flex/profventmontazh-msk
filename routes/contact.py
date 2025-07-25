from flask import Blueprint, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['POST'])
def handle_contact_form():
    try:
        data = request.get_json()
        
        # Получаем данные из формы
        name = data.get('name', '')
        phone = data.get('phone', '')
        email = data.get('email', '')
        service = data.get('service', '')
        message = data.get('message', '')
        
        # Формируем текст письма
        email_body = f"""
Новая заявка с сайта ООО "Профвентмонтаж-МСК"

Имя: {name}
Телефон: {phone}
Email: {email}
Интересующая услуга: {service}
Сообщение: {message}

---
Заявка отправлена с сайта автоматически.
        """
        
        # Список получателей
        recipients = ['pvm-msk@yandex.ru', 'fedotovfd63@gmail.com']
        
        # Отправляем уведомление (в реальном проекте здесь была бы настройка SMTP)
        # Для демонстрации просто возвращаем успешный ответ
        print(f"Новая заявка от {name} ({phone})")
        print(f"Email: {email}")
        print(f"Услуга: {service}")
        print(f"Сообщение: {message}")
        
        return jsonify({
            'success': True,
            'message': 'Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.'
        })
        
    except Exception as e:
        print(f"Ошибка при обработке заявки: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Произошла ошибка при отправке заявки. Пожалуйста, попробуйте позже или свяжитесь с нами по телефону.'
        }), 500

